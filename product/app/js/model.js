/* ================= the model =================
   The arithmetic the whole product rests on.

   CBSE publishes marks per *unit*, not per chapter. So a chapter's stake is
   its unit's marks divided between the chapters in that unit — Calculus
   carries 35 marks across five chapters, so each is worth about seven. That is
   an even split rather than a measured one, and it is the honest assumption to
   make: the board does not publish a per-chapter split, and pretending to know
   one would be inventing precision.

   Everything else follows. You grade each chapter 0-3; a grade of 3 secures
   its stake, 0 secures none of it, and the difference is marks still at risk.
   ================================================================================ */

var SUBJ = {
  maths:   { code:"041", total:80, label:"Mathematics", k:"subj.maths" },
  physics: { code:"042", total:70, label:"Physics",     k:"subj.physics" }
};
var SUBJECTS = ["maths", "physics"];
var GRADES = [0, 1, 2, 3];
//: What a grade is worth, as a share of the chapter's marks. Deliberately
//: linear: a "shaky" chapter really does tend to return about a third of its
//: marks, and a curve here would be a claim nobody can support.
function gradeShare(g){ return (g || 0) / 3; }

//: How much the queue trusts a chapter's marks. A priority-1 chapter is one
//: the board asks almost every year, so marks recovered there are more
//: reliably marks earned. From the frequency analysis in analysis/.
var PRIO_WEIGHT = { 1: 1.0, 2: 0.82, 3: 0.64 };

var CH = DATA.chapters || [];
var byId = {};
CH.forEach(function(c){ byId[c.id] = c; });

// stake: the chapter's share of its unit's marks
(function(){
  var perUnit = {};
  CH.forEach(function(c){ var k = c.subj + "|" + c.unit; perUnit[k] = (perUnit[k] || 0) + 1; });
  CH.forEach(function(c){
    c.siblings = perUnit[c.subj + "|" + c.unit];
    c.stake = c.unitMarks / c.siblings;
  });
})();

// "Unit I (8 marks, shared with Ch 2) · Typical appearance: one 1-mark MCQ…"
// The first clause repeats the unit and the marks, both of which are already
// on screen wherever this is shown. Keep the half that says something.
CH.forEach(function(c){
  var parts = String(c.appear || "").split(" · ");
  if (parts.length > 1 && /^Units? /.test(parts[0])) parts.shift();
  c.appearShort = parts.join(" · ").replace(/^Typical appearance:\s*/i, "");
});

function chapters(subj){
  return CH.filter(function(c){ return c.subj === subj; });
}

/* ---------------- questions ---------------- */
function parseQs(c){
  var sols = {};
  // A locked chapter ships no questions and no solutions: the fields are
  // absent rather than empty, because the point of the gate is that they are
  // not in this file at all.
  (c.s.sol || "").split(/\n(?=### Q\d+\b)/).forEach(function(b){
    var m = b.match(/^### Q(\d+)\b[^\n]*\n?([\s\S]*)$/);
    if (m) sols[m[1]] = (m[2] || "").trim();
  });
  var out = [];
  (c.s.pyq || "").split(/\n(?=\*\*Q\d+\.\*\*)/).forEach(function(b){
    var m = b.match(/^\*\*Q(\d+)\.\*\*\s*(?:\*\(([^)]*)\)\*)?\s*([\s\S]*)$/);
    if (!m) return;
    out.push({ n:m[1], marks:(m[2] || "").replace(/\s*—[\s\S]*/,"").trim(),
               body:(m[3] || "").trim(), sol:sols[m[1]] || "" });
  });
  return out;
}
function requeue(c){ c.qs = parseQs(c); }
CH.forEach(requeue);

/* ---------------- what the student has told us ---------------- */
var PLAN_KEY = "mf.plan";
var plan = { grades:{}, passes:{}, scores:{}, target:85, exam:"" };
try {
  var saved = JSON.parse(localStorage.getItem(PLAN_KEY) || "null");
  if (saved && typeof saved === "object"){
    plan.grades = saved.grades || {};
    plan.passes = saved.passes || {};
    plan.scores = saved.scores || {};
    plan.target = typeof saved.target === "number" ? saved.target : 85;
    plan.exam = saved.exam || "";
  }
} catch(e){}

function savePlan(){
  try { localStorage.setItem(PLAN_KEY, JSON.stringify(plan)); } catch(e){}
}
function gradeOf(id){ return plan.grades[id] || 0; }
function setGrade(id, g){
  if (g) plan.grades[id] = g; else delete plan.grades[id];
  savePlan();
}
function passesOf(id){ return plan.passes[id] || {}; }
function togglePass(id, which, on){
  var p = plan.passes[id] || (plan.passes[id] = {});
  if (on) p[which] = true; else delete p[which];
  if (!Object.keys(p).length) delete plan.passes[id];
  savePlan();
}
function passCount(id){
  var p = passesOf(id), n = 0;
  ["p1","p2","p3"].forEach(function(k){ if (p[k]) n++; });
  return n;
}

/* ---------------- the ledger ---------------- */
function ledger(subj){
  var list = chapters(subj), total = SUBJ[subj].total;
  var secured = 0;
  list.forEach(function(c){ secured += c.stake * gradeShare(gradeOf(c.id)); });
  var target = total * plan.target / 100;
  return {
    subject: subj,
    total: total,
    secured: secured,
    risk: Math.max(total - secured, 0),
    target: target,
    gap: Math.max(target - secured, 0),
    graded: list.filter(function(c){ return gradeOf(c.id) > 0; }).length,
    chapters: list.length
  };
}
function bothLedgers(){
  var a = ledger("maths"), b = ledger("physics");
  return {
    total: a.total + b.total,
    secured: a.secured + b.secured,
    target: a.target + b.target,
    gap: a.gap + b.gap
  };
}

/* ---------------- the queue ----------------
   Ranked by marks recoverable, weighted by how reliably the board asks the
   chapter. Then cut where the running total closes the gap — so the answer to
   "what do I do next" is a short list, not all 27 chapters.
   ---------------------------------------------------------------------------- */
function queue(subj){
  var out = chapters(subj)
    .map(function(c){
      var g = gradeOf(c.id);
      var recoverable = c.stake * (1 - gradeShare(g));
      return { c:c, grade:g, recoverable:recoverable,
               weight:recoverable * (PRIO_WEIGHT[c.prio] || 0.7) };
    })
    .filter(function(x){ return x.recoverable > 0.05; })
    .sort(function(a,b){
      return b.weight - a.weight || a.c.prio - b.c.prio || a.c.num - b.c.num;
    });

  var gap = ledger(subj).gap, running = 0;
  out.forEach(function(x){
    x.running = (running += x.recoverable);
    x.closesGap = gap > 0 && x.running >= gap;
  });
  var cut = -1;
  for (var i = 0; i < out.length; i++){
    if (out[i].closesGap){ cut = i; break; }
  }
  return { items: out, cut: cut, gap: gap };
}

/* ---------------- the schedule ----------------
   A plan, not a prediction. Days to the exam are divided between the chapters
   in the queue with a fifth held back for revision, because a plan with no
   slack is a plan that breaks on the first bad week.
   ---------------------------------------------------------------------------- */
var MS_DAY = 86400000;
function daysToExam(){
  if (!plan.exam) return null;
  var when = Date.parse(plan.exam + "T00:00:00");
  if (isNaN(when)) return null;
  var today = new Date();
  today = Date.parse(today.getFullYear() + "-" +
    String(today.getMonth() + 1).padStart(2, "0") + "-" +
    String(today.getDate()).padStart(2, "0") + "T00:00:00");
  return Math.round((when - today) / MS_DAY);
}
function schedule(items, days){
  if (!items.length || !days || days < 1) return [];
  var usable = Math.max(Math.floor(days * 0.8), 1);      // a fifth for revision
  var per = usable / items.length;
  var out = [], cursor = 0;
  items.forEach(function(x, i){
    var from = Math.floor(cursor), to = Math.floor(cursor + per) - 1;
    if (to < from) to = from;
    if (i === items.length - 1) to = usable - 1;
    out.push({ item:x, from:from, to:to, days:Math.max(to - from + 1, 1) });
    cursor += per;
  });
  return out;
}
function dateAfter(offset){
  var d = new Date(Date.now() + offset * MS_DAY);
  return d.toLocaleDateString(LANG === "hi" ? "hi-IN" : "en-IN",
    { day:"numeric", month:"short" });
}
function marks(n){
  // Marks read as marks: one decimal, and never a bare ".0"
  var r = Math.round(n * 10) / 10;
  return (r === Math.round(r) ? String(Math.round(r)) : r.toFixed(1));
}

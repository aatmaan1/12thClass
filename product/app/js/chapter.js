/* ================= the chapter, the shelf, the pack, search =================
   One scrolling page per chapter rather than six tabs, in the order the marks
   are in: what the examiner pays for, then the questions, then the self-test,
   then the recall box, then the detail, then the scope. The old order started
   with the syllabus and finished with the marking scheme, which is the order
   a textbook is written in, not the order marks are won in.
   ================================================================================ */

//: id, string key, where the text comes from, and what a locked one says.
var SECTIONS = [
  { id:"start",  key:"start",  field:"intro",   lock:null },
  { id:"pays",   key:"pays",   field:"s.tips",  lock:"pays" },
  { id:"qs",     key:"qs",     field:"s.pyq",   lock:"qs" },
  { id:"test",   key:"test",   field:"s.test",  lock:"test" },
  { id:"recall", key:"recall", field:"recall",  lock:"recall" },
  { id:"detail", key:"detail", field:"s.brief", lock:"detail" },
  { id:"scope",  key:"scope",  field:"s.scope", lock:null }
];

function fieldOf(c, path){ return tr(c, path).text; }

function chapterView(c){
  var g = gradeOf(c.id);
  var h = '<button class="back noprint" data-home>&larr; ' + T("ch.back") + "</button>" +
    '<p class="crumb"><b>' + subjLabel(c.subj) + "</b> · " + T("ch.chapter") + " " +
      c.num + " · " + esc(unitName(c.unit)) + "</p>" +
    '<h1 class="pt">' + esc(chTitle(c)) + "</h1>" +
    '<div class="tags">' +
      (!c.lock && anyLocked() ? '<span class="tag free">' + T("lock.free") + "</span>" : "") +
      '<span class="tag ' + (g === 3 ? "ok" : "risk") + '">' +
        T("ch.stake", {n:marks(c.stake)}) + "</span>" +
      '<span class="tag">' + T("ch.prio", {n:c.prio}) + "</span>" +
      (c.appearShort ? '<span class="tag wrap">' + esc(c.appearShort) + "</span>" : "") +
    "</div>";

  /* grading, where the studying happens rather than back on the plan */
  h += '<div class="card noprint" style="margin-top:20px;display:flex;gap:14px;' +
    'align-items:center;flex-wrap:wrap;justify-content:space-between">' +
    '<span style="font:500 13.5px/1.4 var(--sans);color:var(--ink)">' +
      T("ch.gradeQ") + "</span>" +
    '<span class="grade" role="group" aria-label="' + esc(chTitle(c)) + '">';
  GRADES.forEach(function(n){
    h += '<button data-grade="' + c.id + ":" + n + '" data-g="' + n +
      '" aria-pressed="' + (g === n) + '">' + T("plan.g" + n) + "</button>";
  });
  h += "</span></div>";

  if (c.deleted){
    h += '<div class="warn"><p class="warn-h">' + T("ch.deleted") + "</p>" +
      '<div class="md">' + md(c.deleted) + "</div></div>";
  }

  /* the in-chapter nav: only sections that exist or are gated */
  var live = SECTIONS.filter(function(s){
    return fieldOf(c, s.field) || (s.lock && isLocked(c, s.field));
  });
  h += '<nav class="jump noprint">';
  live.forEach(function(s, i){
    h += '<a href="#s-' + s.id + '"' + (i === 0 ? ' aria-current="true"' : "") + ">" +
      T("sec." + s.key) + (s.lock && isLocked(c, s.field) ? lockSvg(11) : "") + "</a>";
  });
  h += "</nav>";

  live.forEach(function(s){
    h += '<section class="sect" id="s-' + s.id + '"><h2>' + T("sec." + s.key) + "</h2>" +
      '<p class="why">' + T("sec." + s.key + "Why") + "</p>" +
      sectionBody(c, s) + "</section>";
  });

  h += passBlock(c);
  return h;
}

function sectionBody(c, s){
  if (s.lock && isLocked(c, s.field)) return gate(s.lock);
  var got = tr(c, s.field);

  if (s.id === "start") return notrans(got.translated) + '<div class="md">' + md(got.text) + "</div>";
  if (s.id === "qs") return notrans(qaSource(c).translated) + questions(c);
  if (s.id === "test") return selfTest(c);
  return notrans(got.translated) + '<div class="md">' + md(got.text) + "</div>";
}

function questions(c){
  if (!c.qs.length) return "";
  var h = '<div class="qlist">';
  c.qs.forEach(function(q){
    var k = c.id + "-" + q.n;
    h += '<article class="qq"><div class="qq-h"><span class="qq-n">Q' + q.n + "</span>" +
      (q.marks ? '<span class="qq-m">' + esc(q.marks) + "</span>" : "") + "</div>" +
      '<div class="qq-b"><div class="md">' + md(q.body) + "</div></div>" +
      '<div class="qq-f noprint"><button class="reveal" data-sol="' + k +
        '" aria-expanded="false" aria-controls="sol-' + k + '">' + T("qs.show") + "</button></div>" +
      '<div class="sol" id="sol-' + k + '" hidden><p class="sol-l">' + T("qs.sol") + "</p>" +
      '<div class="md">' + md(q.sol) + "</div></div></article>";
  });
  return h + "</div>";
}

function selfTest(c){
  var got = tr(c, "s.test");
  var cut = got.text.split(/\n### (?:Answer key|उत्तर कुंजी)\s*\n/);
  var score = plan.scores[c.id];
  return notrans(got.translated) + '<div class="md">' + md(cut[0]) + "</div>" +
    '<div class="card noprint" style="margin-top:18px;display:flex;gap:13px;' +
      'align-items:center;flex-wrap:wrap">' +
      '<p style="margin:0;flex:1;min-width:180px;font-size:13.5px"><strong style="color:var(--ink)">' +
        T("test.hidden") + "</strong> " + T("test.hiddenWhy") + "</p>" +
      '<button class="reveal" data-sol="key-' + c.id + '" aria-expanded="false" ' +
        'aria-controls="key-' + c.id + '">' + T("test.reveal") + "</button></div>" +
    '<div id="key-' + c.id + '" hidden><div class="md"><h3>' + T("test.key") + "</h3>" +
      md(cut[1] || "") + "</div></div>" +
    '<div class="card noprint" style="margin-top:14px;display:flex;gap:11px;' +
      'align-items:center;flex-wrap:wrap">' +
      '<label for="score-' + c.id + '" style="font:500 13px/1 var(--sans);color:var(--ink)">' +
        T("test.score") + "</label>" +
      '<input id="score-' + c.id + '" type="text" inputmode="numeric" placeholder="—" ' +
        'value="' + (score == null ? "" : esc(String(score))) + '" data-score="' + c.id +
        '" style="width:76px;font:400 14px/1 var(--mono);padding:9px 10px;border-radius:7px;' +
        'border:1px solid var(--line);background:var(--paper);color:var(--ink)">' +
      '<span style="font-size:12.5px;color:var(--muted)">' + T("test.scoreNote") + "</span></div>";
}

function passBlock(c){
  var p = passesOf(c.id);
  var h = '<section class="block noprint"><div class="block-h"><h2 class="sec">' +
    T("pass.h") + '</h2><p>' + T("pass.why") + "</p></div>" +
    '<div class="shelf">';
  ["p1","p2","p3"].forEach(function(k){
    h += '<label class="dcard" style="cursor:pointer">' +
      '<b style="justify-content:flex-start;gap:9px"><input type="checkbox" data-pass="' +
        c.id + ":" + k + '"' + (p[k] ? " checked" : "") +
        ' style="width:16px;height:16px;accent-color:var(--secured)">' +
        T("pass." + k) + "</b>" +
      "<span>" + T("pass." + k + "d") + "</span></label>";
  });
  return h + "</div></section>";
}

/* ---------------- the reference shelf ---------------- */
function libView(){
  return '<button class="back noprint" data-home>&larr; ' + T("ch.back") + "</button>" +
    '<p class="eyebrow">' + T("lib.eyebrow") + "</p>" +
    '<h1 class="pt">' + T("lib.h") + "</h1>" +
    '<p class="lede">' + T("lib.lede") + "</p>" +
    '<div style="margin-top:28px">' + shelf() + "</div>";
}

function docView(d){
  var body = isLocked(d, "body")
    ? '<div style="margin-top:26px">' + gate("doc") + "</div>"
    : (function(){
        var t = ((d.tr || {})[LANG] || {}).body;
        return notrans(LANG === "en" || !!t) +
          '<div class="md" style="margin-top:26px">' + md(t || d.body || "") + "</div>";
      })();
  return '<button class="back noprint" data-home>&larr; ' + T("ch.back") + "</button>" +
    '<p class="eyebrow">' + T("doc.eyebrow") + "</p>" +
    '<h1 class="pt">' + esc(docTitle(d)) + "</h1>" +
    '<p class="lede">' + esc(docBlurb(d)) + "</p>" + body;
}

/* ---------------- the print pack ---------------- */
function packView(){
  var pack = (PACKS["packs.revision"] || {}).pack;
  if (!pack){
    return '<button class="back noprint" data-home>&larr; ' + T("ch.back") + "</button>" +
      '<p class="eyebrow">' + T("pack.eyebrow") + "</p>" +
      '<h1 class="pt">' + T("pack.h") + "</h1>" +
      '<div style="margin-top:22px">' + gate("doc", "bump") + "</div>";
  }
  var h = '<button class="back noprint" data-home>&larr; ' + T("ch.back") + "</button>" +
    '<p class="eyebrow noprint">' + T("pack.eyebrow") + "</p>" +
    '<h1 class="pt noprint">' + T("pack.h") + "</h1>" +
    '<p class="lede noprint">' + esc(pack.note || "") + "</p>" +
    '<p class="noprint" style="margin-top:16px"><button class="buy" data-print>' +
      T("pack.print") + '</button></p><div style="margin-top:26px">';
  (pack.sheets || []).forEach(function(x){
    h += '<section class="sheet"><div class="sheet-h"><b>' + esc(x.title) + "</b>" +
      "<span>" + subjLabel(x.subj) + " · " + T("ch.chapter") + " " + x.num +
      (x.appear ? " · " + esc(x.appear) : "") + "</span></div>" +
      (x.deleted ? '<div class="warn"><p class="warn-h">' + T("ch.deleted") + "</p>" +
        '<div class="md">' + md(x.deleted) + "</div></div>" : "") +
      '<div class="md">' + md(x.recall) + "</div></section>";
  });
  return h + "</div>";
}

/* ---------------- search ---------------- */
function searchView(term){
  var t = term.toLowerCase(), hits = [];
  function push(title, where, text, act){
    if (!text) return;
    var i = String(text).toLowerCase().indexOf(t);
    if (i < 0) return;
    var a = Math.max(0, i - 70), b = Math.min(text.length, i + term.length + 110);
    var frag = (a ? "…" : "") + text.slice(a, i) + C1 +
      text.slice(i, i + term.length) + C2 + text.slice(i + term.length, b) +
      (b < text.length ? "…" : "");
    hits.push({ title:title, where:where, act:act,
      frag: esc(frag.replace(/\s+/g," "))
        .split(C1).join("<mark>").split(C2).join("</mark>") });
  }
  CH.forEach(function(c){
    // Only what is actually here. A search that matched paid text would be
    // leaking the thing the gate exists to hold back.
    SECTIONS.forEach(function(s){
      push(chTitle(c), subjLabel(c.subj) + " · " + T("ch.chapter") + " " + c.num +
        " · " + T("sec." + s.key), fieldOf(c, s.field),
        JSON.stringify({ k:"ch", id:c.id, sec:s.id }));
    });
    push(chTitle(c), subjLabel(c.subj) + " · " + T("ch.chapter") + " " + c.num,
      chIntro(c), JSON.stringify({ k:"ch", id:c.id }));
  });
  DATA.docs.forEach(function(d){
    push(docTitle(d), T("doc.eyebrow"), d.body, JSON.stringify({ k:"doc", id:d.id }));
  });

  var h = '<button class="back noprint" data-home>&larr; ' + T("ch.back") + "</button>" +
    '<p class="eyebrow">' + T("find.eyebrow") + "</p>" +
    '<h1 class="pt">' + T(hits.length === 1 ? "find.n1" : "find.n", {n:hits.length}) + "</h1>" +
    '<p class="lede">' + T("find.for", {q:esc(term)}) + "</p>" +
    (anyLocked()
      ? '<p class="small" style="margin-top:10px;max-width:68ch">' +
        T("find.locked", {n:CH.length, d:DATA.docs.length}) + "</p>"
      : "");
  if (!hits.length) return h + '<p class="lede">' + T("find.none") + "</p>";

  h += '<div class="hits" style="margin-top:24px">';
  hits.slice(0, 60).forEach(function(x){
    h += "<button class=\"hit\" data-go='" + x.act + "'><b>" + esc(x.title) + "</b>" +
      "<span>" + x.frag + "</span><em>" + x.where + "</em></button>";
  });
  h += "</div>";
  if (hits.length > 60) h += '<p class="small" style="margin-top:14px">' + T("find.first60") + "</p>";
  return h;
}

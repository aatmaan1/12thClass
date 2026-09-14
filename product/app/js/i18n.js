/* ================= language =================
   English is the default and lives here; every other language overrides by key
   from DATA.langs. A key with no translation falls back to English rather than
   disappearing, and the app says so wherever a whole section is English only.
   ================================================================================ */

var EN = {
  "lang.name":"English", "lang.short":"EN",
  "lang.notTranslated":"This part is not translated yet — the English text is below.",
  "brand.sub":"CBSE 2025-26 · 041 · 042",
  "subj.maths":"Mathematics", "subj.physics":"Physics",
  "search.ph":"Search", "btn.theme":"Theme", "btn.access":"Access",

  /* ---- the ledger ---- */
  "led.title":"Marks ledger",
  "led.inHand":"In hand", "led.atRisk":"Still at risk",
  "led.target":"Your target", "led.gap":"Short by",
  "led.of":"of {n}",
  "led.examLabel":"Exam date",
  "led.targetLabel":"Target %",
  "led.graded":"{done} of {all} chapters graded",
  "led.gradeMore":"Grade the rest and the plan sharpens",
  "led.onTarget":"On target. Hold it with the third pass.",
  "led.method":"A chapter's marks are its unit's marks split between the chapters in that unit. An even split, because the board does not publish a finer one.",
  "led.both":"Both papers: {n} of {t}",

  /* ---- the planner ---- */
  "plan.eyebrow":"The plan",
  "plan.h":"You are short by {gap} marks in {subject}",
  "plan.hOk":"You are on target in {subject}",
  "plan.hEmpty":"Grade what you know, and the plan writes itself",
  "plan.lede":"Grade each chapter 0-3. The page works out how many marks you are missing and which chapters hold them — then puts them in the order worth studying.",
  "plan.ledeOk":"Every chapter graded at your target or above. What is left is holding it: the third pass on the chapters you have only read once.",
  "plan.queueH":"Study these next",
  "plan.queueWhy":"Ranked by marks recoverable, weighted by how reliably the board asks it",
  "plan.cut":"These {n} chapters carry the {gap} marks you are short.",
  "plan.cutAll":"Every chapter left is in the queue — the gap is larger than what is recoverable.",
  "plan.recover":"recoverable",
  "plan.schedH":"A schedule",
  "plan.schedWhy":"{days} days to the exam, a fifth of them held back for revision",
  "plan.schedNoDate":"Set an exam date in the ledger and this becomes dates.",
  "plan.schedCol1":"When", "plan.schedCol2":"Chapter", "plan.schedCol3":"Passes",
  "plan.passes":"Learn · Apply · Test",
  "plan.rateH":"Grade the chapters",
  "plan.rateWhy":"One tap each. Nothing is sent anywhere — it is saved on this device.",
  "plan.g0":"new", "plan.g1":"shaky", "plan.g2":"ok", "plan.g3":"solid",
  "plan.atStake":"at stake",
  "plan.libH":"Read before you start",
  "plan.libWhy":"The exam before the syllabus",
  "plan.caveatH":"Two things this carries from the notes.",
  "plan.caveat1":"The frequency bands (“every year”, “8–9/10”) are well-informed pattern estimates, not a machine count of past papers. Two scope points are flagged rather than asserted: polarisation in Wave Optics, and the magnetic-materials block in Physics chapter 5.",
  "plan.caveat2":"CBSE republishes the syllabus and one sample paper per subject each year. Check the deletion lists against the current PDF at cbseacademic.nic.in at the start of the session. Notes go stale; the board circular does not.",
  "plan.notAff":"Not affiliated with CBSE.",

  /* ---- the chapter ---- */
  "ch.back":"The plan",
  "ch.chapter":"Chapter",
  "ch.stake":"{n} marks at stake",
  "ch.prio":"Priority P{n}",
  "ch.gradeQ":"How solid are you?",
  "ch.deleted":"Deleted — do not study this",
  "sec.start":"Start here", "sec.startWhy":"Plain English, no prior knowledge assumed",
  "sec.pays":"What the examiner pays for",
  "sec.paysWhy":"The marking-scheme traps for this chapter, question type by question type",
  "sec.qs":"Board questions",
  "sec.qsWhy":"Attempt each on paper first — the solution stays hidden until you ask",
  "sec.test":"Self-test", "sec.testWhy":"Under time, then score it honestly",
  "sec.recall":"Quick recall", "sec.recallWhy":"For the third pass, and the night before",
  "sec.detail":"The full detail", "sec.detailWhy":"Every statement, formula and table, in exam language",
  "sec.scope":"Scope", "sec.scopeWhy":"Exactly what is in the syllabus, and what has been cut",
  "qs.show":"Show solution", "qs.hide":"Hide solution", "qs.sol":"Solution",
  "test.hidden":"The answer key is hidden.",
  "test.hiddenWhy":"Finish the set under time first — a key you have glanced at turns this into a reading exercise.",
  "test.reveal":"Reveal answer key", "test.hideKey":"Hide answer key", "test.key":"Answer key",
  "test.score":"Score for this set",
  "test.scoreNote":"% · below 70 means another Learn pass on what you dropped",
  "pass.h":"Three passes",
  "pass.why":"Read it, work it, test it. The method from the study plan, one chapter at a time.",
  "pass.p1":"Learn", "pass.p1d":"Read Start here, then reproduce the recall box from memory.",
  "pass.p2":"Apply", "pass.p2d":"Work the board questions with the solutions hidden.",
  "pass.p3":"Test", "pass.p3d":"Do the self-test under time, then score it.",

  /* ---- the library and search ---- */
  "lib.eyebrow":"Reference", "lib.h":"The reference shelf",
  "lib.lede":"Nine documents that sit behind the chapters: the paper design, what repeats, the formula sheets and the derivations.",
  "doc.eyebrow":"Reference",
  "find.eyebrow":"Search", "find.n1":"{n} result", "find.n":"{n} results",
  "find.for":"for “{q}”",
  "find.none":"Nothing matched. Try a formula name, a chapter title, or a term like “Bayes”, “drift velocity” or “minimum deviation”.",
  "find.locked":"Searching the free chapters only. Unlock the guide to search all {n} chapters and {d} reference documents.",
  "find.first60":"Showing the first 60. Narrow the term for fewer.",

  /* ---- the gate ---- */
  "lock.badge":"Locked", "lock.free":"Free chapter",
  "lock.h":"This part is in the full guide",
  "lock.pays":"The marking-scheme traps for this chapter — what the examiner pays for, question type by question type.",
  "lock.qs":"The board questions for this chapter, each with the full working an examiner expects.",
  "lock.sol":"Every solution for this chapter in one place.",
  "lock.test":"The self-test for this chapter, and its answer key.",
  "lock.recall":"The quick-recall box: this chapter compressed to what you must be able to reproduce.",
  "lock.detail":"The exam-language detail for this chapter: every statement, formula and table.",
  "lock.doc":"This reference document.",
  "lock.reading":"The plan above is free and always will be, for all {n} chapters — along with the syllabus scope, the deleted topics and the plain-English opening to each. What is behind this is the material that closes the gap it just showed you, plus {s} chapters you can read in full first.",
  "lock.cta":"Unlock everything — {p}",
  "lock.have":"I have a key",
  "pack.eyebrow":"The print pack", "pack.h":"One page per chapter",
  "pack.print":"Print / save as PDF",

  /* ---- access ---- */
  "acct.free":"Free plan", "acct.full":"Full access",
  "unlock.h":"Unlock the full guide",
  "unlock.have":"Paste the key from your receipt.",
  "unlock.ph":"MF1-XXXXX-XXXXX-XXXXX", "unlock.go":"Unlock", "unlock.busy":"Checking…",
  "unlock.ok":"Unlocked. Everything is on this device now, and it works offline.",
  "unlock.badkey":"That key was not accepted. Check it was copied whole, or write to {e}.",
  "unlock.offline":"Could not reach the server. Check the connection and try again — nothing is lost.",
  "unlock.buy":"See what is inside", "unlock.close":"Close",
  "unlock.status":"Full access on this device. {u} of {s} device(s) in use.",
  "unlock.keyIs":"Your key", "unlock.forget":"Remove from this device",
  "unlock.forgetNote":"This only clears the copy stored in this browser. It does not free the device slot — write to {e} to move one.",
  "unlock.claiming":"Finding your purchase…",
  "unlock.claimFail":"We could not find that purchase yet. Payments can take a minute to arrive — try again, or write to {e} with your receipt.",
  "unlock.support":"Lost your key? Write to {e} with the email you paid with."
};

var LANG = "en";
var LANGS = ["en"].concat(Object.keys(DATA.langs || {}));
function L(){ return (DATA.langs || {})[LANG] || null; }
function T(k, vars){
  var t = L() && L().ui[k];
  if (t == null) t = EN[k];
  if (t == null) return k;
  if (vars) Object.keys(vars).forEach(function(v){ t = t.split("{" + v + "}").join(vars[v]); });
  return t;
}
// chapter, unit and document names are translated as data, not as UI strings
function chTitle(c){ return (L() && L().titles[c.id]) || c.title; }
function unitName(u){ return (L() && L().units[u]) || u; }
function docTitle(d){ return (L() && L().docs[d.id] && L().docs[d.id][0]) || d.title; }
function docBlurb(d){ return (L() && L().docs[d.id] && L().docs[d.id][1]) || d.blurb; }
function chIntro(c){ return tr(c, "intro").text; }
function subjLabel(s){ return T(SUBJ[s].k); }

/* ---------------- one chapter field, in the reader's language ----------------
   Where a translation lives depends on what it costs. The free sections sit in
   the language pack, which ships whole; the sold ones sit on the chapter, so a
   locked chapter withholds its Hindi exactly as it withholds its English.
   Both are read through here, so a caller never has to know which is which.
   -------------------------------------------------------------------------- */
var TR_PACK = { intro:"intros", "s.scope":"scopes", deleted:"deleteds",
                appear:"appears" };
var TR_CHAP = { "s.tips":"tips", "s.test":"test", recall:"recall",
                "s.brief":"brief", "s.pyq":"pyq", "s.sol":"sol" };

function english(c, path){
  return (path.indexOf("s.") === 0 ? (c.s || {})[path.slice(2)] : c[path]) || "";
}
function tr(c, path){
  var en = english(c, path);
  if (LANG === "en") return { text:en, translated:true };
  var t = null;
  if (TR_PACK[path]) t = L() && (L()[TR_PACK[path]] || {})[c.id];
  else if (TR_CHAP[path]) t = ((c.tr || {})[LANG] || {})[TR_CHAP[path]];
  return t ? { text:t, translated:true } : { text:en, translated:false };
}
function notrans(on){
  // Silent in English, and silent wherever the section really is translated.
  if (LANG === "en" || on === true) return "";
  return '<p class="notrans"><span>' + T("lang.notTranslated") + "</span></p>";
}

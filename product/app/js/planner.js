/* ================= the ledger and the planner =================
   The margin totals marks the way an examiner totals a script, and the plan
   is what falls out of those totals: the gap, the chapters that hold it, and
   how many days there are to close it.
   ================================================================================ */

function lockSvg(n){
  n = n || 12;
  return '<svg class="lk" width="' + n + '" height="' + n + '" viewBox="0 0 16 16" ' +
    'aria-hidden="true"><path d="M4.4 7.2V5a3.6 3.6 0 0 1 7.2 0v2.2M3.4 7.2h9.2v7H3.4z" ' +
    'fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"></path></svg>';
}

/* ---------------- the margin ---------------- */
function drawLedger(){
  var l = ledger(subject), both = bothLedgers();
  var securedPc = l.total ? (100 * l.secured / l.total) : 0;
  var targetPc = l.total ? (100 * l.target / l.total) : 0;
  var days = daysToExam();

  var h = '<p class="led-k">' + T("led.title") + " · " + subjLabel(subject) + "</p>" +
    '<div class="led-row big secured"><span>' + T("led.inHand") + "</span>" +
      "<b>" + marks(l.secured) + "</b></div>" +
    '<div class="led-bar" aria-hidden="true"><i class="s" style="width:' +
      securedPc.toFixed(1) + '%"></i><i class="r" style="width:' +
      Math.max(targetPc - securedPc, 0).toFixed(1) + '%"></i></div>' +
    '<p class="led-note">' + T("led.of", {n:l.total}) + " · " +
      T("led.both", {n:marks(both.secured), t:both.total}) + "</p>" +
    '<div class="led-row"><span>' + T("led.target") + "</span><b>" + marks(l.target) + "</b></div>" +
    '<div class="led-row ' + (l.gap > 0.05 ? "risk" : "secured") + '"><span>' +
      (l.gap > 0.05 ? T("led.gap") : T("led.atRisk")) + "</span><b>" +
      marks(l.gap > 0.05 ? l.gap : l.risk) + "</b></div>" +

    '<div class="led-field"><label for="examIn">' + T("led.examLabel") + "</label>" +
      '<input id="examIn" type="date" value="' + esc(plan.exam) + '"></div>' +
    '<div class="led-field"><label for="targetIn">' + T("led.targetLabel") + "</label>" +
      '<input id="targetIn" type="number" min="40" max="100" step="1" value="' +
      plan.target + '"></div>' +
    '<p class="led-note">' +
      (l.graded < l.chapters
        ? T("led.graded", {done:l.graded, all:l.chapters}) + ". " + T("led.gradeMore")
        : (l.gap > 0.05 ? T("led.method") : T("led.onTarget"))) +
      (days != null && days > 0 ? " · " + days + " days" : "") + "</p>";

  if (anyLocked()){
    var url = checkoutUrl("core");
    h += '<a class="led-cta noprint" href="' + esc(url || "#") + '" data-buy>' +
      T("lock.cta", {p:price("core")}) + "</a>";
  }
  var el = document.getElementById("ledger");
  el.innerHTML = h;

  var exam = el.querySelector("#examIn");
  exam.onchange = function(){ plan.exam = exam.value; savePlan(); render(); };
  var target = el.querySelector("#targetIn");
  target.onchange = function(){
    var v = parseInt(target.value, 10);
    plan.target = isNaN(v) ? 85 : Math.min(100, Math.max(40, v));
    target.value = plan.target;
    savePlan(); render();
  };
  el.querySelectorAll("a[data-buy]").forEach(function(a){
    a.onclick = function(){ a.href = withNonce(a.href); };
  });
}

/* ---------------- the plan ---------------- */
function planView(){
  var l = ledger(subject), qd = queue(subject), days = daysToExam();
  var ranked = qd.cut >= 0 ? qd.items.slice(0, qd.cut + 1) : qd.items;

  var head;
  if (!l.graded){
    head = '<h1 class="pt">' + T("plan.hEmpty") + "</h1>" +
      '<p class="lede">' + T("plan.lede") + "</p>";
  } else if (l.gap > 0.05){
    head = '<h1 class="pt">' + T("plan.h",
        {gap:marks(l.gap), subject:subjLabel(subject)}) + "</h1>" +
      '<p class="lede">' + T("plan.lede") + "</p>";
  } else {
    head = '<h1 class="pt">' + T("plan.hOk", {subject:subjLabel(subject)}) + "</h1>" +
      '<p class="lede">' + T("plan.ledeOk") + "</p>";
  }
  var h = '<p class="eyebrow">' + T("plan.eyebrow") + " · " + subjLabel(subject) +
    " · " + SUBJ[subject].code + "</p>" + head;

  /* the queue */
  if (ranked.length){
    h += '<section class="block"><div class="block-h"><h2 class="sec">' +
      T("plan.queueH") + '</h2><p>' + T("plan.queueWhy") + "</p></div>" +
      '<div class="queue">';
    ranked.forEach(function(x, i){
      var c = x.c;
      h += '<button class="qi" data-ch="' + c.id + '">' +
        '<span class="qi-n">' + (i + 1) + "</span>" +
        '<span class="qi-t"><b>' + esc(chTitle(c)) + (c.lock ? "" : "") + "</b>" +
          "<span>" + T("ch.chapter") + " " + c.num + " · " + esc(unitName(c.unit)) +
          " · P" + c.prio +
          "</span></span>" +
        '<span class="qi-m"><b>' + marks(x.recoverable) + "</b>" +
          "<span>" + T("plan.recover") + "</span></span>" +
        "</button>";
    });
    if (qd.gap > 0.05){
      h += '<p class="cut">' + (qd.cut >= 0
        ? T("plan.cut", {n:ranked.length, gap:marks(qd.gap)})
        : T("plan.cutAll")) + "</p>";
    }
    h += "</div></section>";
  }

  /* the schedule */
  if (ranked.length){
    h += '<section class="block"><div class="block-h"><h2 class="sec">' +
      T("plan.schedH") + '</h2><p>' + (days != null && days > 0
        ? T("plan.schedWhy", {days:days}) : T("plan.schedNoDate")) + "</p></div>";
    if (days != null && days > 0){
      var rows = schedule(ranked, days);
      h += '<div class="tablewrap" style="max-width:none"><table class="sched"><thead><tr><th>' +
        T("plan.schedCol1") + "</th><th>" + T("plan.schedCol2") + "</th><th>" +
        T("plan.schedCol3") + "</th></tr></thead><tbody>";
      rows.forEach(function(r){
        h += '<tr><td class="d">' + dateAfter(r.from) +
          (r.to > r.from ? " – " + dateAfter(r.to) : "") + "</td>" +
          '<td class="c">' + esc(chTitle(r.item.c)) + "</td>" +
          '<td class="p">' + T("plan.passes") + "</td></tr>";
      });
      h += "</tbody></table></div>";
    }
    h += "</section>";
  }

  /* the grading pass */
  h += '<section class="block"><div class="block-h"><h2 class="sec">' +
    T("plan.rateH") + '</h2><p>' + T("plan.rateWhy") + "</p></div>" + '<div class="rate">';
  var unit = null;
  chapters(subject).forEach(function(c){
    if (c.unit !== unit){
      unit = c.unit;
      h += '<div class="rate-u"><span>' + esc(unitName(unit)) + "</span><i>" +
        c.unitMarks + " marks</i></div>";
    }
    var g = gradeOf(c.id);
    h += '<div class="rr"><span class="rr-n">' + c.num + "</span>" +
      '<span class="rr-t"><button data-ch="' + c.id + '">' + esc(chTitle(c)) +
        (c.lock ? " " + lockSvg(10) : "") + "</button>" +
        "<em>" + (c.appearShort ? esc(c.appearShort) : esc(unitName(c.unit))) + "</em></span>" +
      '<span class="rr-m">' + marks(c.stake) + ' <u>' + T("plan.atStake") + "</u></span>" +
      '<span class="grade" role="group" aria-label="' + esc(chTitle(c)) + '">';
    GRADES.forEach(function(n){
      h += '<button data-grade="' + c.id + ":" + n + '" data-g="' + n +
        '" aria-pressed="' + (g === n) + '">' + T("plan.g" + n) + "</button>";
    });
    h += "</span></div>";
  });
  h += "</div></section>";

  /* the shelf */
  h += '<section class="block"><div class="block-h"><h2 class="sec">' +
    T("plan.libH") + '</h2><p>' + T("plan.libWhy") + "</p></div>" +
    shelf() + "</section>";

  h += '<footer class="block"><p class="small" style="max-width:68ch"><strong>' +
    T("plan.caveatH") + "</strong> " + T("plan.caveat1") + "</p>" +
    '<p class="small" style="max-width:68ch">' + T("plan.caveat2") + " " +
    T("plan.notAff") + "</p></footer>";
  return h;
}

function shelf(){
  var h = '<div class="shelf">';
  DATA.docs.forEach(function(d){
    h += '<button class="dcard" data-doc="' + d.id + '"><b>' + esc(docTitle(d)) +
      (isLocked(d, "body") ? lockSvg(11) : "") + "</b><span>" + esc(docBlurb(d)) +
      "</span></button>";
  });
  if ((PACKS["packs.revision"] || {}).pack){
    h += '<button class="dcard" data-go=\'{"k":"pack"}\'><b>' + T("pack.eyebrow") +
      "</b><span>" + T("pack.h") + "</span></button>";
  }
  return h + "</div>";
}

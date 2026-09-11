/* ================= the shell: routes, wiring, boot ================= */

var subject = "maths";
var route = { k:"plan" };
var stage = document.getElementById("stage");

function render(){
  if (route.k === "ch" && byId[route.id]) stage.innerHTML = chapterView(byId[route.id]);
  else if (route.k === "doc"){
    var d = DATA.docs.filter(function(x){ return x.id === route.id; })[0];
    stage.innerHTML = d ? docView(d) : planView();
  }
  else if (route.k === "pack") stage.innerHTML = packView();
  else if (route.k === "lib") stage.innerHTML = libView();
  else if (route.k === "search") stage.innerHTML = searchView(route.term);
  else stage.innerHTML = planView();
  drawLedger();
  paintSubject();
  wire();
}

function hashOf(r){
  if (r.k === "ch")     return "#/ch/" + r.id + (r.sec ? "/" + r.sec : "");
  if (r.k === "doc")    return "#/doc/" + r.id;
  if (r.k === "pack")   return "#/pack";
  if (r.k === "lib")    return "#/library";
  if (r.k === "search") return "#/find/" + encodeURIComponent(r.term || "");
  return "#/" + subject;
}
function parseHash(){
  var p = (location.hash || "").replace(/^#\/?/, "").split("/");
  if (p[0] === "ch" && byId[p[1]])  return { k:"ch", id:p[1], sec:p[2] || "" };
  if (p[0] === "doc" && p[1])       return { k:"doc", id:decodeURIComponent(p[1]) };
  if (p[0] === "pack")              return { k:"pack" };
  if (p[0] === "library")           return { k:"lib" };
  if (p[0] === "find" && p[1])      return { k:"search", term:decodeURIComponent(p.slice(1).join("/")) };
  if (p[0] === "maths" || p[0] === "physics") subject = p[0];
  return { k:"plan" };
}
function apply(r, keepScroll){
  route = r;
  if (r.k === "ch" && byId[r.id]) subject = byId[r.id].subj;
  render();
  if (!keepScroll){
    if (r.k === "ch" && r.sec){
      var target = document.getElementById("s-" + r.sec);
      if (target){ target.scrollIntoView(); return; }
    }
    window.scrollTo(0, 0);
  }
}
function go(r, keepScroll){
  var h = hashOf(r);
  if (location.hash !== h){
    try {
      if (r.k === "search" && history.replaceState) history.replaceState(null, "", h);
      else location.hash = h;
    } catch(e){}
  }
  apply(r, keepScroll);
}
window.addEventListener("hashchange", function(){
  if (location.hash === hashOf(route)) return;     // our own write, already rendered
  apply(parseHash(), false);
});

/* ---------------- wiring the current view ---------------- */
function wire(){
  stage.querySelectorAll("[data-ch]").forEach(function(b){
    b.onclick = function(){ go({ k:"ch", id:b.dataset.ch }); };
  });
  stage.querySelectorAll("[data-doc]").forEach(function(b){
    b.onclick = function(){ go({ k:"doc", id:b.dataset.doc }); };
  });
  stage.querySelectorAll("[data-home]").forEach(function(b){
    b.onclick = function(){ go({ k:"plan" }); };
  });
  stage.querySelectorAll("[data-go]").forEach(function(b){
    b.onclick = function(){ go(JSON.parse(b.dataset.go)); };
  });
  stage.querySelectorAll("[data-unlock]").forEach(function(b){
    b.onclick = function(){ openAccess(); };
  });
  stage.querySelectorAll("[data-print]").forEach(function(b){
    b.onclick = function(){ window.print(); };
  });
  stage.querySelectorAll("a[data-buy]").forEach(function(a){
    // Tagged on click rather than on render, so the value is fresh and a
    // cached page cannot send a stale one.
    a.onclick = function(){ a.href = withNonce(a.href); };
  });

  /* grading: update in place, and keep the ledger honest */
  stage.querySelectorAll("[data-grade]").forEach(function(b){
    b.onclick = function(){
      var bits = b.dataset.grade.split(":");
      setGrade(bits[0], +bits[1]);
      if (route.k === "plan") render();
      else {
        b.closest(".grade").querySelectorAll("button").forEach(function(x){
          x.setAttribute("aria-pressed", String(x === b));
        });
        drawLedger();
      }
    };
  });

  /* solutions and answer keys */
  stage.querySelectorAll("[data-sol]").forEach(function(b){
    b.onclick = function(){
      var open = b.getAttribute("aria-expanded") === "true";
      b.setAttribute("aria-expanded", String(!open));
      var t = document.getElementById(b.getAttribute("aria-controls"));
      if (t) t.hidden = open;
      var isKey = b.dataset.sol.indexOf("key-") === 0;
      b.textContent = open ? T(isKey ? "test.reveal" : "qs.show")
                           : T(isKey ? "test.hideKey" : "qs.hide");
    };
  });
  stage.querySelectorAll("[data-pass]").forEach(function(cb){
    cb.onchange = function(){
      var bits = cb.dataset.pass.split(":");
      togglePass(bits[0], bits[1], cb.checked);
    };
  });
  stage.querySelectorAll("[data-score]").forEach(function(inp){
    inp.onchange = function(){
      var v = inp.value.replace(/[^0-9]/g, "");
      if (v === "") delete plan.scores[inp.dataset.score];
      else plan.scores[inp.dataset.score] = Math.min(100, +v);
      inp.value = plan.scores[inp.dataset.score] == null ? "" : plan.scores[inp.dataset.score];
      savePlan();
    };
  });

  /* the in-chapter nav follows the scroll */
  var links = stage.querySelectorAll(".jump a");
  if (links.length && "IntersectionObserver" in window){
    var sections = stage.querySelectorAll(".sect");
    var seen = new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if (!e.isIntersecting) return;
        links.forEach(function(a){
          a.setAttribute("aria-current", String(a.getAttribute("href") === "#" + e.target.id));
        });
      });
    }, { rootMargin: "-120px 0px -70% 0px" });
    sections.forEach(function(s){ seen.observe(s); });
  }
}

/* ---------------- the chrome ---------------- */
function paintSubject(){
  document.getElementById("tabM").setAttribute("aria-pressed", String(subject === "maths"));
  document.getElementById("tabP").setAttribute("aria-pressed", String(subject === "physics"));
}
function paintChrome(){
  document.getElementById("brandSub").textContent = T("brand.sub");
  document.getElementById("tabM").textContent = T("subj.maths");
  document.getElementById("tabP").textContent = T("subj.physics");
  var q = document.getElementById("q");
  q.setAttribute("placeholder", T("search.ph"));
  q.setAttribute("aria-label", T("search.ph"));
  document.getElementById("themeBtn").textContent = T("btn.theme");
  paintAccess();

  // each language names itself, so the switch never needs translating
  var sw = "";
  LANGS.forEach(function(l){
    var name = l === "en" ? EN["lang.short"] : (DATA.langs[l].ui["lang.short"] || l);
    sw += '<button data-lang="' + l + '" aria-pressed="' + (l === LANG) + '">' +
      esc(name) + "</button>";
  });
  var el = document.getElementById("langSw");
  el.innerHTML = sw;
  el.querySelectorAll("[data-lang]").forEach(function(b){
    b.onclick = function(){ setLang(b.dataset.lang); };
  });
}
function setLang(l){
  LANG = LANGS.indexOf(l) === -1 ? "en" : l;
  try { localStorage.setItem("mf.lang", LANG); } catch(e){}
  document.documentElement.setAttribute("lang", LANG);
  // the questions are language-dependent, so they are parsed again
  CH.forEach(requeue);
  paintChrome();
  render();
}

document.getElementById("tabM").onclick = function(){ subject = "maths";   go({ k:"plan" }); };
document.getElementById("tabP").onclick = function(){ subject = "physics"; go({ k:"plan" }); };
document.getElementById("brand").onclick = function(){ go({ k:"plan" }); };
document.getElementById("accessBtn").onclick = function(){ openAccess(); };
accessDlg.addEventListener("close", function(){ paintAccess(); });

var findTimer = null;
document.getElementById("q").oninput = function(e){
  var v = e.target.value.trim();
  clearTimeout(findTimer);
  findTimer = setTimeout(function(){
    if (v.length >= 2) go({ k:"search", term:v }, true);
    else if (route.k === "search") go({ k:"plan" }, true);
  }, 190);
};

document.getElementById("themeBtn").onclick = function(){
  var cur = document.documentElement.getAttribute("data-theme");
  var dark = cur ? cur === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
  document.documentElement.setAttribute("data-theme", dark ? "light" : "dark");
  try { localStorage.setItem("mf.theme", dark ? "light" : "dark"); } catch(e){}
};
try {
  var th = localStorage.getItem("mf.theme");
  if (th) document.documentElement.setAttribute("data-theme", th);
} catch(e){}

document.addEventListener("keydown", function(e){
  if (e.key === "/" && !/^(INPUT|TEXTAREA)$/.test(e.target.tagName)){
    e.preventDefault();
    document.getElementById("q").focus();
  }
  if (e.key === "Escape" && route.k !== "plan" &&
      !/^(INPUT|TEXTAREA)$/.test(e.target.tagName)) go({ k:"plan" });
});

/* ---------------- boot ---------------- */
try {
  var savedLang = localStorage.getItem("mf.lang");
  if (savedLang && LANGS.indexOf(savedLang) !== -1) LANG = savedLang;
} catch(e){}
document.documentElement.setAttribute("lang", LANG);

// Whatever was already bought is applied before the first paint, so a paid
// device opens straight into the full guide with no network and no flicker.
restoreAccess();
paintChrome();
apply(parseHash(), false);

// Then, in the background: pick up a purchase that has just completed, and
// re-check a cached licence in case it was refunded.
claimFromUrl();
refreshAccess();

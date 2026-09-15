/* ================= the paywall =================
   What ships in this file: the planner in full, the syllabus scope, the
   deleted-topics warning and the plain-English opening for all 27 chapters,
   plus two chapters and two reference documents whole. Nothing else is here in
   any form — a study app that shipped all 27 chapters and hid 25 behind a CSS
   class would be defeated by the first person to open view-source.

   The rest arrives from the unlock endpoint against a licence key and is
   cached afterwards, because the week before a board exam is exactly when a
   phone has no signal.

   The mechanics below are the ones already proved out: signed keys, seats
   counted per device, a cached unlock re-checked in the background so a refund
   can take access back. Only the presentation is new.
   ================================================================================ */

var PW = (typeof PAYWALL === "object" && PAYWALL) ? PAYWALL : {};
var ACCESS = { key:"", codes:"", seats:0, used:0, grants:{}, cache:{} };
var PACKS = {};
var K_GRANTS = "mf.grants", K_LIC = "mf.licence", K_INSTALL = "mf.install", K_NONCE = "mf.nonce";

function installId(){
  // Identifies this browser to the seat count, so unlocking twice here does
  // not spend a second device. Random and local; it says nothing about who is
  // using it.
  try {
    var v = localStorage.getItem(K_INSTALL);
    if (!v){
      v = "d" + Math.random().toString(36).slice(2, 10) + Date.now().toString(36);
      localStorage.setItem(K_INSTALL, v);
    }
    return v;
  } catch(e){ return "unstored"; }
}
function isLocked(item, path){
  return !!(item && item.lock && item.lock.indexOf(path) !== -1);
}
function anyLocked(){
  return CH.some(function(c){ return !!c.lock; }) ||
         DATA.docs.some(function(d){ return !!d.lock; });
}
function freeChapters(){
  return CH.filter(function(c){ return !c.lock; }).length;
}
function price(offer){ return (PW.prices || {})[offer || "core"] || ""; }
function checkoutUrl(offer){
  var urls = PW.checkout || {};
  return urls[offer || "core"] || PW.offerUrl || "";
}
function nonce(){
  // Generated here, before the browser leaves for the checkout, and carried
  // out through the provider's custom data. It is what lets the thank-you page
  // hand this browser its key without trusting a guessable order number.
  try {
    var v = localStorage.getItem(K_NONCE);
    if (!v){
      v = "n" + Math.random().toString(36).slice(2, 12) +
          Math.random().toString(36).slice(2, 12);
      localStorage.setItem(K_NONCE, v);
    }
    return v;
  } catch(e){ return ""; }
}
function withNonce(url){
  var param = PW.nonceParam, value = param ? nonce() : "";
  if (!param || !value || !url || url === "#") return url;
  try {
    var u = new URL(url, location.href);
    u.searchParams.set(param, value);
    return u.toString();
  } catch(e){ return url; }
}

/* ---------------- merging what was bought into the page ---------------- */
function deepMerge(target, patch, prefix, filled){
  Object.keys(patch).forEach(function(k){
    var path = prefix ? prefix + "." + k : k, v = patch[k];
    if (v && typeof v === "object" && !Array.isArray(v)){
      if (typeof target[k] !== "object" || !target[k]) target[k] = {};
      deepMerge(target[k], v, path, filled);
    } else {
      target[k] = v;
      filled.push(path);
    }
  });
}
function mergeItem(item, patch){
  var filled = [];
  deepMerge(item, patch, "", filled);
  if (item.lock){
    item.lock = item.lock.filter(function(p){ return filled.indexOf(p) === -1; });
    if (!item.lock.length) delete item.lock;
  }
}
function applyGrants(grants){
  if (!grants) return;
  Object.keys(grants).forEach(function(name){
    var payload = grants[name];
    ACCESS.grants[name] = true;
    if (name === "chapters"){
      Object.keys(payload || {}).forEach(function(id){
        if (!byId[id]) return;
        mergeItem(byId[id], payload[id]);
        requeue(byId[id]);
      });
    } else if (name === "docs"){
      Object.keys(payload || {}).forEach(function(id){
        var d = DATA.docs.filter(function(x){ return x.id === id; })[0];
        if (d) mergeItem(d, payload[id]);
      });
    } else {
      PACKS[name] = payload;
    }
  });
}
function cacheAccess(){
  try {
    localStorage.setItem(K_LIC, ACCESS.key);
    localStorage.setItem(K_GRANTS, JSON.stringify({
      codes: ACCESS.codes, seats: ACCESS.seats, used: ACCESS.used, grants: ACCESS.cache
    }));
  } catch(e){
    // Out of quota, or storage blocked. The unlock holds for this session; it
    // just has to be fetched again next time.
  }
}
function forgetAccess(){
  try { localStorage.removeItem(K_LIC); localStorage.removeItem(K_GRANTS); } catch(e){}
}
function restoreAccess(){
  var raw = null;
  try {
    ACCESS.key = localStorage.getItem(K_LIC) || "";
    raw = JSON.parse(localStorage.getItem(K_GRANTS) || "null");
  } catch(e){ raw = null; }
  if (!raw || !raw.grants) return false;
  ACCESS.codes = raw.codes || "";
  ACCESS.seats = raw.seats || 0;
  ACCESS.used = raw.used || 0;
  ACCESS.cache = raw.grants;
  applyGrants(raw.grants);
  return true;
}

/* ---------------- talking to the endpoint ---------------- */
function postJSON(url, body){
  if (!url) return Promise.reject(new Error("no-endpoint"));
  return fetch(url, {
    method:"POST", headers:{"Content-Type":"application/json"},
    body: JSON.stringify(body)
  }).then(function(r){
    return r.json().catch(function(){ return {}; }).then(function(j){
      if (!r.ok || j.error){
        var err = new Error(j.error || ("http-" + r.status));
        err.status = r.status;
        err.revoked = j.revoked === true;
        throw err;
      }
      return j;
    });
  });
}
function takeUnlock(res, key){
  ACCESS.key = key || ACCESS.key;
  ACCESS.codes = res.codes || "";
  ACCESS.seats = res.seats || 0;
  ACCESS.used = res.used || 0;
  ACCESS.cache = res.grants || {};
  applyGrants(res.grants);
  cacheAccess();
}
function unlockWithKey(key){
  return postJSON(PW.unlockUrl, { key:key, install:installId() })
    .then(function(res){ takeUnlock(res, key); return res; });
}
function claimWithNonce(n){
  return postJSON(PW.claimUrl, { nonce:n, install:installId() })
    .then(function(res){ takeUnlock(res, res.key || ""); return res; });
}
function refreshAccess(){
  // Re-check a cached unlock in the background. A network failure is ignored:
  // losing the guide because a café wifi is down would be worse than serving a
  // refunded licence for one more session. An explicit refusal is not ignored —
  // that is what a refund has to be able to do.
  if (!ACCESS.key || !PW.unlockUrl) return;
  postJSON(PW.unlockUrl, { key:ACCESS.key, install:installId() })
    .then(function(res){ takeUnlock(res, ACCESS.key); })
    .catch(function(err){
      if (err && (err.revoked || err.status === 403)){
        forgetAccess();
        location.reload();
      }
    });
}

/* ---------------- the gate panel ---------------- */
function gate(what, offer){
  var p = price(offer), url = checkoutUrl(offer);
  return '<div class="gate noprint"><p class="gate-k">' + lockSvg(12) + "<span>" +
    T("lock.badge") + "</span></p>" +
    "<h3>" + T("lock.h") + "</h3>" +
    "<p>" + T("lock." + what) + "</p>" +
    '<p class="small">' + T("lock.reading", {n:CH.length, s:freeChapters()}) + "</p>" +
    '<div class="gate-row">' +
    (url ? '<a class="buy" href="' + esc(url) + '" data-buy>' +
        T("lock.cta", {p:p}) + "</a>" : "") +
    '<button type="button" class="plain" data-unlock>' + T("lock.have") + "</button>" +
    "</div></div>";
}

/* ---------------- the access dialog ---------------- */
var accessDlg = document.getElementById("accessDlg");
var accessBody = document.getElementById("accessBody");
function accessMsg(text, kind){
  var el = accessBody.querySelector(".msg");
  if (el){ el.className = "msg" + (kind ? " " + kind : ""); el.innerHTML = text; }
}
function unlockError(err){
  // A 400 means the key itself was not accepted, and the endpoint deliberately
  // will not say which way — forged, mistyped and expired look identical from
  // outside. A 403 is different: the licence is real and the reason is
  // something the buyer can act on, so pass it through rather than sending
  // them off to check a key that is perfectly fine.
  if (!err || err.message === "no-endpoint") return T("unlock.offline");
  if (err.status === 403 && err.message) return esc(err.message);
  if (err.status) return T("unlock.badkey", {e:esc(PW.support || "")});
  return T("unlock.offline");
}
function drawAccess(){
  var support = PW.support || "";
  var note = PW.note ? '<p class="small">' + esc(PW.note) + "</p>" : "";
  if (!anyLocked() && ACCESS.key){
    accessBody.innerHTML = note +
      "<p>" + T("unlock.status", {u:ACCESS.used || 1, s:ACCESS.seats || 1}) + "</p>" +
      '<p class="small">' + T("unlock.keyIs") + ": <code>" + esc(ACCESS.key) + "</code></p>" +
      '<div class="dlg-row"><button type="button" class="plain" data-forget>' +
        T("unlock.forget") + "</button>" +
      '<button class="buy dlg-x" value="close">' + T("unlock.close") + "</button></div>" +
      '<p class="msg"></p>' +
      '<p class="small">' + T("unlock.forgetNote", {e:esc(support)}) + "</p>";
  } else {
    var url = checkoutUrl("core");
    accessBody.innerHTML = note +
      "<p>" + T("unlock.have") + "</p>" +
      '<input class="keyin" id="keyIn" type="text" autocomplete="off" spellcheck="false" ' +
        'placeholder="' + esc(T("unlock.ph")) + '" aria-label="' + esc(T("unlock.have")) +
        '" value="' + esc(ACCESS.key || "") + '">' +
      '<p class="msg"></p>' +
      '<div class="dlg-row"><button type="button" class="buy" data-dounlock>' +
        T("unlock.go") + "</button>" +
      (url ? '<a class="plain" href="' + esc(url) + '" data-buy>' + T("unlock.buy") + "</a>" : "") +
      '<button class="plain dlg-x" value="close">' + T("unlock.close") + "</button></div>" +
      (support ? "<p class=\"small\">" + T("unlock.support",
        {e:'<a href="mailto:' + esc(support) + '">' + esc(support) + "</a>"}) + "</p>" : "");
  }
  wireAccess();
}
function wireAccess(){
  var input = accessBody.querySelector("#keyIn");
  var go = accessBody.querySelector("[data-dounlock]");
  if (go){
    go.onclick = function(){
      var key = (input && input.value || "").trim();
      if (!key) return;
      go.disabled = true;
      accessMsg(T("unlock.busy"));
      unlockWithKey(key).then(function(){
        accessMsg(T("unlock.ok"), "good");
        render(); paintAccess();
        setTimeout(function(){ try { accessDlg.close(); } catch(e){} }, 900);
      }).catch(function(err){
        go.disabled = false;
        accessMsg(unlockError(err), "bad");
      });
    };
  }
  if (input){
    input.onkeydown = function(e){ if (e.key === "Enter" && go){ e.preventDefault(); go.click(); } };
  }
  var forget = accessBody.querySelector("[data-forget]");
  if (forget) forget.onclick = function(){ forgetAccess(); location.reload(); };
  accessBody.querySelectorAll("a[data-buy]").forEach(function(a){
    a.addEventListener("click", function(){
      a.href = withNonce(a.href);
      try { accessDlg.close(); } catch(e){}
    });
  });
}
function openAccess(){
  drawAccess();
  if (accessDlg.showModal) accessDlg.showModal(); else accessDlg.setAttribute("open", "");
  var input = accessBody.querySelector("#keyIn");
  if (input) input.focus();
}
function paintAccess(){
  var btn = document.getElementById("accessBtn");
  if (!btn) return;
  var full = !anyLocked();
  btn.textContent = full ? T("acct.full") : T("acct.free");
  btn.className = "chip" + (full ? " on" : "");
}

/* ---------------- claiming a purchase straight after checkout ---------------- */
function claimFromUrl(){
  var match = /[?&]claim=([^&]+)/.exec(location.search || "");
  if (!match) return;
  openAccess();
  accessMsg(T("unlock.claiming"));
  claimWithNonce(decodeURIComponent(match[1])).then(function(){
    accessMsg(T("unlock.ok"), "good");
    render(); paintAccess(); drawAccess();
    try { history.replaceState(null, "", location.pathname + location.hash); } catch(e){}
  }).catch(function(){
    drawAccess();
    accessMsg(T("unlock.claimFail", {e:esc(PW.support || "")}), "bad");
  });
}

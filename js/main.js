// flip to true to enable the waitlist popup sitewide; flip back to disable
const WAITLIST_ACTIVE = false;

document.addEventListener("DOMContentLoaded",function(){const e=document.querySelector(".nav-toggle"),t=document.querySelectorAll(".main-nav__list");e&&e.addEventListener("click",function(){t.forEach(function(e){e.classList.toggle("is-open")}),e.classList.toggle("is-active");const n="true"===e.getAttribute("aria-expanded");e.setAttribute("aria-expanded",String(!n))}),document.querySelectorAll(".main-nav__item--has-dropdown > .main-nav__link").forEach(function(e){e.addEventListener("click",function(e){window.innerWidth<=768&&(e.preventDefault(),this.parentElement.classList.toggle("is-open"))})}),document.querySelectorAll(".faq-item__question").forEach(function(e){e.addEventListener("click",function(){const e=this.closest(".faq-item"),t=e.classList.contains("is-open");document.querySelectorAll(".faq-item").forEach(function(e){e.classList.remove("is-open")}),t||e.classList.add("is-open")})})});

(function () {
  if (!WAITLIST_ACTIVE) return;

  var PORTAL = "deirdre-kuvaas.clientsecure.me";
  var overlay = null;
  var lastFocus = null;

  function isPortalLink(a) {
    if (!a || !a.href) return false;
    try { return new URL(a.href, location.href).hostname === PORTAL; } catch (err) { return false; }
  }

  function injectStyles() {
    if (document.getElementById("waitlist-modal-styles")) return;
    var css =
      ".waitlist-overlay{position:fixed;inset:0;z-index:1000;display:flex;align-items:center;justify-content:center;padding:1.5rem;background:rgba(54,54,54,.55)}" +
      ".waitlist-modal{background:var(--color-cream,#F1EEE3);color:var(--color-body-text,#363636);max-width:440px;width:100%;padding:2rem 2rem 1.5rem;border-top:4px solid var(--color-sage,#5F7C54);border-radius:6px;box-shadow:0 8px 32px rgba(0,0,0,.2);text-align:center;font-family:var(--font-body,'Work Sans',sans-serif)}" +
      ".waitlist-modal h2{font-size:1.5rem;color:var(--color-olive-dark,#434539);margin:0 0 1rem}" +
      ".waitlist-modal p{font-size:1rem;line-height:1.6;margin:0 0 1.5rem}" +
      ".waitlist-modal__join{display:inline-block;background:var(--color-sage,#5F7C54);color:#fff;font-family:var(--font-ui,'Work Sans',sans-serif);font-size:.875rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;padding:.75rem 1.75rem;border:none;border-radius:4px;cursor:pointer;transition:background-color .25s ease}" +
      ".waitlist-modal__join:hover,.waitlist-modal__join:focus-visible{background:var(--color-sage-dark,#3E5237)}" +
      ".waitlist-modal__later{display:block;margin:1rem auto 0;background:none;border:none;color:var(--color-olive,#646756);font-family:var(--font-ui,'Work Sans',sans-serif);font-size:.875rem;text-decoration:underline;text-underline-offset:2px;cursor:pointer}" +
      ".waitlist-modal button:focus-visible{outline:2px solid var(--color-sage-dark,#3E5237);outline-offset:3px}";
    var style = document.createElement("style");
    style.id = "waitlist-modal-styles";
    style.textContent = css;
    document.head.appendChild(style);
  }

  function close() {
    if (!overlay) return;
    overlay.remove();
    overlay = null;
    document.removeEventListener("keydown", onKey, true);
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  function onKey(e) {
    if (e.key === "Escape" || e.key === "Esc") { e.preventDefault(); close(); return; }
    if (e.key === "Tab" && overlay) {
      var f = overlay.querySelectorAll("button");
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  }

  function open(href) {
    injectStyles();
    lastFocus = document.activeElement;
    overlay = document.createElement("div");
    overlay.className = "waitlist-overlay";

    var modal = document.createElement("div");
    modal.className = "waitlist-modal";
    modal.setAttribute("role", "dialog");
    modal.setAttribute("aria-modal", "true");
    modal.setAttribute("aria-labelledby", "waitlist-modal-title");

    var h = document.createElement("h2");
    h.id = "waitlist-modal-title";
    h.textContent = "Thank you for reaching out";

    var p = document.createElement("p");
    p.textContent = "Deirdre's caseload is currently full. You're welcome to join the waitlist. She reaches out personally as soon as the next opening becomes available.";

    var join = document.createElement("button");
    join.type = "button";
    join.className = "waitlist-modal__join";
    join.textContent = "Join the Waitlist";
    join.addEventListener("click", function () { window.location.href = href; });

    var later = document.createElement("button");
    later.type = "button";
    later.className = "waitlist-modal__later";
    later.textContent = "Maybe later";
    later.addEventListener("click", close);

    modal.appendChild(h);
    modal.appendChild(p);
    modal.appendChild(join);
    modal.appendChild(later);
    overlay.appendChild(modal);
    overlay.addEventListener("click", function (e) { if (e.target === overlay) close(); });
    document.body.appendChild(overlay);
    document.addEventListener("keydown", onKey, true);
    join.focus();
  }

  // Capture phase on window so this runs before the SimplePractice widget's
  // own click handler on the Request Consultation button.
  window.addEventListener("click", function (e) {
    if (overlay || e.defaultPrevented || e.button !== 0) return;
    var a = e.target && e.target.closest ? e.target.closest("a[href]") : null;
    if (!isPortalLink(a)) return;
    e.preventDefault();
    e.stopImmediatePropagation();
    open(a.href);
  }, true);
})();

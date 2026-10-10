(function () {
  "use strict";

  var header = document.querySelector(".site-header");
  var button = document.querySelector(".menu-toggle");
  var nav = document.getElementById("primary-navigation");
  if (!header || !button || !nav) return;

  var mobile = window.matchMedia("(max-width: 52rem)");

  function closeMenu(restoreFocus) {
    header.classList.remove("menu-open");
    button.setAttribute("aria-expanded", "false");
    if (restoreFocus && mobile.matches) button.focus();
  }

  button.addEventListener("click", function () {
    var open = button.getAttribute("aria-expanded") !== "true";
    header.classList.toggle("menu-open", open);
    button.setAttribute("aria-expanded", String(open));
  });

  nav.addEventListener("click", function (event) {
    if (event.target.closest("a")) closeMenu(true);
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && button.getAttribute("aria-expanded") === "true") {
      closeMenu(true);
    }
  });

  document.addEventListener("click", function (event) {
    if (!header.contains(event.target)) closeMenu(nav.contains(document.activeElement));
  });

  mobile.addEventListener("change", function () {
    closeMenu(nav.contains(document.activeElement));
  });

  header.classList.add("navigation-ready");
  if (mobile.matches && nav.contains(document.activeElement)) button.focus();
}());

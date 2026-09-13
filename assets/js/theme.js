(function () {
  "use strict";

  var key = "anoop-theme";
  var root = document.documentElement;
  var system = window.matchMedia("(prefers-color-scheme: dark)");
  var button = document.querySelector(".theme-toggle");

  function savedTheme() {
    try {
      var value = localStorage.getItem(key);
      return value === "light" || value === "dark" ? value : null;
    } catch (_) {
      return null;
    }
  }

  function effectiveTheme() {
    return savedTheme() || (system.matches ? "dark" : "light");
  }

  function updateControls() {
    var current = effectiveTheme();
    var next = current === "dark" ? "light" : "dark";
    var label = "Switch to " + next + " theme";
    var meta = document.querySelector('meta[name="theme-color"]');

    if (button) {
      button.setAttribute("aria-label", label);
      button.setAttribute("title", label + "; system theme is used until you choose");
      button.setAttribute("aria-pressed", current === "dark" ? "true" : "false");
      var text = button.querySelector(".theme-toggle-text");
      if (text) text.textContent = current === "dark" ? "Dark" : "Light";
    }

    if (meta) {
      meta.content = current === "dark"
        ? (meta.dataset.dark || "#101715")
        : (meta.dataset.light || "#f7f5ef");
    }
  }

  if (button) {
    button.addEventListener("click", function () {
      var next = effectiveTheme() === "dark" ? "light" : "dark";
      try { localStorage.setItem(key, next); } catch (_) {}
      root.dataset.theme = next;
      updateControls();
    });
  }

  system.addEventListener("change", function () {
    if (!savedTheme()) updateControls();
  });

  updateControls();
}());

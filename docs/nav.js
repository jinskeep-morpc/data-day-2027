/* Data Day 2027 — accessible nav dropdowns.
   Click to toggle; closes on Escape, outside-click, and focus leaving the menu.
   Arrow keys move between items. No dependencies. */
(function () {
  "use strict";

  var menus = Array.prototype.slice.call(document.querySelectorAll(".navitem--menu"));
  if (!menus.length) return;

  function panelOf(menu) { return menu.querySelector(".navmenu"); }
  function btnOf(menu) { return menu.querySelector(".navitem__btn"); }
  function itemsOf(menu) {
    return Array.prototype.slice.call(menu.querySelectorAll("a.navmenu__item"));
  }

  function close(menu) {
    btnOf(menu).setAttribute("aria-expanded", "false");
    panelOf(menu).removeAttribute("data-open");
  }
  function open(menu) {
    btnOf(menu).setAttribute("aria-expanded", "true");
    panelOf(menu).setAttribute("data-open", "true");
  }
  function closeAll(except) {
    menus.forEach(function (m) { if (m !== except) close(m); });
  }

  menus.forEach(function (menu) {
    var btn = btnOf(menu);
    var items = itemsOf(menu);

    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      var isOpen = btn.getAttribute("aria-expanded") === "true";
      closeAll(menu);
      if (isOpen) { close(menu); } else { open(menu); }
    });

    btn.addEventListener("keydown", function (e) {
      if (e.key === "ArrowDown" || e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        closeAll(menu);
        open(menu);
        if (items[0]) items[0].focus();
      }
    });

    menu.addEventListener("keydown", function (e) {
      var idx = items.indexOf(document.activeElement);
      if (e.key === "ArrowDown") {
        e.preventDefault();
        if (items[idx + 1]) items[idx + 1].focus();
      } else if (e.key === "ArrowUp") {
        e.preventDefault();
        if (idx > 0) { items[idx - 1].focus(); }
        else { btn.focus(); }
      } else if (e.key === "Escape") {
        close(menu);
        btn.focus();
      }
    });

    // Close when focus moves outside this menu (e.g. Tab out).
    menu.addEventListener("focusout", function (e) {
      if (!menu.contains(e.relatedTarget)) { close(menu); }
    });
  });

  document.addEventListener("click", function (e) {
    if (!e.target.closest(".navitem--menu")) { closeAll(null); }
  });
})();

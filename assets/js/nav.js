(function () {
  function normalizeBaseurl(b) {
    if (!b) return "";
    if (b === "/") return "";
    if (b.endsWith("/")) return b.slice(0, -1);
    return b;
  }

  function stripBaseurl(path, b) {
    if (!b) return path;
    if (path.indexOf(b + "/") === 0) return path.slice(b.length);
    if (path === b) return "/";
    return path;
  }

  function addKoPrefix(path) {
    if (path === "/") return "/ko/";
    if (path.indexOf("/ko/") === 0) return path;
    return "/ko" + path;
  }

  function removeKoPrefix(path) {
    if (path.indexOf("/ko/") === 0) {
      var rest = path.slice(3);
      return rest === "" ? "/" : rest;
    }
    return path;
  }

  function buildUrl(targetPath, baseurl) {
    return baseurl + targetPath + window.location.search + window.location.hash;
  }

  function closeNav() {
    var menu = document.getElementById("nav-links");
    var btn = document.querySelector(".nav-toggle");
    if (menu) menu.classList.remove("is-open");
    if (btn) btn.setAttribute("aria-expanded", "false");
  }

  function toggleNav() {
    var menu = document.getElementById("nav-links");
    var btn = document.querySelector(".nav-toggle");
    if (!menu || !btn) return;

    var isOpen = menu.classList.toggle("is-open");
    btn.setAttribute("aria-expanded", isOpen ? "true" : "false");
  }

  document.addEventListener("DOMContentLoaded", function () {
    var baseurl = normalizeBaseurl(window.__SITE_BASEURL__ || "");

    /* Hamburger */
    var btn = document.querySelector(".nav-toggle");
    if (btn) {
      btn.addEventListener("click", function (e) {
        e.stopPropagation();
        toggleNav();
      });
    }

    document.addEventListener("click", function (e) {
      var menu = document.getElementById("nav-links");
      if (!menu || !btn) return;
      if (!menu.contains(e.target) && !btn.contains(e.target)) {
        closeNav();
      }
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeNav();
    });

    /* Language toggle */
    var toggle = document.getElementById("lang-toggle");
    if (!toggle) return;

    toggle.addEventListener("click", function (e) {
      var a = e.target.closest("a[data-lang]");
      if (!a) return;

      e.preventDefault();

      var lang = a.getAttribute("data-lang");
      var path = stripBaseurl(window.location.pathname, baseurl);
      var targetPath =
        lang === "ko"
          ? addKoPrefix(removeKoPrefix(path))
          : removeKoPrefix(path);

      window.location.href = buildUrl(targetPath, baseurl);
    });
  });
})();

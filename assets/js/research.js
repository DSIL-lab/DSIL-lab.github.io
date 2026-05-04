document.addEventListener("DOMContentLoaded", function() {
  var researchRoot = document.querySelector(".research-wrap");
  if (!researchRoot) return;

  var researchOrder = [];
  var researchTitles = {};
  var currentIndex = -1;

  var prev = document.getElementById("research-prev");
  var next = document.getElementById("research-next");
  var back = document.getElementById("research-back");

  var prevBaseLabel = prev ? prev.textContent.trim() : "Previous";
  var nextBaseLabel = next ? next.textContent.trim() : "Next";

  function getSlugFromHash() {
    var h = location.hash || "";
    if (h.indexOf("#") === 0) h = h.slice(1);
    return h.trim();
  }

  function setViewModeForMobile() {
    var slug = getSlugFromHash();
    document.body.classList.remove("research-list-view");
    document.body.classList.remove("research-detail-view");
    if (slug) document.body.classList.add("research-detail-view");
    else document.body.classList.add("research-list-view");
  }

  function hideAllArticles() {
    var articles = document.querySelectorAll(".research-article");
    for (var i = 0; i < articles.length; i++) {
      articles[i].style.display = "none";
    }
  }

  function setActiveLink(slug) {
    var links = document.querySelectorAll(".research-link");
    for (var i = 0; i < links.length; i++) {
      links[i].classList.remove("is-active");
      if (links[i].dataset.slug === slug) links[i].classList.add("is-active");
    }
  }

  function updatePrevNext(slug) {
    if (!prev || !next) return;

    currentIndex = researchOrder.indexOf(slug);

    if (currentIndex > 0) {
      var prevSlug = researchOrder[currentIndex - 1];
      prev.href = "#" + prevSlug;
      prev.textContent = prevBaseLabel + ": " + (researchTitles[prevSlug] || prevBaseLabel);
      prev.classList.remove("is-disabled");
    } else {
      prev.href = "#";
      prev.textContent = prevBaseLabel;
      prev.classList.add("is-disabled");
    }

    if (currentIndex >= 0 && currentIndex < researchOrder.length - 1) {
      var nextSlug = researchOrder[currentIndex + 1];
      next.href = "#" + nextSlug;
      next.textContent = (researchTitles[nextSlug] || nextBaseLabel) + " :" + nextBaseLabel;
      next.classList.remove("is-disabled");
    } else {
      next.href = "#";
      next.textContent = nextBaseLabel;
      next.classList.add("is-disabled");
    }
  }

  function showBySlug(slug) {
    if (!slug) return;

    hideAllArticles();

    var active = document.getElementById("r-" + slug);
    if (active) {
      active.style.display = "block";
    }

    setActiveLink(slug);
    updatePrevNext(slug);
  }

  function buildOrderFromLinks() {
    researchOrder = [];
    researchTitles = {};

    var articles = document.querySelectorAll(".research-article");
    for (var i = 0; i < articles.length; i++) {
      var id = articles[i].id || "";
      if (id.indexOf("r-") !== 0) continue;
      var slug = id.slice(2);
      researchOrder.push(slug);
      researchTitles[slug] = articles[i].dataset.title || slug;
    }
  }

  function goToList() {
    history.pushState(null, "", location.pathname);
    syncFromHash();
  }

  function syncFromHash() {
    setViewModeForMobile();
    var slug = getSlugFromHash();

    if (slug) {
      showBySlug(slug);
    } else {
      hideAllArticles();
      setActiveLink("");
      updatePrevNext("");
    }
  }

  buildOrderFromLinks();
  hideAllArticles();

  if (back) {
    back.addEventListener("click", function(e) {
      e.preventDefault();
      goToList();
    });
  }

  syncFromHash();

  window.addEventListener("hashchange", function() {
    syncFromHash();
  });

  window.addEventListener("popstate", function() {
    syncFromHash();
  });
});

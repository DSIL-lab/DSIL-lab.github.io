---
layout: page
title: Research
---

{% assign projects = site.research | sort: "order" %}
{% assign team_order = "TD|DB|CP" | split: "|" %}

<div class="research-wrap">

  <!-- Left list -->
  <aside class="research-list" id="research-list">
    {% for team in team_order %}
      {% assign team_items = projects | where: "team", team %}
      {% if team_items.size > 0 %}
        <section class="research-team-group">
          <h3 class="research-team-title">{{ team }} Team</h3>
          <ul>
            {% for p in team_items %}
              {% assign slug = p.slug | default: p.id | split: '/' | last %}
              {% assign p_summary = p.summary | to_s | strip %}
              <li>
                <a class="research-link" href="#{{ slug }}" data-slug="{{ slug }}">
                  <span class="research-link-title">{{ p.title }}</span>
                  {% if p_summary != '' %}
                    <div class="research-link-summary">{{ p_summary | markdownify }}</div>
                  {% endif %}
                </a>
              </li>
            {% endfor %}
          </ul>
        </section>
      {% endif %}
    {% endfor %}

  </aside>

  <!-- Right content -->
  <div class="research-detail" id="research-detail">
    <a href="#" class="research-back" id="research-back">◀ Back to list</a>

    {% for team in team_order %}
      {% assign team_items = projects | where: "team", team %}
      {% for p in team_items %}
        {% assign slug = p.slug | default: p.id | split: '/' | last %}
        <article class="research-article article-page" id="r-{{ slug }}" data-title="{{ p.title | strip_html }}">
            <header class="article-header">
              <h1 class="article-title">{{ p.title }}</h1>
            </header>
            <div class="article-body research-body">
              {{ p.content }}
            </div>
        </article>
      {% endfor %}
    {% endfor %}
  </div>

</div>

<!-- Mobile bottom nav (outside the detail box) -->
<div class="research-mobile-nav" id="research-mobile-nav">
  <a class="research-nav-btn" id="research-prev" href="#">◀ Previous</a>
  <a class="research-nav-btn" id="research-next" href="#">Next ▶</a>
</div>

<script>
var researchOrder = [];   // array of slugs
var researchTitles = {};  // slug -> title
var currentIndex = -1;

function getSlugFromHash() {
  var h = location.hash || "";
  if (h.startsWith("#")) h = h.slice(1);
  return h.trim();
}

function setViewModeForMobile() {
  // mobile: if hash exists => detail view, else list view
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
  var prev = document.getElementById("research-prev");
  var next = document.getElementById("research-next");
  if (!prev || !next) return;

  currentIndex = researchOrder.indexOf(slug);

  // Prev
  if (currentIndex > 0) {
    var prevSlug = researchOrder[currentIndex - 1];
    prev.href = "#" + prevSlug;
    prev.textContent = "◀ Previous: " + (researchTitles[prevSlug] || "Previous");
    prev.classList.remove("is-disabled");
  } else {
    prev.href = "#";
    prev.textContent = "◀ Previous";
    prev.classList.add("is-disabled");
  }

  // Next
  if (currentIndex >= 0 && currentIndex < researchOrder.length - 1) {
    var nextSlug = researchOrder[currentIndex + 1];
    next.href = "#" + nextSlug;
    next.textContent = "Next: " + (researchTitles[nextSlug] || "Next") + " ▶";
    next.classList.remove("is-disabled");
  } else {
    next.href = "#";
    next.textContent = "Next ▶";
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

  // Prefer articles for titles (stable even if list hidden)
  var articles = document.querySelectorAll(".research-article");
  for (var i = 0; i < articles.length; i++) {
    var id = articles[i].id || "";
    if (!id.startsWith("r-")) continue;
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

document.addEventListener("DOMContentLoaded", function() {
  buildOrderFromLinks();
  hideAllArticles();

  // Back to list link
  var back = document.getElementById("research-back");
  if (back) {
    back.addEventListener("click", function(e) {
      e.preventDefault();
      goToList();
    });
  }

  // Initial render
  syncFromHash();

  // If no hash, set hash to first for PC only? No.
  // You said: PC index shows order 0, mobile shows list only.
  // So do not force hash on load.
});

window.addEventListener("hashchange", function() {
  syncFromHash();
});

window.addEventListener("popstate", function() {
  syncFromHash();
});
</script>

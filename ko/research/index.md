---
layout: page
title: Research
permalink: /ko/research/
---

{% assign projects = site.ko_research | sort: "order" %}

<div class="research-wrap">

  <aside class="research-list" id="research-list">
    <ul>
        {% for p in projects %}
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
  </aside>

  <div class="research-detail" id="research-detail">
    <a href="#" class="research-back" id="research-back">◀ 목록으로</a>

    {% for p in projects %}
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
  </div>

</div>

<div class="research-mobile-nav" id="research-mobile-nav">
  <a class="research-nav-btn" id="research-prev" href="#">◀ 이전</a>
  <a class="research-nav-btn" id="research-next" href="#">다음 ▶</a>
</div>

<script>
var researchOrder = [];
var researchTitles = {};
var currentIndex = -1;

function getSlugFromHash() {
  var h = location.hash || "";
  if (h.startsWith("#")) h = h.slice(1);
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
  var prev = document.getElementById("research-prev");
  var next = document.getElementById("research-next");
  if (!prev || !next) return;

  currentIndex = researchOrder.indexOf(slug);

  if (currentIndex > 0) {
    var prevSlug = researchOrder[currentIndex - 1];
    prev.href = "#" + prevSlug;
    prev.textContent = "◀ 이전: " + (researchTitles[prevSlug] || "이전");
    prev.classList.remove("is-disabled");
  } else {
    prev.href = "#";
    prev.textContent = "◀ 이전";
    prev.classList.add("is-disabled");
  }

  if (currentIndex >= 0 && currentIndex < researchOrder.length - 1) {
    var nextSlug = researchOrder[currentIndex + 1];
    next.href = "#" + nextSlug;
    next.textContent = "다음: " + (researchTitles[nextSlug] || "다음") + " ▶";
    next.classList.remove("is-disabled");
  } else {
    next.href = "#";
    next.textContent = "다음 ▶";
    next.classList.add("is-disabled");
  }
}

function showBySlug(slug) {
  if (!slug) return;

  hideAllArticles();

  var active = document.getElementById("r-" + slug);
  if (active) active.style.display = "block";

  setActiveLink(slug);
  updatePrevNext(slug);
}

function buildOrderFromLinks() {
  researchOrder = [];
  researchTitles = {};

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
  setViewModeForMobile();
  if (!getSlugFromHash() && researchOrder.length > 0) {
    showBySlug(researchOrder[0]);
    setActiveLink(researchOrder[0]);
  }
}

function syncFromHash() {
  setViewModeForMobile();
  var slug = getSlugFromHash();

  if (slug) {
    showBySlug(slug);
  } else {
    if (researchOrder.length > 0) showBySlug(researchOrder[0]);
  }
}

document.addEventListener("DOMContentLoaded", function() {
  buildOrderFromLinks();
  hideAllArticles();

  var back = document.getElementById("research-back");
  if (back) {
    back.addEventListener("click", function(e) {
      e.preventDefault();
      goToList();
    });
  }

  syncFromHash();
});

window.addEventListener("hashchange", function() {
  syncFromHash();
});

window.addEventListener("popstate", function() {
  syncFromHash();
});
</script>

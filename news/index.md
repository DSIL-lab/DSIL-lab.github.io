---
layout: page
title: News
permalink: /news/
---

{% assign items = site.news | sort: "date" | reverse %}

<div class="news-feed">
  {% for n in items %}
    {% assign news_image = n.image | to_s | strip %}
    {% assign news_summary_raw = n.summary | to_s | strip %}
    {% if news_summary_raw == "" %}
      {% assign news_summary_html = n.excerpt %}
    {% else %}
      {% assign news_summary_html = news_summary_raw | markdownify %}
    {% endif %}

    <article class="news-item{% if news_image != '' %} has-image{% endif %}">
      <div class="news-item-click" data-url="{{ n.url | relative_url }}" role="link" tabindex="0" aria-label="Open news article: {{ n.title | strip_html }}">
        {% if news_image != '' %}
          <div class="news-item-media">
            <img class="news-item-image" src="{{ news_image | relative_url }}" alt="{{ n.title }}">
          </div>
        {% endif %}

        <div class="news-item-main">
        <div class="news-item-head">
          <h2 class="news-item-title">{{ n.title }}</h2>
          {% if n.date %}
            <div class="news-item-date">{{ n.date | date: "%b %d, %Y" }}</div>
          {% endif %}
        </div>
          <div class="news-item-excerpt">{{ news_summary_html }}</div>
        </div>
      </div>
    </article>
  {% endfor %}
</div>

<script>
document.addEventListener("DOMContentLoaded", function() {
  var cards = document.querySelectorAll(".news-item-click");
  cards.forEach(function(card) {
    card.addEventListener("click", function(e) {
      // Keep inner links usable (summary markdown may include links).
      if (e.target.closest("a")) return;
      var url = card.getAttribute("data-url");
      if (url) window.location.href = url;
    });

    card.addEventListener("keydown", function(e) {
      if (e.key === "Enter" || e.key === " ") {
        if (e.target.closest("a")) return;
        e.preventDefault();
        var url = card.getAttribute("data-url");
        if (url) window.location.href = url;
      }
    });
  });
});
</script>
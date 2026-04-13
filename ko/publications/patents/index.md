---
layout: page
title: Patents
permalink: /ko/publications/patents/
---

<div class="pub-legend">
  <div>* Corresponding authors</div>
  <div>&dagger; The authors equally contributed</div>
  <div>Lab member names in <strong>bold</strong></div>
</div>

{% assign items_all = site.publications | where_exp: "p", "p.type contains 'patent'" %}
{% assign years = items_all | map: "year" | uniq | sort | reverse %}

<section class="pub-section">
  <h2 class="pub-section-title">Patents</h2>

  {% if items_all.size == 0 %}
    <p>No patent records yet.</p>
  {% else %}
    {% for y in years %}
      <div class="pub-year-block">
        <h3 class="pub-year">{{ y }}</h3>

        {% assign items = items_all | where: "year", y | sort: "pub-id" | reverse %}
        <ol class="pub-list">
          {% for p in items %}
            <li class="pub-item">
              <div class="pub-title-line">
                {% if p.title_url and p.title_url != "" %}
                  <a class="pub-title" href="{{ p.title_url }}" target="_blank" rel="noopener">{{ p.title }}</a>
                {% else %}
                  <span class="pub-title">{{ p.title }}</span>
                {% endif %}
              </div>

              {% if p.authors and p.authors != "" %}
                <div class="pub-authors">{{ p.authors }}</div>
              {% endif %}

              {% if p.venue and p.venue != "" %}
                <div class="pub-meta"><span class="pub-venue">{{ p.venue }}</span></div>
              {% endif %}
            </li>
          {% endfor %}
        </ol>
      </div>
    {% endfor %}
  {% endif %}
</section>

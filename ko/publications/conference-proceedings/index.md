---
layout: page
title: Conference Proceedings
permalink: /ko/publications/conference-proceedings/
---

<div class="pub-legend">
  <div>* Corresponding authors</div>
  <div>&dagger; The authors equally contributed</div>
  <div>Lab member names in <strong>bold</strong></div>
</div>

{% assign items_a = site.publications | where: "type", "conference" %}
{% assign items_b = site.publications | where_exp: "p", "p.type contains 'conference-proceeding'" %}
{% assign items_all = items_a | concat: items_b %}
{% assign years = items_all | map: "year" | uniq | sort | reverse %}

<section class="pub-section">
  <h2 class="pub-section-title">Conference Proceedings</h2>

  {% for y in years %}
    <div class="pub-year-block">
      <h3 class="pub-year">{{ y }}</h3>

      {% assign items = items_all | where: "year", y | sort: "pub-id" | reverse %}
      <ol class="pub-list">
        {% for p in items %}
          <li class="pub-item">
            <div class="pub-title-line">
              {% if p["pub-id"] %}
                <span class="pub-id">[{{ p["pub-id"] | plus: 0 | prepend: "000" | slice: -3, 3 }}]</span>
              {% endif %}

              {% if p.title_url and p.title_url != "" %}
                <a class="pub-title" href="{{ p.title_url }}" target="_blank" rel="noopener">{{ p.title }}</a>
              {% else %}
                <span class="pub-title">{{ p.title }}</span>
              {% endif %}
            </div>

            {% if p.authors and p.authors != "" %}
              <div class="pub-authors">{{ p.authors }}</div>
            {% endif %}

            <div class="pub-meta">
              {% if p.status and p.status != "published" %}
                <span class="pub-status">{{ p.status | replace: "_", " " }}</span>
              {% else %}
                {% if p.venue and p.venue != "" %}
                  <span class="pub-venue">{{ p.venue }}</span>
                {% endif %}
                {% if p.venue_detail and p.venue_detail != "" %}
                  <span class="pub-venue-detail">{{ p.venue_detail }}</span>
                {% endif %}
              {% endif %}
            </div>
          </li>
        {% endfor %}
      </ol>
    </div>
  {% endfor %}
</section>

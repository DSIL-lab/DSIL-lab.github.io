---
layout: page
title: Publications
permalink: /publications/
---

<div class="pub-legend">
  <div>* Corresponding authors</div>
  <div>&dagger; The authors equally contributed</div>
  <div>Lab member names in <strong>bold</strong></div>
</div>

{% assign pubs = site.publications %}

{% assign journals = pubs | where_exp: "p", "p.type == 'journal' or p.type contains 'journal'" %}
{% assign conferences = pubs | where_exp: "p", "p.type == 'conference' or p.type == 'conference-proceeding' or p.type contains 'conference-proceeding'" %}
{% assign talks = pubs | where_exp: "p", "p.type == 'invited_talk' or p.type == 'invited-talk' or p.type contains 'invited-talk' or p.type contains 'invited_talk'" %}

<section class="pub-section">
  <h2 class="pub-section-title">Journal Articles</h2>

  {% assign journal_years = journals | map: "year" | uniq | sort | reverse %}
  {% for y in journal_years %}
    <div class="pub-year-block">
      <h3 class="pub-year">{{ y }}</h3>

      {% assign items = journals | where: "year", y %}
      {% assign items = items | sort: "pub-id" | reverse %}

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
                {% if p.highlights and p.highlights != "" %}
                  <span class="pub-highlights"> - {{ p.highlights }}</span>
                {% endif %}
              {% endif %}
            </div>
          </li>
        {% endfor %}
      </ol>
    </div>
  {% endfor %}
</section>

<section class="pub-section">
  <h2 class="pub-section-title">Conferences</h2>

  {% assign conf_years = conferences | map: "year" | uniq | sort | reverse %}
  {% for y in conf_years %}
    <div class="pub-year-block">
      <h3 class="pub-year">{{ y }}</h3>

      {% assign items = conferences | where: "year", y %}
      {% assign items = items | sort: "pub-id" | reverse %}

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

<section class="pub-section">
  <h2 class="pub-section-title">Invited Talks</h2>

  {% assign talk_years = talks | map: "year" | uniq | sort | reverse %}
  {% for y in talk_years %}
    <div class="pub-year-block">
      <h3 class="pub-year">{{ y }}</h3>

      {% assign items = talks | where: "year", y %}
      {% assign items = items | sort: "pub-id" | reverse %}

      <ol class="pub-list pub-talks">
        {% for t in items %}
          <li class="pub-item pub-talk-item">
            <div class="pub-title-line">
              {% if t.title_url and t.title_url != "" %}
                <a class="pub-title" href="{{ t.title_url }}" target="_blank" rel="noopener">{{ t.title }}</a>
              {% else %}
                <span class="pub-title">{{ t.title }}</span>
              {% endif %}
            </div>

            {% if t.speaker and t.speaker != "" %}
              <div class="pub-authors">{{ t.speaker }}</div>
            {% endif %}

            {% if t.event and t.event != "" %}
              <div class="pub-meta">
                <span class="pub-venue">{{ t.event }}</span>
                {% if t.event_detail and t.event_detail != "" %}
                  <span class="pub-venue-detail"> ({{ t.event_detail }})</span>
                {% endif %}
              </div>
            {% endif %}
          </li>
        {% endfor %}
      </ol>
    </div>
  {% endfor %}
</section>

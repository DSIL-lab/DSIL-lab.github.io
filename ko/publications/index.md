---
layout: page
title: Publications
permalink: /ko/publications/
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
          {% assign p_title = p["ko-title"] | default: p.title %}
          {% assign p_authors = p["ko-authors"] | default: p.authors %}
          {% assign p_status = p["ko-status"] | default: p.status %}
          {% assign p_venue = p["ko-venue"] | default: p.venue %}
          {% assign p_venue_detail = p["ko-venue_detail"] | default: p.venue_detail %}
          {% assign p_highlights = p["ko-highlights"] | default: p.highlights %}
          <li class="pub-item">
            <div class="pub-title-line">
              {% if p["pub-id"] %}
                <span class="pub-id">[{{ p["pub-id"] | plus: 0 | prepend: "000" | slice: -3, 3 }}]</span>
              {% endif %}

              {% if p.title_url and p.title_url != "" %}
                <a class="pub-title" href="{{ p.title_url }}" target="_blank" rel="noopener">{{ p_title }}</a>
              {% else %}
                <span class="pub-title">{{ p_title }}</span>
              {% endif %}
            </div>

            {% if p_authors and p_authors != "" %}
              <div class="pub-authors">{{ p_authors }}</div>
            {% endif %}

            <div class="pub-meta">
              {% if p_status and p_status != "published" %}
                <span class="pub-status">{{ p_status | replace: "_", " " }}</span>
              {% else %}
                {% if p_venue and p_venue != "" %}
                  <span class="pub-venue">{{ p_venue }}</span>
                {% endif %}
                {% if p_venue_detail and p_venue_detail != "" %}
                  <span class="pub-venue-detail">{{ p_venue_detail }}</span>
                {% endif %}
                {% if p_highlights and p_highlights != "" %}
                  <span class="pub-highlights"> - {{ p_highlights }}</span>
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
  <h2 class="pub-section-title">Conference Proceedings</h2>

  {% assign conf_years = conferences | map: "year" | uniq | sort | reverse %}
  {% for y in conf_years %}
    <div class="pub-year-block">
      <h3 class="pub-year">{{ y }}</h3>

      {% assign items = conferences | where: "year", y %}
      {% assign items = items | sort: "pub-id" | reverse %}

      <ol class="pub-list">
        {% for p in items %}
          {% assign p_title = p["ko-title"] | default: p.title %}
          {% assign p_authors = p["ko-authors"] | default: p.authors %}
          {% assign p_status = p["ko-status"] | default: p.status %}
          {% assign p_venue = p["ko-venue"] | default: p.venue %}
          {% assign p_venue_detail = p["ko-venue_detail"] | default: p.venue_detail %}
          <li class="pub-item">
            <div class="pub-title-line">
              {% if p["pub-id"] %}
                <span class="pub-id">[{{ p["pub-id"] | plus: 0 | prepend: "000" | slice: -3, 3 }}]</span>
              {% endif %}

              {% if p.title_url and p.title_url != "" %}
                <a class="pub-title" href="{{ p.title_url }}" target="_blank" rel="noopener">{{ p_title }}</a>
              {% else %}
                <span class="pub-title">{{ p_title }}</span>
              {% endif %}
            </div>

            {% if p_authors and p_authors != "" %}
              <div class="pub-authors">{{ p_authors }}</div>
            {% endif %}

            <div class="pub-meta">
              {% if p_status and p_status != "published" %}
                <span class="pub-status">{{ p_status | replace: "_", " " }}</span>
              {% else %}
                {% if p_venue and p_venue != "" %}
                  <span class="pub-venue">{{ p_venue }}</span>
                {% endif %}
                {% if p_venue_detail and p_venue_detail != "" %}
                  <span class="pub-venue-detail">{{ p_venue_detail }}</span>
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
          {% assign t_title = t["ko-title"] | default: t.title %}
          {% assign t_speaker = t["ko-speaker"] | default: t.speaker %}
          {% assign t_event = t["ko-event"] | default: t.event %}
          {% assign t_event_detail = t["ko-event_detail"] | default: t.event_detail %}
          <li class="pub-item pub-talk-item">
            <div class="pub-title-line">
              {% if t.title_url and t.title_url != "" %}
                <a class="pub-title" href="{{ t.title_url }}" target="_blank" rel="noopener">{{ t_title }}</a>
              {% else %}
                <span class="pub-title">{{ t_title }}</span>
              {% endif %}
            </div>

            {% if t_speaker and t_speaker != "" %}
              <div class="pub-authors">{{ t_speaker }}</div>
            {% endif %}

            {% if t_event and t_event != "" %}
              <div class="pub-meta">
                <span class="pub-venue">{{ t_event }}</span>
                {% if t_event_detail and t_event_detail != "" %}
                  <span class="pub-venue-detail"> ({{ t_event_detail }})</span>
                {% endif %}
              </div>
            {% endif %}
          </li>
        {% endfor %}
      </ol>
    </div>
  {% endfor %}
</section>

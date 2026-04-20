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

{% assign journals = pubs | where_exp: "p", "p.type contains 'journal'" %}
{% assign conferences_a = pubs | where: "type", "conference" %}
{% assign conferences_b = pubs | where_exp: "p", "p.type contains 'conference-proceeding'" %}
{% assign conferences = conferences_a | concat: conferences_b %}
{% assign patents = pubs | where_exp: "p", "p.type contains 'patent'" %}
{% assign talks = pubs | where_exp: "p", "p.type contains 'invited'" %}

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
              {% if p_venue and p_venue != "" %}
                <span class="pub-venue">{{ p_venue }}</span>
              {% endif %}
              {% if p_venue_detail and p_venue_detail != "" %}
                <span class="pub-venue-detail">{{ p_venue_detail }}</span>
              {% endif %}
              {% if p_status and p_status != "published" %}
                {% if p_venue and p_venue != "" or p_venue_detail and p_venue_detail != "" %}
                  <span class="pub-sep"> &middot; </span>
                {% endif %}
                <span class="pub-status">{{ p_status | replace: "_", " " }}</span>
              {% endif %}
              {% if p_highlights and p_highlights != "" %}
                <span class="pub-highlights"> - {{ p_highlights }}</span>
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
              {% if p_venue and p_venue != "" %}
                <span class="pub-venue">{{ p_venue }}</span>
              {% endif %}
              {% if p_venue_detail and p_venue_detail != "" %}
                <span class="pub-venue-detail">{{ p_venue_detail }}</span>
              {% endif %}
              {% if p_status and p_status != "published" %}
                {% if p_venue and p_venue != "" or p_venue_detail and p_venue_detail != "" %}
                  <span class="pub-sep"> &middot; </span>
                {% endif %}
                <span class="pub-status">{{ p_status | replace: "_", " " }}</span>
              {% endif %}
            </div>
          </li>
        {% endfor %}
      </ol>
    </div>
  {% endfor %}
</section>

<section class="pub-section">
  <h2 class="pub-section-title">Patents</h2>

  {% assign patent_years = patents | map: "year" | uniq | sort | reverse %}
  {% assign patent_display_id = patents.size | plus: 0 %}
  {% for y in patent_years %}
    <div class="pub-year-block">
      <h3 class="pub-year">{{ y }}</h3>

      {% assign items = patents | where: "year", y %}
      {% assign items = items | sort: "pub-id" | reverse %}

      <ol class="pub-list">
        {% for p in items %}
          {% assign p_title = p["ko-title"] | default: p.title %}
          {% assign p_authors = p["ko-authors"] | default: p.authors %}
          {% assign p_status = p["ko-status"] | default: p.status %}
          {% assign p_status_label = p_status | replace: "filed", "출원" | replace: "registered", "등록" %}
          <li class="pub-item">
            <div class="pub-title-line">
              <span class="pub-id">[{{ patent_display_id | prepend: "000" | slice: -3, 3 }}]</span>

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
              {% if p.application_no and p.application_no != "" %}
                <span class="pub-venue">출원번호 {{ p.application_no }}</span>
              {% endif %}
              {% if p.registration_no and p.registration_no != "" %}
                {% if p.application_no and p.application_no != "" %}
                  <span class="pub-venue-detail"> &middot; </span>
                {% endif %}
                <span class="pub-venue-detail">등록번호 {{ p.registration_no }}</span>
              {% endif %}
              {% if p_status and p_status != "published" %}
                {% if p.application_no and p.application_no != "" or p.registration_no and p.registration_no != "" %}
                  <span class="pub-sep"> &middot; </span>
                {% endif %}
                <span class="pub-status">{{ p_status_label | replace: "_", " " }}</span>
              {% endif %}
            </div>
          </li>
          {% assign patent_display_id = patent_display_id | minus: 1 %}
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

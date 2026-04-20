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
              {% if p.venue and p.venue != "" %}
                <span class="pub-venue">{{ p.venue }}</span>
              {% endif %}
              {% if p.venue_detail and p.venue_detail != "" %}
                <span class="pub-venue-detail">{{ p.venue_detail }}</span>
              {% endif %}
              {% if p.status and p.status != "published" %}
                {% if p.venue and p.venue != "" or p.venue_detail and p.venue_detail != "" %}
                  <span class="pub-sep"> &middot; </span>
                {% endif %}
                <span class="pub-status">{{ p.status | replace: "_", " " }}</span>
              {% endif %}
              {% if p.highlights and p.highlights != "" %}
                <span class="pub-highlights"> - {{ p.highlights }}</span>
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
              {% if p.venue and p.venue != "" %}
                <span class="pub-venue">{{ p.venue }}</span>
              {% endif %}
              {% if p.venue_detail and p.venue_detail != "" %}
                <span class="pub-venue-detail">{{ p.venue_detail }}</span>
              {% endif %}
              {% if p.status and p.status != "published" %}
                {% if p.venue and p.venue != "" or p.venue_detail and p.venue_detail != "" %}
                  <span class="pub-sep"> &middot; </span>
                {% endif %}
                <span class="pub-status">{{ p.status | replace: "_", " " }}</span>
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
          <li class="pub-item">
            <div class="pub-title-line">
              <span class="pub-id">[{{ patent_display_id | prepend: "000" | slice: -3, 3 }}]</span>

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
              {% if p.application_no and p.application_no != "" %}
                <span class="pub-venue">Application No. {{ p.application_no }}</span>
              {% endif %}
              {% if p.registration_no and p.registration_no != "" %}
                {% if p.application_no and p.application_no != "" %}
                  <span class="pub-venue-detail"> / </span>
                {% endif %}
                <span class="pub-venue-detail">Registration No. {{ p.registration_no }}</span>
              {% endif %}
              {% if p.status and p.status != "published" %}
                {% if p.application_no and p.application_no != "" or p.registration_no and p.registration_no != "" %}
                  <span class="pub-sep"> &middot; </span>
                {% endif %}
                <span class="pub-status">{{ p.status | replace: "_", " " }}</span>
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

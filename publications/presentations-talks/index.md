---
layout: page
title: Presentations & Talks
permalink: /publications/presentations-talks/
---

{% assign talks_all = site.publications | where_exp: "p", "p.type contains 'invited'" %}
{% assign talk_years = talks_all | map: "year" | uniq | sort | reverse %}
{% assign international_all = site.publications | where_exp: "p", "p.type contains 'international-conf'" %}
{% assign international_years = international_all | map: "year" | uniq | sort | reverse %}
{% assign domestic_all = site.publications | where_exp: "p", "p.type contains 'domestic-conf'" %}
{% assign domestic_years = domestic_all | map: "year" | uniq | sort | reverse %}

<section class="pub-section">
  <h2 class="pub-section-title">Invited Talks</h2>

  {% if talks_all.size == 0 %}
    <p>No invited talks yet.</p>
  {% else %}
    {% for y in talk_years %}
      <div class="pub-year-block">
        <h3 class="pub-year">{{ y }}</h3>

        {% assign items = talks_all | where: "year", y | sort: "pub-id" | reverse %}
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
  {% endif %}
</section>

<section class="pub-section">
  <h2 class="pub-section-title">International Conferences</h2>

  {% if international_all.size == 0 %}
    <p>No international conference records yet.</p>
  {% else %}
    {% for y in international_years %}
      <div class="pub-year-block">
        <h3 class="pub-year">{{ y }}</h3>

        {% assign items = international_all | where: "year", y | sort: "pub-id" | reverse %}
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

              {% if p.venue and p.venue != "" or p.venue_detail and p.venue_detail != "" %}
                <div class="pub-meta">
                  {% if p.venue and p.venue != "" %}
                    <span class="pub-venue">{{ p.venue }}</span>
                  {% endif %}
                  {% if p.venue_detail and p.venue_detail != "" %}
                    {% if p.venue and p.venue != "" %}
                      <span class="pub-sep"> &middot; </span>
                    {% endif %}
                    <span class="pub-venue-detail">{{ p.venue_detail }}</span>
                  {% endif %}
                </div>
              {% endif %}
            </li>
          {% endfor %}
        </ol>
      </div>
    {% endfor %}
  {% endif %}
</section>

<section class="pub-section">
  <h2 class="pub-section-title">Domestic Conferences</h2>

  {% if domestic_all.size == 0 %}
    <p>No domestic conference records yet.</p>
  {% else %}
    {% for y in domestic_years %}
      <div class="pub-year-block">
        <h3 class="pub-year">{{ y }}</h3>

        {% assign items = domestic_all | where: "year", y | sort: "pub-id" | reverse %}
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

              {% if p.venue and p.venue != "" or p.venue_detail and p.venue_detail != "" %}
                <div class="pub-meta">
                  {% if p.venue and p.venue != "" %}
                    <span class="pub-venue">{{ p.venue }}</span>
                  {% endif %}
                  {% if p.venue_detail and p.venue_detail != "" %}
                    {% if p.venue and p.venue != "" %}
                      <span class="pub-sep"> &middot; </span>
                    {% endif %}
                    <span class="pub-venue-detail">{{ p.venue_detail }}</span>
                  {% endif %}
                </div>
              {% endif %}
            </li>
          {% endfor %}
        </ol>
      </div>
    {% endfor %}
  {% endif %}
</section>

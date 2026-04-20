---
layout: page
title: Presentations & Talks
permalink: /ko/publications/presentations-talks/
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

              {% if t_event and t_event != "" or t_event_detail and t_event_detail != "" %}
                <div class="pub-meta">
                  {% if t_event and t_event != "" %}
                    <span class="pub-venue">{{ t_event }}</span>
                  {% endif %}
                  {% if t_event_detail and t_event_detail != "" %}
                    {% if t_event and t_event != "" %}
                      <span class="pub-sep"> &middot; </span>
                    {% endif %}
                    <span class="pub-venue-detail">{{ t_event_detail }}</span>
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
            {% assign p_title = p["ko-title"] | default: p.title %}
            {% assign p_authors = p["ko-authors"] | default: p.authors %}
            {% assign p_venue = p["ko-venue"] | default: p.venue %}
            {% assign p_venue_detail = p["ko-venue_detail"] | default: p.venue_detail %}
            <li class="pub-item">
              <div class="pub-title-line">
                {% if p.title_url and p.title_url != "" %}
                  <a class="pub-title" href="{{ p.title_url }}" target="_blank" rel="noopener">{{ p_title }}</a>
                {% else %}
                  <span class="pub-title">{{ p_title }}</span>
                {% endif %}
              </div>

              {% if p_authors and p_authors != "" %}
                <div class="pub-authors">{{ p_authors }}</div>
              {% endif %}

              {% if p_venue and p_venue != "" or p_venue_detail and p_venue_detail != "" %}
                <div class="pub-meta">
                  {% if p_venue and p_venue != "" %}
                    <span class="pub-venue">{{ p_venue }}</span>
                  {% endif %}
                  {% if p_venue_detail and p_venue_detail != "" %}
                    {% if p_venue and p_venue != "" %}
                      <span class="pub-sep"> &middot; </span>
                    {% endif %}
                    <span class="pub-venue-detail">{{ p_venue_detail }}</span>
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
            {% assign p_title = p["ko-title"] | default: p.title %}
            {% assign p_authors = p["ko-authors"] | default: p.authors %}
            {% assign p_venue = p["ko-venue"] | default: p.venue %}
            {% assign p_venue_detail = p["ko-venue_detail"] | default: p.venue_detail %}
            <li class="pub-item">
              <div class="pub-title-line">
                {% if p.title_url and p.title_url != "" %}
                  <a class="pub-title" href="{{ p.title_url }}" target="_blank" rel="noopener">{{ p_title }}</a>
                {% else %}
                  <span class="pub-title">{{ p_title }}</span>
                {% endif %}
              </div>

              {% if p_authors and p_authors != "" %}
                <div class="pub-authors">{{ p_authors }}</div>
              {% endif %}

              {% if p_venue and p_venue != "" or p_venue_detail and p_venue_detail != "" %}
                <div class="pub-meta">
                  {% if p_venue and p_venue != "" %}
                    <span class="pub-venue">{{ p_venue }}</span>
                  {% endif %}
                  {% if p_venue_detail and p_venue_detail != "" %}
                    {% if p_venue and p_venue != "" %}
                      <span class="pub-sep"> &middot; </span>
                    {% endif %}
                    <span class="pub-venue-detail">{{ p_venue_detail }}</span>
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

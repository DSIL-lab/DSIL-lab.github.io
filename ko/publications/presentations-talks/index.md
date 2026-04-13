---
layout: page
title: Presentations & Talks
permalink: /ko/publications/presentations-talks/
---

<ul>
  <li><a href="{{ '/ko/publications/presentations-talks/invited-talks/' | relative_url }}">Invited Talks</a></li>
  <li><a href="{{ '/ko/publications/presentations-talks/international-conferences/' | relative_url }}">International Conferences</a></li>
  <li><a href="{{ '/ko/publications/presentations-talks/domestic-conferences/' | relative_url }}">Domestic Conferences</a></li>
</ul>

{% assign talks_all = site.publications | where_exp: "p", "p.type contains 'invited'" %}
{% assign talk_years = talks_all | map: "year" | uniq | sort | reverse %}

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

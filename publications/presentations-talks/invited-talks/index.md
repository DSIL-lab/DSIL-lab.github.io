---
layout: page
title: Invited Talks
permalink: /publications/presentations-talks/invited-talks/
---

{% assign items_all = site.publications | where_exp: "p", "p.type == 'invited_talk' or p.type == 'invited-talk' or p.type contains 'invited-talk' or p.type contains 'invited_talk'" %}
{% assign years = items_all | map: "year" | uniq | sort | reverse %}

<section class="pub-section">
  <h2 class="pub-section-title">Invited Talks</h2>

  {% if items_all.size == 0 %}
    <p>No invited talks yet.</p>
  {% else %}
    {% for y in years %}
      <div class="pub-year-block">
        <h3 class="pub-year">{{ y }}</h3>

        {% assign items = items_all | where: "year", y | sort: "pub-id" | reverse %}
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
                <div class="pub-meta"><span class="pub-venue">{{ t.event }}</span></div>
              {% endif %}
            </li>
          {% endfor %}
        </ol>
      </div>
    {% endfor %}
  {% endif %}
</section>

---
layout: page
title: Patents
permalink: /publications/patents/
---

{% assign items_all = site.publications | where_exp: "p", "p.type contains 'patent'" %}
{% assign years = items_all | map: "year" | uniq | sort | reverse %}

<section class="pub-section">
  <h2 class="pub-section-title">Patents</h2>

  {% if items_all.size == 0 %}
    <p>No patent records yet.</p>
  {% else %}
      {% assign patent_display_id = items_all.size | plus: 0 %}
    {% for y in years %}
      <div class="pub-year-block">
        <h3 class="pub-year">{{ y }}</h3>

        {% assign items = items_all | where: "year", y | sort: "pub-id" | reverse %}
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
  {% endif %}
</section>

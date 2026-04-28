---
layout: page
title: Alumni
---

{% assign alumni_all = site.alumni | sort: "order" %}
{% assign regular_alumni = alumni_all | where: "alumni_type", "regular" %}
{% assign intern_alumni = alumni_all | where: "alumni_type", "intern" %}

<section class="pub-section alumni-list-view">
  <h2 class="pub-section-title">Alumni</h2>

  {% if regular_alumni.size == 0 %}
    <p>No regular alumni information found yet.</p>
  {% else %}
    <ol class="pub-list">
      {% for a in regular_alumni %}
        <li class="pub-item alumni-item">
          <div class="pub-title-line">
            <span class="pub-title">{{ a.name }}</span>
          </div>

          {% assign primary_role = "" %}
          {% if a.lab_roles and a.lab_roles.size > 0 %}
            {% assign primary_role = a.lab_roles[0] %}
          {% endif %}

          {% if a.lab_period or primary_role != "" %}
            <div class="pub-meta">
              {% if a.lab_period and a.lab_period != "" %}{{ a.lab_period }}{% endif %}{% if a.lab_period and a.lab_period != "" and primary_role != "" %}, {% endif %}{% if primary_role != "" %}{{ primary_role }}{% endif %}
            </div>
          {% endif %}

          {% if a.lab_roles and a.lab_roles.size > 1 %}
            <ul class="alumni-role-list">
              {% for role in a.lab_roles offset: 1 %}
                <li>{{ role }}</li>
              {% endfor %}
            </ul>
          {% endif %}

          {% if a.current_affiliation and a.current_affiliation != "" %}
            <div class="pub-meta alumni-current-line"><strong>Current:</strong> {{ a.current_affiliation }}</div>
          {% endif %}

          <p class="see-more alumni-see-more">
            <a class="see-more-link" href="{{ a.url | relative_url }}">See more...</a>
          </p>
        </li>
      {% endfor %}
    </ol>
  {% endif %}
</section>

<section class="pub-section alumni-list-view">
  <h2 class="pub-section-title">Intern</h2>

  {% if intern_alumni.size == 0 %}
    <p>No intern alumni information found yet.</p>
  {% else %}
    <ol class="pub-list">
      {% for a in intern_alumni %}
        <li class="pub-item alumni-item">
          <div class="pub-title-line">
            <span class="pub-title">{{ a.name }}</span>
          </div>

          {% assign primary_role = "" %}
          {% if a.lab_roles and a.lab_roles.size > 0 %}
            {% assign primary_role = a.lab_roles[0] %}
          {% endif %}

          {% if a.lab_period or primary_role != "" %}
            <div class="pub-meta">
              {% if a.lab_period and a.lab_period != "" %}{{ a.lab_period }}{% endif %}{% if a.lab_period and a.lab_period != "" and primary_role != "" %}, {% endif %}{% if primary_role != "" %}{{ primary_role }}{% endif %}
            </div>
          {% endif %}

          {% if a.lab_roles and a.lab_roles.size > 1 %}
            <ul class="alumni-role-list">
              {% for role in a.lab_roles offset: 1 %}
                <li>{{ role }}</li>
              {% endfor %}
            </ul>
          {% endif %}

          {% if a.current_affiliation and a.current_affiliation != "" %}
            <div class="pub-meta alumni-current-line"><strong>Current:</strong> {{ a.current_affiliation }}</div>
          {% endif %}
        </li>
      {% endfor %}
    </ol>
  {% endif %}
</section>
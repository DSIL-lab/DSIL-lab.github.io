---
layout: page
title: Principal Investigator
permalink: /ko/people/pi/
---

{% assign pi = site.members | where: "group", "pi" | sort: "order" | first %}
{% assign pi_name = pi["ko-name"] | default: pi.name %}
{% assign pi_role = pi["ko-role"] | default: pi.role %}
{% assign pi_career = pi["ko-career"] | default: pi.career %}
{% assign pi_activities = pi["ko-activities"] | default: pi.activities %}
{% assign pi_awards = pi["ko-awards"] | default: pi.awards %}
{% assign pi_education = pi["ko-education"] | default: pi.education %}

{% if pi %}

<div class="pi-profile">

  <div class="pi-header">
    <img class="pi-photo" src="{{ pi.photo | relative_url }}" alt="{{ pi_name }}">
    <div class="pi-basic">
      <h1 class="pi-name">{{ pi_name }}</h1>
      <div class="pi-role">{{ pi_role }}</div>
      {% if pi.email %}
        <div class="pi-email">{{ pi.email }}</div>
      {% endif %}
      <div class="pi-links">
        {% if pi.scholar %}
          <a href="{{ pi.scholar }}" target="_blank" rel="noopener">Google Scholar</a>
        {% endif %}
      </div>
    </div>
  </div>

  {% if pi_career %}
  <section>
    <h2>Career</h2>
    <ul>
      {% for c in pi_career %}
        <li>{{ c }}</li>
      {% endfor %}
    </ul>
  </section>
  {% endif %}

  {% if pi_activities %}
  <section>
    <h2>Professional Activities</h2>
    <ul>
      {% for a in pi_activities %}
        <li>{{ a }}</li>
      {% endfor %}
    </ul>
  </section>
  {% endif %}

  {% if pi_awards %}
  <section>
    <h2>Awards & Honors</h2>
    <ul>
      {% for a in pi_awards %}
        <li>{{ a }}</li>
      {% endfor %}
    </ul>
  </section>
  {% endif %}

  {% if pi_education %}
  <section>
    <h2>Education</h2>
    <ul>
      {% for e in pi_education %}
        <li>{{ e }}</li>
      {% endfor %}
    </ul>
  </section>
  {% endif %}

</div>

{% else %}
<p>No PI information found.</p>
{% endif %}

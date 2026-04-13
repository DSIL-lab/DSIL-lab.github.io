---
layout: page
title: Principal Investigator
---

{% assign pi = site.members | where: "group", "pi" | sort: "order" | first %}

{% if pi %}

<div class="pi-profile">

  <div class="pi-header">
    <img class="pi-photo" src="{{ pi.photo | relative_url }}" alt="{{ pi.name }}">
    <div class="pi-basic">
      <h1 class="pi-name">{{ pi.name }}</h1>
      <div class="pi-role">{{ pi.role }}</div>
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

  {% if pi.career %}
  <section>
    <h2>Career</h2>
    <ul>
      {% for c in pi.career %}
        <li>{{ c }}</li>
      {% endfor %}
    </ul>
  </section>
  {% endif %}

  {% if pi.activities %}
  <section>
    <h2>Professional Activities</h2>
    <ul>
      {% for a in pi.activities %}
        <li>{{ a }}</li>
      {% endfor %}
    </ul>
  </section>
  {% endif %}

  {% if pi.awards %}
  <section>
    <h2>Awards & Honors</h2>
    <ul>
      {% for a in pi.awards %}
        <li>{{ a }}</li>
      {% endfor %}
    </ul>
  </section>
  {% endif %}

  {% if pi.education %}
  <section>
    <h2>Education</h2>
    <ul>
      {% for e in pi.education %}
        <li>{{ e }}</li>
      {% endfor %}
    </ul>
  </section>
  {% endif %}

</div>

{% else %}
<p>No PI information found.</p>
{% endif %}
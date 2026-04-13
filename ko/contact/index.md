---
layout: page
title: Contact
permalink: /ko/contact/
---

{% assign contact_intro_page = site.pages | where: "path", "ko/contact-content.md" | first %}
{% assign contact_roles = site.contact | sort: "order" %}

<section class="contact-intro">
  {% if contact_intro_page %}
    <div class="contact-intro-body">{{ contact_intro_page.content | markdownify }}</div>
  {% endif %}
</section>

<section class="contact-positions" aria-label="Recruiting positions">
  <h2 class="contact-positions-title">Open Roles</h2>

  <div class="contact-position-list">
    {% for pos in contact_roles %}
      <article class="contact-position-card">
        <a class="contact-position-link" href="{{ pos.url | relative_url }}">
          <h3 class="contact-position-name">{{ pos.title | default: pos.position }}</h3>
          <p class="contact-position-team">{{ pos.team }}</p>
          <div class="contact-position-summary">{{ pos.summary | default: pos.excerpt | markdownify }}</div>
        </a>
      </article>
    {% endfor %}
  </div>
</section>

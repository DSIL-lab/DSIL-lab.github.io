---
layout: page
title: Gallery
---

{% assign gallery_files = site.static_files | where_exp: "f", "f.path contains '/assets/img/gallery/'" | sort: "modified_time" | reverse %}

{% if gallery_files.size > 0 %}
<div class="gallery-grid">
  {% for file in gallery_files %}
    {% assign ext = file.extname | downcase %}
    {% if ext == '.jpg' or ext == '.jpeg' or ext == '.png' or ext == '.webp' or ext == '.gif' %}
    <figure class="gallery-card">
      <a href="{{ file.path | relative_url }}" target="_blank" rel="noopener">
        <img src="{{ file.path | relative_url }}" alt="Gallery image {{ forloop.index }}" class="gallery-image">
      </a>
    </figure>
    {% endif %}
  {% endfor %}
</div>
{% else %}
<p class="gallery-empty">No gallery images yet. Add image files to assets/img/gallery.</p>
{% endif %}
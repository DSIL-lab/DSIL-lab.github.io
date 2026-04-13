---
layout: page
title: Gallery
permalink: /ko/people/gallery/
---

{% assign gallery_files = site.static_files | where_exp: "f", "f.path contains '/assets/img/gallery/'" | where_exp: "f", "f.extname == '.jpg' or f.extname == '.jpeg' or f.extname == '.png' or f.extname == '.webp' or f.extname == '.gif'" | sort: "modified_time" | reverse %}

{% if gallery_files.size > 0 %}
<div class="gallery-grid">
  {% for file in gallery_files %}
    <figure class="gallery-card">
      <a href="{{ file.path | relative_url }}" target="_blank" rel="noopener">
        <img src="{{ file.path | relative_url }}" alt="Gallery image {{ forloop.index }}" class="gallery-image">
      </a>
    </figure>
  {% endfor %}
</div>
{% else %}
<p class="gallery-empty">아직 갤러리 이미지가 없습니다. assets/img/gallery 폴더에 이미지를 추가하세요.</p>
{% endif %}

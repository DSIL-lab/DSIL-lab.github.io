---
layout: page
title: Facilities
permalink: /facilities/
---

{% capture facilities_markdown %}{% include facilities-content.md %}{% endcapture %}

<div class="page-facilities">
{{ facilities_markdown | markdownify }}
</div>
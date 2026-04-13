---
layout: page
title: People
permalink: /ko/people/
---

{% assign members_sorted = site.members | where_exp: "m", "m.group == 'pi' or m.group == 'students'" | sort: "order" %}

<div class="people-wrap">

  <div id="member-detail" class="people-detail">
    <p>Loading...</p>
  </div>

  <div class="people-grid">
    {% for m in members_sorted %}
      {% assign display_name = m["ko-name"] | default: m.name %}
      {% assign display_role = m["ko-role"] | default: m.role %}
      <button
        type="button"
        class="member-card a4-card"
        data-member='{{ m | jsonify | escape }}'
        data-photo='{{ m.photo | relative_url }}'
        onclick="showMember(this)"
      >
        {% if m.photo %}
          <img class="member-card-photo a4-photo" src="{{ m.photo | relative_url }}" alt="{{ display_name }}">
        {% endif %}
        <div class="member-card-text a4-text">
          <div class="member-card-name">{{ display_name }}</div>
          <div class="member-card-role">{{ display_role }}</div>
        </div>
      </button>
    {% endfor %}
  </div>
</div>

<script>
function escapeHtml(s) {
  return String(s)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function renderInlineHtml(s) {
  return String(s || "");
}

function getKoValue(obj, key) {
  var ko = obj["ko-" + key];
  if (ko === undefined || ko === null) return obj[key];
  if (typeof ko === "string" && ko.trim() === "") return obj[key];
  if (Array.isArray(ko) && ko.length === 0) return obj[key];
  return ko;
}

function renderList(title, items, ulClass, allowHtml) {
  if (!items || items.length === 0) return "";
  var cls = ulClass ? ' class="' + ulClass + '"' : "";
  var html = "<h2>" + escapeHtml(title) + "</h2><ul" + cls + ">";
  for (var i = 0; i < items.length; i++) {
    html += "<li>" + (allowHtml ? renderInlineHtml(items[i]) : escapeHtml(items[i])) + "</li>";
  }
  html += "</ul>";
  return html;
}

function renderResearch(research) {
  if (!research || research.length === 0) return "";
  var html = "<h2>Research</h2>";
  for (var r = 0; r < research.length; r++) {
    var area = research[r]["ko-area"] || research[r].area || "";
    var topics = research[r]["ko-topics"] || research[r].topics || [];
    html += '<div class="detail-research-area">';
    html += '<div class="research-area-title">' + renderInlineHtml(area) + "</div>";
    if (topics.length > 0) {
      html += "<ul>";
      for (var t = 0; t < topics.length; t++) {
        html += "<li>" + renderInlineHtml(topics[t]) + "</li>";
      }
      html += "</ul>";
    }
    html += "</div>";
  }
  return html;
}

function renderLinks(m) {
  var parts = [];
  if (m.scholar) {
    parts.push('<a href="' + escapeHtml(m.scholar) + '" target="_blank" rel="noopener">Google Scholar</a>');
  }
  if (m.linkedin) {
    parts.push('<a href="' + escapeHtml(m.linkedin) + '" target="_blank" rel="noopener">LinkedIn</a>');
  }
  if (parts.length === 0) return "";
  return '<div class="contact-links">' + parts.join(" ") + "</div>";
}

function renderPiExtras(m) {
  if (m.group !== "pi") return "";

  var career = getKoValue(m, "career") || [];

  var html = "";
  if (career.length > 0) {
    html += "<h2>Career</h2><ul>";
    var n = Math.min(2, career.length);
    for (var i = 0; i < n; i++) {
      html += "<li>" + career[i] + "</li>";
    }
    html += "</ul>";
  }

  if (m.email || m.scholar || m.linkedin) {
    html += "<h2>Contact</h2>";
    if (m.email) html += '<p class="contact-email">' + escapeHtml(m.email) + "</p>";
    html += renderLinks(m);
  }

  html += '<p class="see-more"><a class="see-more-link" href="{{ "/ko/people/pi/" | relative_url }}">See more →</a></p>';
  return html;
}

function showMember(btn) {
  var raw = btn.getAttribute("data-member");
  var m = JSON.parse(raw);
  var name = getKoValue(m, "name") || "";
  var role = getKoValue(m, "role") || "";
  var career = getKoValue(m, "career") || [];
  var projects = getKoValue(m, "projects") || [];
  var education = getKoValue(m, "education") || [];
  var research = getKoValue(m, "research") || [];
  var photoUrl = btn.dataset.photo;

  var html = "";
  html += '<div class="detail-layout">';

  if (photoUrl) {
    html += '<img class="detail-photo" src="' + escapeHtml(photoUrl) + '" alt="' + escapeHtml(name) + '">';
  }

  html += '<div class="detail-basic">';
  html += '<div class="detail-name">' + escapeHtml(name) + "</div>";
  if (role) html += '<div class="detail-role">' + escapeHtml(role) + "</div>";
  html += "</div>";

  html += '<div class="detail-body">';

  if (m.group === "pi") {
    html += renderPiExtras(m);
  } else {
    if (career.length > 0) {
      html += "<h2>Career</h2><ul>";
      for (var i = 0; i < career.length; i++) {
        html += "<li>" + renderInlineHtml(career[i]) + "</li>";
      }
      html += "</ul>";

      if (projects.length > 0) {
        for (var j = 0; j < projects.length; j++) {
          html += '<p class="project-inline">*' + renderInlineHtml(projects[j]) + "</p>";
        }
      }
    }

    html += renderList("Education", education, "", true);
    html += renderResearch(research);

    if (m.email || m.scholar || m.linkedin) {
      html += "<h2>Contact</h2>";
      if (m.email) html += '<p class="contact-email">' + escapeHtml(m.email) + "</p>";
      html += renderLinks(m);
    }
  }

  html += "</div>";
  html += "</div>";

  document.getElementById("member-detail").innerHTML = html;
}

document.addEventListener("DOMContentLoaded", function() {
  var first = document.querySelector(".member-card");
  if (first) showMember(first);
});
</script>

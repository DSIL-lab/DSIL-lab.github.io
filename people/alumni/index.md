---
layout: page
title: Alumni
---

{% assign alumni_members = site.members | where: "group", "alumni" | sort: "order" %}

<div class="people-wrap">

	<!-- Detail -->
	<div id="member-detail" class="people-detail">
		{% if alumni_members.size == 0 %}
			<p>No alumni information found yet.</p>
		{% else %}
			<p>Loading...</p>
		{% endif %}
	</div>

	<!-- Cards -->
	<div class="people-grid">
		{% for m in alumni_members %}
			<button
				type="button"
				class="member-card a4-card"
				data-member='{{ m | jsonify | escape }}'
				data-photo='{{ m.photo | relative_url }}'
				onclick="showMember(this)"
			>
				{% if m.photo %}
					<img class="member-card-photo a4-photo" src="{{ m.photo | relative_url }}" alt="{{ m.name }}">
				{% endif %}
				<div class="member-card-text a4-text">
					<div class="member-card-name">{{ m.name }}</div>
					<div class="member-card-role">{{ m.role }}</div>
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
		var area = research[r].area || "";
		var topics = research[r].topics || [];
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

function showMember(btn) {
	var raw = btn.getAttribute("data-member");
	var m = JSON.parse(raw);
	var photoUrl = btn.dataset.photo;

	var html = "";
	html += '<div class="detail-layout">';

	if (photoUrl) {
		html += '<img class="detail-photo" src="' + escapeHtml(photoUrl) + '" alt="' + escapeHtml(m.name || "") + '">';
	}

	html += '<div class="detail-basic">';
	html += '<div class="detail-name">' + escapeHtml(m.name || "") + "</div>";
	if (m.role) html += '<div class="detail-role">' + escapeHtml(m.role) + "</div>";
	html += "</div>";

	html += '<div class="detail-body">';

	if (m.career && m.career.length > 0) {
		html += "<h2>Career</h2><ul>";
		for (var i = 0; i < m.career.length; i++) {
			html += "<li>" + renderInlineHtml(m.career[i]) + "</li>";
		}
		html += "</ul>";

		if (m.projects && m.projects.length > 0) {
			for (var j = 0; j < m.projects.length; j++) {
				html += '<p class="project-inline">*' + renderInlineHtml(m.projects[j]) + "</p>";
			}
		}
	}

	html += renderList("Education", m.education, "", true);
	html += renderResearch(m.research);

	if (m.email || m.scholar || m.linkedin) {
		html += "<h2>Contact</h2>";
		if (m.email) html += '<p class="contact-email">' + escapeHtml(m.email) + "</p>";
		html += renderLinks(m);
	}

	html += "</div>"; // detail-body
	html += "</div>"; // detail-layout

	document.getElementById("member-detail").innerHTML = html;
}

document.addEventListener("DOMContentLoaded", function() {
	var first = document.querySelector(".member-card");
	if (first) showMember(first);
});
</script>
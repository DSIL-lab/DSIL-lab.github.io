var peopleRoot = document.querySelector(".people-wrap");
var siteBaseUrl = peopleRoot ? (peopleRoot.getAttribute("data-base-url") || "") : "";
var piLink = peopleRoot ? (peopleRoot.getAttribute("data-pi-link") || "/people/pi/") : "/people/pi/";
var isKoPage = peopleRoot ? peopleRoot.getAttribute("data-is-ko") === "true" : false;

var labels = {
  current: "Current",
  noMembers: "No members for the selected term.",
  career: "Career",
  education: "Education",
  research: "Research",
  contact: "Contact",
  seeMore: "See more ->"
};

var selectedMemberButton = null;
var activeTerm = "";
var termOptions = [];

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

function getDisplayName(m) {
  if (isKoPage && m["ko-name"]) return m["ko-name"];
  return m.name || "";
}

function getDisplayRole(m) {
  if (isKoPage && m["ko-role"]) return m["ko-role"];
  return m.role || "";
}

function toSiteUrl(path) {
  var p = String(path || "").trim();
  if (!p) return "";
  if (/^(https?:)?\/\//i.test(p) || p.indexOf("data:") === 0) return p;

  if (p.charAt(0) !== "/") p = "/" + p;

  var base = siteBaseUrl;
  if (!base) return p;

  if (base.charAt(0) !== "/") base = "/" + base;
  if (base.length > 1 && base.charAt(base.length - 1) === "/") {
    base = base.slice(0, -1);
  }

  if (p === base || p.indexOf(base + "/") === 0) return p;
  return base + p;
}

function getPhotoForTerm(m, term) {
  if (m && m.photo_by_term && term && m.photo_by_term[term]) {
    return toSiteUrl(m.photo_by_term[term]);
  }

  if (m && m.photo_by_term) {
    var memberTerms = Object.keys(m.photo_by_term).sort(compareTermsDesc);
    if (memberTerms.length > 0) {
      return toSiteUrl(m.photo_by_term[memberTerms[0]]);
    }
  }

  return "";
}

function parseTerm(term) {
  var match = /^(\d{4})-(spring|summer|fall|winter)$/i.exec(String(term || ""));
  if (!match) return null;

  var seasonOrder = {
    spring: 1,
    summer: 2,
    fall: 3,
    winter: 4
  };

  return {
    year: parseInt(match[1], 10),
    season: seasonOrder[match[2].toLowerCase()] || 0
  };
}

function compareTermsDesc(a, b) {
  var ta = parseTerm(a);
  var tb = parseTerm(b);

  if (ta && tb) {
    if (ta.year !== tb.year) return tb.year - ta.year;
    return tb.season - ta.season;
  }

  if (a === b) return 0;
  return a < b ? 1 : -1;
}

function toTitleCaseWords(s) {
  return String(s || "")
    .split(/\s+/)
    .filter(Boolean)
    .map(function(word) {
      return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
    })
    .join(" ");
}

function formatTermLabel(term) {
  var parsed = parseTerm(term);
  if (parsed) {
    var seasonName = {
      1: "Spring",
      2: "Summer",
      3: "Fall",
      4: "Winter"
    }[parsed.season] || "Term";
    return seasonName + " " + parsed.year;
  }

  return toTitleCaseWords(String(term || "").replaceAll("-", " "));
}

function collectTerms() {
  var terms = [];
  var seen = {};
  var cards = document.querySelectorAll(".member-card");

  for (var i = 0; i < cards.length; i++) {
    var m = JSON.parse(cards[i].getAttribute("data-member") || "{}");
    if (Array.isArray(m.terms)) {
      for (var j = 0; j < m.terms.length; j++) {
        var listedTerm = String(m.terms[j] || "").trim();
        if (listedTerm && !seen[listedTerm]) {
          seen[listedTerm] = true;
          terms.push(listedTerm);
        }
      }
    }

    if (m.photo_by_term) {
      for (var term in m.photo_by_term) {
        if (Object.prototype.hasOwnProperty.call(m.photo_by_term, term) && !seen[term]) {
          seen[term] = true;
          terms.push(term);
        }
      }
    }
  }

  terms.sort(compareTermsDesc);
  return terms;
}

function closeTermMenu() {
  var picker = document.getElementById("people-term-picker");
  var trigger = document.getElementById("photo-term-trigger");
  var menu = document.getElementById("photo-term-menu");
  if (!picker || !trigger || !menu) return;

  picker.classList.remove("is-open");
  trigger.setAttribute("aria-expanded", "false");
  menu.hidden = true;
}

function openTermMenu() {
  var picker = document.getElementById("people-term-picker");
  var trigger = document.getElementById("photo-term-trigger");
  var menu = document.getElementById("photo-term-menu");
  if (!picker || !trigger || !menu) return;

  picker.classList.add("is-open");
  trigger.setAttribute("aria-expanded", "true");
  menu.hidden = false;
}

function renderTermMenuOptions() {
  var menu = document.getElementById("photo-term-menu");
  if (!menu) return;

  menu.innerHTML = "";

  for (var i = 0; i < termOptions.length; i++) {
    var term = termOptions[i];
    var option = document.createElement("button");
    option.type = "button";
    option.className = "people-term-option";
    option.setAttribute("role", "option");
    option.setAttribute("data-term", term);
    option.textContent = formatTermLabel(term);

    option.addEventListener("click", function() {
      var selected = this.getAttribute("data-term") || "";
      if (selected !== activeTerm) {
        activeTerm = selected;
        refreshView();
      }
      syncTermSelectorUI();
      closeTermMenu();
    });

    menu.appendChild(option);
  }
}

function syncTermSelectorUI() {
  var trigger = document.getElementById("photo-term-trigger");
  var label = document.getElementById("photo-term-label");
  var options = document.querySelectorAll(".people-term-option");

  if (label) {
    label.textContent = activeTerm ? formatTermLabel(activeTerm) : labels.current;
  }

  if (trigger) {
    if (termOptions.length === 0) {
      trigger.disabled = true;
      trigger.classList.add("is-disabled");
    } else {
      trigger.disabled = false;
      trigger.classList.remove("is-disabled");
    }
  }

  for (var i = 0; i < options.length; i++) {
    var isActive = options[i].getAttribute("data-term") === activeTerm;
    options[i].classList.toggle("is-active", isActive);
    options[i].setAttribute("aria-selected", isActive ? "true" : "false");
  }
}

function initTermSelector() {
  var picker = document.getElementById("people-term-picker");
  var trigger = document.getElementById("photo-term-trigger");
  var menu = document.getElementById("photo-term-menu");
  if (!picker || !trigger || !menu) return;

  termOptions = collectTerms();

  if (termOptions.length === 0) {
    activeTerm = "";
    renderTermMenuOptions();
    syncTermSelectorUI();
    closeTermMenu();
    return;
  }

  activeTerm = termOptions[0];

  renderTermMenuOptions();
  syncTermSelectorUI();
  closeTermMenu();

  trigger.addEventListener("click", function() {
    if (trigger.disabled) return;
    if (picker.classList.contains("is-open")) {
      closeTermMenu();
    } else {
      openTermMenu();
    }
  });

  document.addEventListener("click", function(e) {
    if (!picker.contains(e.target)) {
      closeTermMenu();
    }
  });

  document.addEventListener("keydown", function(e) {
    if (e.key === "Escape") {
      closeTermMenu();
    }
  });
}

function isMemberActiveForTerm(m, term) {
  if (!term) return true;
  if (!m) return false;

  if (Array.isArray(m.terms) && m.terms.length > 0) {
    for (var i = 0; i < m.terms.length; i++) {
      if (String(m.terms[i] || "").trim() === term) return true;
    }
    return false;
  }

  return true;
}

function updateMemberVisibility() {
  var cards = document.querySelectorAll(".member-card");

  for (var i = 0; i < cards.length; i++) {
    var btn = cards[i];
    var m = JSON.parse(btn.getAttribute("data-member") || "{}");
    var isActive = isMemberActiveForTerm(m, activeTerm);
    btn.style.display = isActive ? "" : "none";

    if (!isActive && selectedMemberButton === btn) {
      selectedMemberButton = null;
    }
  }
}

function findFirstVisibleMemberCard() {
  var cards = document.querySelectorAll(".member-card");
  for (var i = 0; i < cards.length; i++) {
    if (cards[i].style.display !== "none") return cards[i];
  }
  return null;
}

function renderNoMemberMessage() {
  var detail = document.getElementById("member-detail");
  if (!detail) return;
  detail.innerHTML = "<p>" + labels.noMembers + "</p>";
}

function refreshView() {
  updateMemberVisibility();
  updateCardPhotos();

  if (selectedMemberButton && selectedMemberButton.style.display !== "none") {
    showMember(selectedMemberButton);
    return;
  }

  var firstVisible = findFirstVisibleMemberCard();
  if (firstVisible) {
    showMember(firstVisible);
  } else {
    renderNoMemberMessage();
  }
}

function updateCardPhotos() {
  var cards = document.querySelectorAll(".member-card");

  for (var i = 0; i < cards.length; i++) {
    var btn = cards[i];
    var m = JSON.parse(btn.getAttribute("data-member") || "{}");
    var photoUrl = getPhotoForTerm(m, activeTerm);
    var img = btn.querySelector(".member-card-photo");

    if (!img) continue;

    if (photoUrl) {
      img.src = photoUrl;
      img.style.display = "";
    } else {
      img.removeAttribute("src");
      img.style.display = "none";
    }
  }
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
  var html = "<h2>" + labels.research + "</h2>";
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

function renderPiExtras(m) {
  if (m.group !== "pi") return "";

  var html = "";
  if (m.career && m.career.length > 0) {
    html += "<h2>" + labels.career + "</h2><ul>";
    var n = Math.min(2, m.career.length);
    for (var i = 0; i < n; i++) {
      html += "<li>" + m.career[i] + "</li>";
    }
    html += "</ul>";
  }

  if (m.email || m.scholar || m.linkedin) {
    html += "<h2>" + labels.contact + "</h2>";
    if (m.email) html += '<p class="contact-email">' + escapeHtml(m.email) + "</p>";
    html += renderLinks(m);
  }

  html += '<p class="see-more"><a class="see-more-link" href="' + piLink + '">' + labels.seeMore + "</a></p>";
  return html;
}

function showMember(btn) {
  selectedMemberButton = btn;

  var raw = btn.getAttribute("data-member");
  var m = JSON.parse(raw);
  var photoUrl = getPhotoForTerm(m, activeTerm);

  var html = "";
  html += '<div class="detail-layout">';

  if (photoUrl) {
    html += '<img class="detail-photo" src="' + escapeHtml(photoUrl) + '" alt="' + escapeHtml(getDisplayName(m) || "") + '">';
  }

  html += '<div class="detail-basic">';
  html += '<div class="detail-name">' + escapeHtml(getDisplayName(m) || "") + "</div>";
  if (getDisplayRole(m)) html += '<div class="detail-role">' + escapeHtml(getDisplayRole(m)) + "</div>";
  html += "</div>";

  html += '<div class="detail-body">';

  if (m.group === "pi") {
    html += renderPiExtras(m);
  } else {
    if (m.career && m.career.length > 0) {
      html += "<h2>" + labels.career + "</h2><ul>";
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

    html += renderList(labels.education, m.education, "", true);
    html += renderResearch(m.research);

    if (m.email || m.scholar || m.linkedin) {
      html += "<h2>" + labels.contact + "</h2>";
      if (m.email) html += '<p class="contact-email">' + escapeHtml(m.email) + "</p>";
      html += renderLinks(m);
    }
  }

  html += "</div>";
  html += "</div>";

  document.getElementById("member-detail").innerHTML = html;
}

document.addEventListener("DOMContentLoaded", function() {
  initTermSelector();
  refreshView();
});

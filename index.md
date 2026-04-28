---
layout: default
title: Home
---

<!--
	HOME HERO SETTINGS
	- Slider images live in: assets/img/home/
	- All right-side text (including headings) lives in: home-content.md
-->
{% capture hero_content_markdown %}{% include_relative home-content.md %}{% endcapture %}
{% assign _home_all = site.static_files | where_exp: "f", "f.path contains '/assets/img/home/'" %}
{% assign home_slides = _home_all | where_exp: "f", "f.extname != '.md'" | sort: "name" | reverse %}

<!--
	NEWS SETTINGS
	- home_news_limit: Number of latest news items to show (recommended: 1 or 2).
	- home_news_excerpt_words: Preview text length for each news card.
	- News image field (optional): add `image: /path/to/image.jpg` in each file under _news.
-->
{% assign home_news_limit = 2 %}
{% assign home_news_excerpt_words = 30 %}
{% assign home_join_excerpt_words = 24 %}
{% assign contact_intro_page = site.pages | where: "path", "contact-content.md" | first %}
{% assign popup_roles = site.contact | sort: "order" %}

<section class="home-hero" aria-label="Lab introduction">
	<div class="home-hero-media">
		<div class="home-slider" id="home-slider">
			<div class="home-slider-track" id="home-slider-track">
				{% for slide in home_slides %}
				<div class="home-slider-slide">
					<img src="{{ slide.path | relative_url }}" alt="{{ slide.basename }}" class="home-hero-image">
				</div>
				{% endfor %}
			</div>
			<button class="home-slider-btn home-slider-prev" id="home-slider-prev" aria-label="Previous image">
				<span class="material-icons">arrow_back_ios</span>
			</button>
			<button class="home-slider-btn home-slider-next" id="home-slider-next" aria-label="Next image">
				<span class="material-icons">arrow_forward_ios</span>
			</button>
			<div class="home-slider-dots" id="home-slider-dots" aria-hidden="true"></div>
		</div>
	</div>

	<div class="home-hero-content">
		<div class="home-intro home-intro-preview" id="home-intro-preview">{{ hero_content_markdown | markdownify }}</div>
	</div>
</section>

<div class="home-intro home-intro-continuation" id="home-intro-continuation" hidden></div>

<section class="home-news" aria-label="Latest news">
	<div class="home-section-head">
		<h2 class="home-section-title">Latest News</h2>
		<a class="home-section-link" href="{{ '/news/' | relative_url }}">View all</a>
	</div>

	<div class="home-news-list">
		{% assign latest_news = site.news | sort: 'date' | reverse %}
		{% for item in latest_news limit: home_news_limit %}
			{% assign home_image = item.image | to_s | strip | replace: '\\', '/' %}
			{% assign home_summary_raw = item.summary | to_s | strip %}
			{% if home_summary_raw == '' %}
				{% assign home_summary_html = item.excerpt %}
			{% else %}
				{% assign home_summary_html = home_summary_raw | markdownify %}
			{% endif %}
			<article class="home-news-card{% if home_image != '' %} has-image{% endif %}">
				{% if home_image != '' %}
					<div class="home-news-media">
						<img src="{{ home_image | relative_url }}" alt="{{ item.title }}" class="home-news-image">
					</div>
				{% endif %}

				<div class="home-news-content">
					<div class="home-news-head">
						<h3 class="home-news-title"><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
						<p class="home-news-date">{{ item.date | date: "%b %d, %Y" }}</p>
					</div>
					<div class="home-news-excerpt">{{ home_summary_html }}</div>
				</div>
			</article>
		{% endfor %}
	</div>
</section>

<section class="home-join" aria-label="Join us opportunities">
	<div class="home-section-head">
		<h2 class="home-section-title">Join Us</h2>
		<a class="home-section-link" href="{{ '/contact/' | relative_url }}">View all</a>
	</div>

	{% if popup_roles.size > 0 %}
		<div class="home-join-slider" role="list">
			{% for role in popup_roles %}
				{% assign join_summary_raw = role.summary | default: role.excerpt %}
				{% assign join_summary_compact = join_summary_raw | markdownify | strip_html | strip_newlines | truncatewords: home_join_excerpt_words %}
				<article class="home-join-card" role="listitem">
					<div class="home-join-card-body">
						<h3 class="home-join-card-title">{{ role.title }}</h3>
						<p class="home-join-card-team">{{ role.team }}</p>
						<p class="home-join-card-summary">{{ join_summary_compact }}</p>
					</div>
					<p class="home-join-card-actions">
						<a class="home-join-more" href="{{ role.url | relative_url }}">More</a>
					</p>
				</article>
			{% endfor %}
		</div>
	{% else %}
		<p class="home-join-empty">Recruitment openings will be posted soon.</p>
	{% endif %}
</section>

<div class="home-recruit-modal" id="home-recruit-modal" aria-hidden="true">
	<div class="home-recruit-backdrop" data-modal-close="true"></div>
	<div class="home-recruit-dialog" role="dialog" aria-modal="true" aria-labelledby="home-recruit-title">
		<div class="home-recruit-topbar">
			<button class="home-recruit-close" type="button" id="home-recruit-close" aria-label="Close">
				×
			</button>

			<h2 class="home-recruit-title" id="home-recruit-title">We are looking for highly motivated students</h2>
		</div>

		<div class="home-recruit-body">

		{% if contact_intro_page %}
			<div class="home-recruit-intro">{{ contact_intro_page.content | markdownify }}</div>
		{% endif %}

		<div class="home-recruit-roles">
			<h5 class="home-recruit-roles-title">Open Roles</h5>
			<div class="home-recruit-role-list">
				{% for role in popup_roles %}
					{% assign role_summary_raw = role.summary | default: role.excerpt %}
					{% assign role_summary_compact = role_summary_raw | markdownify | strip_html | strip_newlines | truncatewords: 20 %}
					<article class="home-recruit-role-item">
						<p class="home-recruit-role-name">{{ role.title }}</p>
						<p class="home-recruit-role-team">{{ role.team }}</p>
						<p class="home-recruit-role-summary">{{ role_summary_compact }}</p>
					</article>
				{% endfor %}
			</div>
		</div>
		</div>

		<p class="home-recruit-cta-wrap">
			<button class="home-recruit-hide-today" type="button" id="home-recruit-hide-today">Do not show again today</button>
			<a class="home-recruit-cta" href="{{ '/contact/' | relative_url }}">See full details on Contact page</a>
		</p>
	</div>
</div>

<script>
document.addEventListener("DOMContentLoaded", function() {
	var introPreview = document.getElementById("home-intro-preview");
	var introContinuation = document.getElementById("home-intro-continuation");
	var heroMedia = document.querySelector(".home-hero-media");
	var heroSection = document.querySelector(".home-hero");

	function splitBlockByWords(block, preview, continuation, maxHeight) {
		if (!block || block.nodeType !== Node.ELEMENT_NODE) return false;

		var tag = (block.tagName || "").toUpperCase();
		var canSplitTag = tag === "P" || tag === "LI" || tag === "DIV";
		if (!canSplitTag || block.children.length > 0) return false;

		var fullText = (block.textContent || "").trim();
		if (!fullText) return false;

		var words = fullText.split(/\s+/);
		if (words.length < 3) return false;

		var low = 1;
		var high = words.length - 1;
		var best = 0;

		while (low <= high) {
			var mid = Math.floor((low + high) / 2);
			var test = block.cloneNode(false);
			test.textContent = words.slice(0, mid).join(" ");
			preview.appendChild(test);

			var fits = preview.scrollHeight <= maxHeight + 1;
			preview.removeChild(test);

			if (fits) {
				best = mid;
				low = mid + 1;
			} else {
				high = mid - 1;
			}
		}

		if (best <= 0 || best >= words.length) return false;

		var topPart = block.cloneNode(false);
		topPart.textContent = words.slice(0, best).join(" ");

		var bottomPart = block.cloneNode(false);
		bottomPart.textContent = words.slice(best).join(" ");

		preview.appendChild(topPart);
		continuation.replaceChild(bottomPart, block);
		return true;
	}

	function layoutHomeIntro() {
		if (!introPreview || !introContinuation || !heroMedia) return;
		if (!introPreview.dataset.originalHtml) {
			introPreview.dataset.originalHtml = introPreview.innerHTML;
		}

		introPreview.innerHTML = introPreview.dataset.originalHtml;
		introContinuation.innerHTML = "";
		introContinuation.hidden = true;
		if (heroSection) heroSection.classList.remove("has-overflow-content");

		// Mobile already stacks content under image; no split needed.
		if (window.matchMedia("(max-width: 900px)").matches) return;

		var maxHeight = heroMedia.getBoundingClientRect().height;
		if (!maxHeight || introPreview.scrollHeight <= maxHeight + 1) return;

		while (introPreview.lastChild && introPreview.scrollHeight > maxHeight + 1) {
			introContinuation.prepend(introPreview.lastChild);
		}

		// Make the split feel smoother by splitting the first overflow block by words.
		if (introContinuation.firstChild) {
			splitBlockByWords(introContinuation.firstChild, introPreview, introContinuation, maxHeight);
		}

		if (introContinuation.childNodes.length > 0) {
			introContinuation.hidden = false;
			if (heroSection) heroSection.classList.add("has-overflow-content");
		}
	}

	window.addEventListener("resize", layoutHomeIntro);
	window.addEventListener("load", layoutHomeIntro);
	layoutHomeIntro();

	// Home image slider
	var sliderTrack = document.getElementById("home-slider-track");
	var sliderPrev  = document.getElementById("home-slider-prev");
	var sliderNext  = document.getElementById("home-slider-next");
	var dotsContainer = document.getElementById("home-slider-dots");
	if (sliderTrack && dotsContainer) {
		var slides = sliderTrack.querySelectorAll(".home-slider-slide");
		// Sort slides by year + season (most recent first)
		var _seasonNum = { spring: 1, summer: 2, fall: 3, winter: 4 };
		function _slideKey(slide) {
			var src = (slide.querySelector("img") || {}).getAttribute ? slide.querySelector("img").getAttribute("src") : "";
			var base = src.split("/").pop().replace(/\.[^.]+$/, "");
			var m = base.match(/^(\d+)-(spring|summer|fall|winter)/i);
			if (!m) return 0;
			return parseInt(m[1], 10) * 10 + (_seasonNum[m[2].toLowerCase()] || 0);
		}
		var _arr = Array.prototype.slice.call(slides);
		_arr.sort(function(a, b) { return _slideKey(b) - _slideKey(a); });
		_arr.forEach(function(s) { sliderTrack.appendChild(s); });
		slides = sliderTrack.querySelectorAll(".home-slider-slide");
		var currentSlide = 0;
		function goToSlide(n) {
			currentSlide = (n + slides.length) % slides.length;
			sliderTrack.style.transform = "translateX(-" + (currentSlide * 100) + "%)";
			var dots = dotsContainer.querySelectorAll(".home-slider-dot");
			for (var di = 0; di < dots.length; di++) {
				dots[di].classList.toggle("is-active", di === currentSlide);
			}
		}
		if (sliderPrev) sliderPrev.addEventListener("click", function() { goToSlide(currentSlide - 1); });
		if (sliderNext) sliderNext.addEventListener("click", function() { goToSlide(currentSlide + 1); });
		for (var si = 0; si < slides.length; si++) {
			(function(idx) {
				var dot = document.createElement("button");
				dot.className = "home-slider-dot" + (idx === 0 ? " is-active" : "");
				dot.setAttribute("aria-label", "Go to slide " + (idx + 1));
				dot.addEventListener("click", function() { goToSlide(idx); });
				dotsContainer.appendChild(dot);
			})(si);
		}
	}

  var modal = document.getElementById("home-recruit-modal");
  var closeBtn = document.getElementById("home-recruit-close");
	var hideTodayBtn = document.getElementById("home-recruit-hide-today");
	var hideDateKey = "homeRecruitModalHiddenDate";
  if (!modal) return;

	function getTodayStamp() {
		var now = new Date();
		var y = now.getFullYear();
		var m = String(now.getMonth() + 1).padStart(2, "0");
		var d = String(now.getDate()).padStart(2, "0");
		return y + "-" + m + "-" + d;
	}

	function getHiddenDate() {
		try {
			return localStorage.getItem(hideDateKey);
		} catch (err) {
			return null;
		}
	}

	function setHiddenDate(value) {
		try {
			localStorage.setItem(hideDateKey, value);
		} catch (err) {
			// Ignore storage errors (private mode or blocked storage).
		}
	}

  function openModal() {
    modal.classList.add("is-open");
    modal.setAttribute("aria-hidden", "false");
  }

  function closeModal() {
    modal.classList.remove("is-open");
    modal.setAttribute("aria-hidden", "true");
  }

	if (getHiddenDate() !== getTodayStamp()) {
		openModal();
	}

  if (closeBtn) closeBtn.addEventListener("click", closeModal);

	if (hideTodayBtn) {
		hideTodayBtn.addEventListener("click", function() {
			setHiddenDate(getTodayStamp());
			closeModal();
		});
	}

  modal.addEventListener("click", function(e) {
    if (e.target && e.target.getAttribute("data-modal-close") === "true") {
      closeModal();
    }
  });

  document.addEventListener("keydown", function(e) {
    if (e.key === "Escape" && modal.classList.contains("is-open")) {
      closeModal();
    }
  });
});
</script>
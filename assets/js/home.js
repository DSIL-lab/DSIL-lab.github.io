document.addEventListener("DOMContentLoaded", function() {
  var introPreview = document.getElementById("home-intro-preview");
  var introContinuation = document.getElementById("home-intro-continuation");
  var heroMedia = document.querySelector(".home-hero-media");
  var heroSection = document.querySelector(".home-hero");
  var isKo = /^\/ko\//.test(window.location.pathname);

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

    if (window.matchMedia("(max-width: 900px)").matches) return;

    var maxHeight = heroMedia.getBoundingClientRect().height;
    if (!maxHeight || introPreview.scrollHeight <= maxHeight + 1) return;

    while (introPreview.lastChild && introPreview.scrollHeight > maxHeight + 1) {
      introContinuation.prepend(introPreview.lastChild);
    }

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

  var sliderTrack = document.getElementById("home-slider-track");
  var sliderPrev = document.getElementById("home-slider-prev");
  var sliderNext = document.getElementById("home-slider-next");
  var dotsContainer = document.getElementById("home-slider-dots");
  if (sliderTrack && dotsContainer) {
    var slides = sliderTrack.querySelectorAll(".home-slider-slide");
    var seasonNum = { spring: 1, summer: 2, fall: 3, winter: 4 };

    function slideKey(slide) {
      var imageEl = slide.querySelector("img");
      var src = imageEl ? imageEl.getAttribute("src") : "";
      var base = String(src || "").split("/").pop().replace(/\.[^.]+$/, "");
      var match = base.match(/^(\d+)-(spring|summer|fall|winter)/i);
      if (!match) return 0;
      return parseInt(match[1], 10) * 10 + (seasonNum[match[2].toLowerCase()] || 0);
    }

    var sortedSlides = Array.prototype.slice.call(slides);
    sortedSlides.sort(function(a, b) {
      return slideKey(b) - slideKey(a);
    });
    sortedSlides.forEach(function(slide) {
      sliderTrack.appendChild(slide);
    });

    slides = sliderTrack.querySelectorAll(".home-slider-slide");
    var currentSlide = 0;

    function goToSlide(n) {
      currentSlide = (n + slides.length) % slides.length;
      sliderTrack.style.transform = "translateX(-" + (currentSlide * 100) + "%)";
      var dots = dotsContainer.querySelectorAll(".home-slider-dot");
      for (var i = 0; i < dots.length; i++) {
        dots[i].classList.toggle("is-active", i === currentSlide);
      }
    }

    if (sliderPrev) {
      sliderPrev.addEventListener("click", function() {
        goToSlide(currentSlide - 1);
      });
    }

    if (sliderNext) {
      sliderNext.addEventListener("click", function() {
        goToSlide(currentSlide + 1);
      });
    }

    for (var slideIndex = 0; slideIndex < slides.length; slideIndex++) {
      (function(idx) {
        var dot = document.createElement("button");
        dot.className = "home-slider-dot" + (idx === 0 ? " is-active" : "");
        dot.setAttribute("aria-label", isKo ? (idx + 1) + "번 슬라이드" : "Go to slide " + (idx + 1));
        dot.addEventListener("click", function() {
          goToSlide(idx);
        });
        dotsContainer.appendChild(dot);
      })(slideIndex);
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
      // Ignore storage errors.
    }
  }

  function openModal() {
    modal.classList.add("is-open");
    modal.setAttribute("aria-hidden", "false");
    if (isKo) document.body.classList.add("modal-open");
  }

  function closeModal() {
    modal.classList.remove("is-open");
    modal.setAttribute("aria-hidden", "true");
    if (isKo) document.body.classList.remove("modal-open");
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

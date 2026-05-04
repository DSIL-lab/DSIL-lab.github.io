---
layout: default
title: 홈
permalink: /ko/
---

{% capture hero_content_markdown %}{% include_relative home-content.md %}{% endcapture %}
{% assign _home_all = site.static_files | where_exp: "f", "f.path contains '/assets/img/home/'" %}
{% assign home_slides = _home_all | where_exp: "f", "f.extname != '.md'" | sort: "name" | reverse %}

{% assign home_news_limit = 2 %}
{% assign home_news_excerpt_words = 30 %}
{% assign home_join_excerpt_words = 24 %}
{% assign locale_prefix = '/ko' %}
{% assign contact_intro_page = site.pages | where: "path", "ko/contact-content.md" | first %}
{% assign popup_roles = site.contact | sort: "order" %}

<section class="home-hero" aria-label="연구실 소개">
  <div class="home-hero-media">
    <div class="home-slider" id="home-slider">
      <div class="home-slider-track" id="home-slider-track">
        {% for slide in home_slides %}
        <div class="home-slider-slide">
          <img src="{{ slide.path | relative_url }}" alt="{{ slide.basename }}" class="home-hero-image">
        </div>
        {% endfor %}
      </div>
      <button class="home-slider-btn home-slider-prev" id="home-slider-prev" aria-label="이전 이미지">
        <span class="material-icons">arrow_back_ios</span>
      </button>
      <button class="home-slider-btn home-slider-next" id="home-slider-next" aria-label="다음 이미지">
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

<section class="home-news" aria-label="최신 소식">
  <div class="home-section-head">
    <h2 class="home-section-title">최신 뉴스</h2>
    <a class="home-section-link" href="{{ locale_prefix | append: '/news/' | relative_url }}">전체 보기</a>
  </div>

  <div class="home-news-list">
    {% assign latest_news = site.ko_news | sort: 'date' | reverse %}
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
            <p class="home-news-date">{{ item.date | date: "%Y.%m.%d" }}</p>
          </div>
          <div class="home-news-excerpt">{{ home_summary_html }}</div>
        </div>
      </article>
    {% endfor %}
  </div>
</section>

<section class="home-join" aria-label="모집 안내">
  <div class="home-section-head">
    <h2 class="home-section-title">Join Us</h2>
    <a class="home-section-link" href="{{ locale_prefix | append: '/contact/' | relative_url }}">전체 보기</a>
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
    <p class="home-join-empty">현재 공고가 없습니다.</p>
  {% endif %}
</section>

<div class="home-recruit-modal" id="home-recruit-modal" aria-hidden="true">
  <div class="home-recruit-backdrop" data-modal-close="true"></div>
  <div class="home-recruit-dialog" role="dialog" aria-modal="true" aria-labelledby="home-recruit-title">
    <div class="home-recruit-topbar">
      <button class="home-recruit-close" type="button" id="home-recruit-close" aria-label="닫기">
        ×
      </button>

      <h2 class="home-recruit-title" id="home-recruit-title">We are looking for highly motivated students and researchers</h2>
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
      <button class="home-recruit-hide-today" type="button" id="home-recruit-hide-today">오늘 하루 보지 않기</button>
      <a class="home-recruit-cta" href="{{ locale_prefix | append: '/contact/' | relative_url }}">Contact에서 전체 내용 보기</a>
    </p>
  </div>
</div>

<script src="{{ '/assets/js/home.js' | relative_url }}"></script>


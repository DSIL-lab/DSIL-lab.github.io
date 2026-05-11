module DSIL
  class GeneratedNewsPage < Jekyll::PageWithoutAFile
    def initialize(site, base, dir, title, collection)
      super(site, base, dir, "index.html")

      data["layout"] = "page"
      data["title"] = title
      self.content = "{% include news.html collection='#{collection}' %}\n"
    end
  end

  class NewsPagesGenerator < Jekyll::Generator
    safe true
    priority :low

    def generate(site)
      site.pages << GeneratedNewsPage.new(site, site.source, "news", "News", "news")
      site.pages << GeneratedNewsPage.new(site, site.source, File.join("ko", "news"), "News", "ko_news")
    end
  end
end

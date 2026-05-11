module DSIL
  class GeneratedDownloadsPage < Jekyll::PageWithoutAFile
    def initialize(site, base, dir, title)
      super(site, base, dir, "index.html")

      data["layout"] = "page"
      data["title"] = title
      self.content = "{% include downloads.html %}\n"
    end
  end

  class DownloadsPagesGenerator < Jekyll::Generator
    safe true
    priority :low

    def generate(site)
      site.pages << GeneratedDownloadsPage.new(site, site.source, "downloads", "Downloads")
      site.pages << GeneratedDownloadsPage.new(site, site.source, File.join("ko", "downloads"), "Downloads")
    end
  end
end

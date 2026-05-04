module DSIL
  class GeneratedGalleryPage < Jekyll::PageWithoutAFile
    def initialize(site, base, dir, title)
      super(site, base, dir, "index.html")

      data["layout"] = "page"
      data["title"] = title
      self.content = "{% include people-gallery.html %}\n"
    end
  end

  class GalleryPagesGenerator < Jekyll::Generator
    safe true
    priority :low

    def generate(site)
      site.pages << GeneratedGalleryPage.new(site, site.source, File.join("people", "gallery"), "Gallery")
      site.pages << GeneratedGalleryPage.new(site, site.source, File.join("ko", "people", "gallery"), "Gallery")
    end
  end
end

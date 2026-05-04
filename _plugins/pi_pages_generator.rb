module DSIL
  class GeneratedPiPage < Jekyll::PageWithoutAFile
    def initialize(site, base, dir, title)
      super(site, base, dir, "index.html")

      data["layout"] = "page"
      data["title"] = title
      self.content = "{% include people-pi.html %}\n"
    end
  end

  class PiPagesGenerator < Jekyll::Generator
    safe true
    priority :low

    def generate(site)
      site.pages << GeneratedPiPage.new(site, site.source, File.join("people", "pi"), "Principal Investigator")
      site.pages << GeneratedPiPage.new(site, site.source, File.join("ko", "people", "pi"), "Principal Investigator")
    end
  end
end

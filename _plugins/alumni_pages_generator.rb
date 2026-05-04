module DSIL
  class GeneratedAlumniPage < Jekyll::PageWithoutAFile
    def initialize(site, base, dir, title)
      super(site, base, dir, "index.html")

      data["layout"] = "page"
      data["title"] = title
      self.content = "{% include people-alumni.html %}\n"
    end
  end

  class AlumniPagesGenerator < Jekyll::Generator
    safe true
    priority :low

    def generate(site)
      site.pages << GeneratedAlumniPage.new(site, site.source, File.join("people", "alumni"), "Alumni")
      site.pages << GeneratedAlumniPage.new(site, site.source, File.join("ko", "people", "alumni"), "Alumni")
    end
  end
end

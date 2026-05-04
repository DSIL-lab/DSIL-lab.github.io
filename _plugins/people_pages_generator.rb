module DSIL
  class GeneratedPeoplePage < Jekyll::PageWithoutAFile
    def initialize(site, base, dir, title, is_ko)
      super(site, base, dir, "index.html")

      data["layout"] = "page"
      data["title"] = title
      self.content = "{% include people-member.html %}\n"
    end
  end

  class PeoplePagesGenerator < Jekyll::Generator
    safe true
    priority :low

    def generate(site)
      site.pages << GeneratedPeoplePage.new(site, site.source, "people", "People", false)
      site.pages << GeneratedPeoplePage.new(site, site.source, File.join("ko", "people"), "People", true)
    end
  end
end

module DSIL
  class GeneratedResearchPage < Jekyll::PageWithoutAFile
    def initialize(site, base, dir, title, collection)
      super(site, base, dir, "index.html")

      data["layout"] = "page"
      data["title"] = title
      self.content = "{% include research.html collection='#{collection}' %}\n"
    end
  end

  class ResearchPagesGenerator < Jekyll::Generator
    safe true
    priority :low

    def generate(site)
      site.pages << GeneratedResearchPage.new(site, site.source, "research", "Research", "research")
      site.pages << GeneratedResearchPage.new(site, site.source, File.join("ko", "research"), "Research", "ko_research")
    end
  end
end

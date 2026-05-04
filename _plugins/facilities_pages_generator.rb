module DSIL
  class GeneratedFacilitiesPage < Jekyll::PageWithoutAFile
    def initialize(site, base, dir)
      super(site, base, dir, "index.html")

      data["layout"] = "page"
      data["title"] = "Facilities"
      self.content = <<~LIQUID
        {% capture facilities_markdown %}{% include facilities-content.md %}{% endcapture %}

        <div class="page-facilities">
        {{ facilities_markdown | markdownify }}
        </div>
      LIQUID
    end
  end

  class FacilitiesPagesGenerator < Jekyll::Generator
    safe true
    priority :low

    def generate(site)
      site.pages << GeneratedFacilitiesPage.new(site, site.source, "facilities")
      site.pages << GeneratedFacilitiesPage.new(site, site.source, File.join("ko", "facilities"))
    end
  end
end
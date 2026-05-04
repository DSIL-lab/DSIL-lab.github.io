module DSIL
  class GeneratedContactPage < Jekyll::PageWithoutAFile
    def initialize(site, base, dir, title, intro_source)
      super(site, base, dir, "index.html")

      data["layout"] = "page"
      data["title"] = title
      self.content = "{% include contact-page.html intro_source='#{intro_source}' %}\n"
    end
  end

  class ContactPagesGenerator < Jekyll::Generator
    safe true
    priority :low

    def generate(site)
      site.pages << GeneratedContactPage.new(site, site.source, "contact", "Contact", "contact-content.md")
      site.pages << GeneratedContactPage.new(site, site.source, File.join("ko", "contact"), "Contact", "ko/contact-content.md")
    end
  end
end

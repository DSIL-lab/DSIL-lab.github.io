module DSIL
  class GeneratedPublicationsPage < Jekyll::PageWithoutAFile
    def initialize(site, base, dir, title, include_file)
      super(site, base, dir, "index.html")

      data["layout"] = "page"
      data["title"] = title
      self.content = "{% include #{include_file} %}\n"
    end
  end

  class PublicationsPagesGenerator < Jekyll::Generator
    safe true
    priority :low

    PAGE_SPECS = [
      ["publications", "Publications", "publications.html"],
      ["publications/journal-articles", "Journal Articles", "publications-journal-articles.html"],
      ["publications/conference-proceedings", "Conference Proceedings", "publications-conference-proceedings.html"],
      ["publications/patents", "Patents", "publications-patents.html"],
      ["publications/presentations-talks", "Presentations & Talks", "publications-presentations-talks.html"],
      ["publications/presentations-talks/invited-talks", "Invited Talks", "publications-invited-talks.html"],
      ["publications/presentations-talks/international-conferences", "International Conferences", "publications-international-conferences.html"],
      ["publications/presentations-talks/domestic-conferences", "Domestic Conferences", "publications-domestic-conferences.html"],
      ["ko/publications", "Publications", "publications-ko.html"],
      ["ko/publications/journal-articles", "Journal Articles", "publications-journal-articles.html"],
      ["ko/publications/conference-proceedings", "Conference Proceedings", "publications-conference-proceedings.html"],
      ["ko/publications/patents", "Patents", "publications-patents-ko.html"],
      ["ko/publications/presentations-talks", "Presentations & Talks", "publications-presentations-talks.html"],
      ["ko/publications/presentations-talks/invited-talks", "Invited Talks", "publications-invited-talks.html"],
      ["ko/publications/presentations-talks/international-conferences", "International Conferences", "publications-international-conferences.html"],
      ["ko/publications/presentations-talks/domestic-conferences", "Domestic Conferences", "publications-domestic-conferences.html"]
    ].freeze

    def generate(site)
      PAGE_SPECS.each do |dir, title, include_file|
        site.pages << GeneratedPublicationsPage.new(site, site.source, dir, title, include_file)
      end
    end
  end
end

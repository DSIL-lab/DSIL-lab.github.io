module DSIL
  class AlumniProxyPage < Jekyll::PageWithoutAFile
    def initialize(site, base, dir, alumni_doc)
      super(site, base, dir, "index.html")

      data["alumni_data"] = alumni_doc.data
      data["layout"] = "alumni-member"
      data["title"] = alumni_doc.data["name"].to_s
      data["alumni_name"] = alumni_doc.data["name"].to_s
      data["alumni_ref_id"] = alumni_doc.data["id"].to_s
      self.content = ""
    end
  end

  class KoAlumniGenerator < Jekyll::Generator
    safe true
    priority :low

    def generate(site)
      alumni_collection = site.collections["alumni"]
      return unless alumni_collection

      alumni_collection.docs.each do |doc|
        next unless doc.data["alumni_type"] == "regular"
        id = doc.data["id"].to_s.strip
        next if id.empty?
        
        # Use explicit id-based URLs for alumni detail pages.
        doc.data["alumni_slug"] = id

        en_dir = File.join("people", "alumni", id)
        ko_dir = File.join("ko", "people", "alumni", id)
        site.pages << AlumniProxyPage.new(site, site.source, en_dir, doc)
        site.pages << AlumniProxyPage.new(site, site.source, ko_dir, doc)
      end

    end
  end
end
import scrapy
from urllib.parse import urljoin


class ProgramsSpider(scrapy.Spider):
    name = "programs"
    allowed_domains = ["coursecatalog.benedictine.edu", "quotes.toscrape.com"]
    start_urls = [
        # "https://quotes.toscrape.com/tag/reading/",
        "https://coursecatalog.benedictine.edu/courses-instruction/#programstext",
    ]

    def parse(self, response):
        program_links = response.css("div#programsbycredentialtextcontainer a::attr(href)").getall()

        for href in program_links:
            url = urljoin(response.url, href)  # + "#suggestedsequencestext"
            # print(url)
            # raise SystemExit
            yield scrapy.Request(url, callback=self.parse_program)

    def parse_program(self, response):
        # Dummy function – replace with real logic later
        title = response.css("h1::text").get() or "No title"
        yield {"url": response.url, "title": title.strip()}

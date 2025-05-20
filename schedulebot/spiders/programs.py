import scrapy
from urllib.parse import urljoin

class ProgramsSpider(scrapy.Spider):
    name = "programs"
    allowed_domains = ["coursecatalog.benedictine.edu"]
    start_urls = ["https://coursecatalog.benedictine.edu/courses-instruction/#programstext"]

    def parse(self, response):
        # Extract all links in the #programstext section
        program_section = response.css('#programstext')
        program_links = program_section.css('a::attr(href)').getall()

        for href in program_links:
            url = urljoin(response.url, href)
            yield scrapy.Request(url, callback=self.parse_program)

    def parse_program(self, response):
        # Dummy function – replace with real logic later
        title = response.css('h1::text').get() or "No title"
        yield {
            'url': response.url,
            'title': title.strip()
        }

import scrapy
from ..items import QuotestutorialItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com'
    ]

    def parse(self, response):
        items = QuotestutorialItem()
        all_div_quotes = response.css("div.quote")

        for quote in all_div_quotes:
            title = quote.css("span.text::text").extract()
            author = quote.css("small::text").extract()
            tags = quote.css("a.tag::text").extract()
            items['title'] = title
            items['author'] = author
            items['tags'] = tags
            yield items

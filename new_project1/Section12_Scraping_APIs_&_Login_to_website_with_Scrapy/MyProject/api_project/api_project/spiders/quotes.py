import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/api/quotes?page=1']

    def parse(self, response):
        # Storing the response in json and getting quotes
        json_response = json.loads(response.body)
        quotes = json_response.get('quotes')

        # Looping through quote elements
        for quote in quotes:
            # Return data extracted
            yield {
                'author': quote.get('author').get('name'),
                'tags': quote.get('tags'),
                'quotes': quote.get('text'),
            }

        has_next = json_response.get('has_next')
        if has_next:
            has_next_number = json_response.get('page')+1
            yield scrapy.Request(
                url=f'https://quotes.toscrape.com/api/quotes?page={has_next_number}',
                callback = self.parse
            )
import scrapy


class WorldometersSpider(scrapy.Spider):
    name = "worldometers"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        #title = response.xpath('//h1/text()').get()
        countries = response.xpath('//td/a')

        for country in countries:
            country_name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # absolution_url
            #absolute_url = f'https://www.worldometers.info/{link}'
            #absolute_url = response.urljoin(link)

            # relative_url
            yield response.follow(url=link, callback=self.parse_country, meta={'country':country_name})

    def parse_country(self, response):
        rows = response.xpath('//table[@class="table table-striped table-bordered dataTable no-footer"]/tbody')
        # response.xpath("(//table[contains(@class,'table')/tbody/tr")
        country = response.request.meta['country']
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            pouplation = row.xpath(".//td[3]/strong/text()").get()

            yield {
                'country':country,
                'year':year,
                'population':pouplation
            }

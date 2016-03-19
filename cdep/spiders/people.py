import scrapy
from ..items import PersonItem

class PeopleSpider(scrapy.Spider):
    name = 'people'
    allowed_domains = ['cdep.ro']
    start_urls = ['http://www.cdep.ro/pls/parlam/structura2015.de']

    def parse(self, response):
        for tr in response.css('.grup-parlamentar-list tbody tr'):
            [href] = tr.css('td')[1].css('a::attr(href)').extract()
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse_person)

    def parse_person(self, response):
        item = PersonItem()
        item['name'] = response.css('.stiri-box h1::text').extract_first()
        return item

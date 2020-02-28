# get list of all countries in the world
import scrapy
class QuoteSpider(scrapy.Spider):
    name = 'country'
    start_urls = ['https://www.britannica.com/topic/list-of-countries-1993160']

    def parse(self, response):
        for i in range(326806,326830,1):
            id = "ref"+ str(i)
            countrynames= response.css("section#"+id+" a::text").extract()
            for country in countrynames:
                yield {'country': country}


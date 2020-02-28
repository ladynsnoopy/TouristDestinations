import scrapy
import csv

with open(r'C:\Users\S510\PycharmProjects\ToursitDest\tourdestination\weblinks.csv', newline='') as csvfile:
    weblinks = []
    reader = csv.reader(csvfile)
    for row in reader:
        weblink =str(row[0])
        weblinks.append(weblink)
class QuoteSpider(scrapy.Spider):
    name = 'SampleCountry'
    start_urls = weblinks
    def parse(self, response):
        titles = response.css("div.listing_title.title_with_snippets h2::text").extract()
        for title in titles:
            yield{'attraction': title,'url': response.request.url}
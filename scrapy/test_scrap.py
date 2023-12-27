import scrapy

class FastcampusSpider(scrapy.Spider):
    name = 'fastcampus'
    allowed_domains = ['fastcampus.co.kr']
    start_urls = ['https://fastcampus.co.kr/.api/www/categories/10/page']

    def parse(self, response):
        # Process the JSON response
        data = response.json()
        # You can process the data here (e.g., extract specific fields, save data, etc.)
        yield data

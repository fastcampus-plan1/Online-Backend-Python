# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FastcampusItem(scrapy.Item):
    public_title = scrapy.Field()
    public_description = scrapy.Field()
    keywords = scrapy.Field()
    img = scrapy.Field()

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Category = scrapy.Field() #desc
    Website_name = scrapy.Field() #title
    Website_URL = scrapy.Field() #link
    Website_title = scrapy.Field() #from the <title></title> tag from the external (related to the catalogue parsed) website





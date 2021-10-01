


from scapy.all import *
import scrapy
from ..items import DmozItem 


class DmozSpider(scrapy.Spider):
    name = "dmoz"                   
    allowed_domains = ['http://www.dmoztools.net']     
    start_urls = ['http://www.dmoztools.net']  #Can use a for loop to add sites 

    #Separate the category
    def parse(self,response):          #parse is the default method for handling responses.
        items = []
        Category = response.xpath('//div[@class="outer-cats"]//h2/a/@href').extract() # If you don't want ' / ', you can try: Category =response.xpath('//div[@class="outer-cats"]//h2/a//text()').extract()
        for category in range(len(Category)):
            item = []
            item = DmozItem()
            Every_category = []
            Every_category.append(Category[category])
            item['Every_category'] = Every_category
            # item['Category'] = Category
            item['Category'] = response.xpath('//div[@class="outer-cats"]//h2/a/@href').extract() # item['Category'] =response.xpath('//div[@class="outer-cats"]//h2/a//text()').extract()
            item['Website_name'] = response.selector.xpath('//title/text()').extract_first()
            item['Website_URL'] = response.url
            item['Website_title'] = response.xpath('//div[@class="outer-cats"]//a/@href').extract()   # item['Website_title'] =response.xpath('//div[@class="outer-cats"]//a//text()').extract()
            items.append(item)
        return items

    # Same row
#     def parse(self,response):          #parse is the default method for handling responses.
        
#         items = []
#         item = DmozItem()
#         item['Category'] = response.xpath('//div[@class="outer-cats"]//h2/a/@href').extract()
#         item['Website_name'] = response.selector.xpath('//title/text()').extract_first()
#         item['Website_URL'] = response.url
#         item['Website_title'] = response.xpath('//div[@class="outer-cats"]//a/@href').extract()
#         items.append(item)
#         return items

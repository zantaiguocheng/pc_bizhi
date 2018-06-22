# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tupian.items import TupianItem
from scrapy.selector import Selector
class BizhiSpider(CrawlSpider):
    name = 'bizhi'
    allowed_domains = ['www.netbian.com','img.netbian.com']
    start_urls = ['http://www.netbian.com/']

    rules = (
        Rule(LinkExtractor(allow=r'index_\d.htm'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/s?/?[a-z]+/',deny='desk/\d+.htm'),callback='parse_item',  follow=False),
    )

    def parse_item(self, response):
        item=TupianItem()
        x=Selector(response)
        imgs=x.re('src="(http.*?\.jpg)".*?alt')
        imgname=x.re('src.*?alt="(.*?)"')
        for i in range(len(imgs)):
            item['tupianming']=imgname[i]
            item['images_urls']=[imgs[i]]
            item['leibie']=x.xpath('//span/h1/text()').extract()
            yield item
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
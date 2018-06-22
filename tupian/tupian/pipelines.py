# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
import re


class TupianPipeline(object):
    def process_item(self, item, spider):
        return item


class XiazaiPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return Request(url=item['images_urls'][0], meta={'leibie': item['leibie'], 'tupianming': item['tupianming']})

    def file_path(self, request, response=None, info=None):
        leibie = request.meta['leibie']
        tpm = request.meta['tupianming']
        houzhui=request.url.split('.')[-1]
        return '%s/%s.%s' % (leibie, tpm,houzhui)

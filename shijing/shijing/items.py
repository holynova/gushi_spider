# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShijingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PoemItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()

    # start_urls = ['http://www.gushiwen.org/guwen/shijing.aspx']

    # def parse(self, response):
    #     for poem in response.css('.guwencontent2'):
    #         yield {
    #             title: poem.css('a::text'),
    #             url: poem.css('a::attr(href)')
    #         }


class ArticalItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    dynasty = scrapy.Field()
    book = scrapy.Field()
    content = scrapy.Field()

# -*- coding: utf-8 -*-
import scrapy
import json
from shijing.items import PoemItem


class PoemSpider(scrapy.Spider):
    name = "poem"
    # start

    def start_requests(self):
        poems = self.convert_json()
        start_urls = [poem['url'] for poem in poems]
        self.log(start_urls)
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = PoemItem()
        item['title'] = response.css('.son1 h1::text').extract_first()
        item['content'] = response.css(
            '.son2 p:nth-of-type(4)').extract_first()
        yield item

    def convert_json(self):
        json_file = file('urls2.json', 'r')
        shijing_arr = json.load(json_file)
        # self.log(shijing_arr[0]['poems'])
        arr = []
        for chapter in shijing_arr:
            for poem in chapter['poems']:
                arr.append({'chapter': chapter['chapter_name'],
                            'name': poem['name'],
                            'url': poem['url']})
        return arr
    # poem = {}
    # poem.chapter_name = chapter.name
    # poem

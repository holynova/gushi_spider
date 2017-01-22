# coding:utf-8

import scrapy


class ShijingSpider(scrapy.Spider):
    name = 'shijing'
    # start_urls = ['http://www.gushiwen.org/guwen/shijing.aspx']
    start_urls = ['http://so.gushiwen.org/gushi/shijing.aspx']

    def parse(self, response):
        for chapter in response.css('.main3 .son2'):
            poems = []
            for poem in chapter.css('a'):
                relative_url = poem.css('::attr(href)').extract_first()
                url = response.urljoin(relative_url)
                poems.append({
                    "name": poem.css('::text').extract_first(),
                    "url": url
                })
            yield {
                "chapter_name": chapter.css('span::text').extract_first(),
                "poems": poems
            }

        # for poem_achor in response.css('.guwencont2 a'):
        #     yield {
        #     "url":poem_achor.css('::attr(href)').extract_first()
        #     }
        # yield response.css('.guwencont2 a::href').extract()
        # for poem in response.css('.guwencont2 a'):
        #     yield {
        #         # content:poem.extract(),
        #         'title': poem.css('::text').extract_first(),
        #         'url': poem.css('::attr(href)').extract_first()
        #     }

# -*- coding: utf-8 -*-
import scrapy
import json
from shijing.items import ArticalItem


def get_url(json_filename):
    f = file(json_filename, 'r')
    json_data = json.load(f)
    urls = []
    for data_item in json_data:
        urls.append(data_item['url'])
    return urls


def clean_str(str):
    ban_words = ['\n', '<br>']
    for ban_word in ban_words:
        str = str.replace(ban_word, '')
    return str


def get_content(response):
    # 正文的几种情况
    # 1. .son2 的text中
    # 2. p::text中,但p下面有span的不包括
    content = ''
    texts = response.css('.son2::text').extract()
    content = ''.join(texts)
    paragraphs = response.css('.son2 p')
    for paragraph in paragraphs:
        span = paragraph.css('span')
        if span == None or span == []:
            p_texts = paragraph.css('::text').extract()
            content += ''.join(p_texts)

    return clean_str(content)


class ArticalUrlSpider(scrapy.Spider):
    name = "artical_url"
    start_urls = [
        # 'http://so.gushiwen.org/type.aspx?p=1&t=%E8%BE%9E%E8%B5%8B%E7%B2%BE%E9%80%89',
        'http://so.gushiwen.org/type.aspx?p=1&t=%E5%AE%8B%E8%AF%8D%E7%B2%BE%E9%80%89']

    def parse(self, response):
        for artical in response.css('.sons p:first-of-type a'):
            yield{
                # 'title': artical.css('::text').extract_first(),
                'url': response.urljoin(artical.css('::attr(href)').extract_first())
            }
        next_page = response.css('.pages a:last-of-type::attr(href)')
        if next_page is not None:
            next_page_url = response.urljoin(next_page.extract_first())
            yield scrapy.Request(url=next_page_url, callback=self.parse)


class UrlSpider(scrapy.Spider):
    name = 'url'
    # start_urls = ['http://so.gushiwen.org/gushi/chuci.aspx']
    start_urls = ['http://so.gushiwen.org/gushi/yuefu.aspx']

    def parse(self, response):
        for anchor in response.css('.son2 span a'):
            yield {'url': response.urljoin(anchor.css('::attr(href)').extract_first())}


class ArticalSpider(scrapy.Spider):
    name = 'artical'
    start_urls = get_url('yuefu.json')
    bookname = u'乐府诗集'

    def parse(self, response):
        # 正文的几种情况
        # 1. .son2 的text中
        # 2. p::text中,但p下面有span的不包括

        content = get_content(response)
        item = ArticalItem()
        item['title'] = response.css('.son1 h1::text').extract_first()
        item['author'] = response.css(
            '.son2 p:nth-of-type(2) a::text').extract_first()
        item['dynasty'] = response.css(
            '.son2 p:nth-of-type(1)::text').extract_first()
        item['content'] = content
        item['book'] = self.bookname
        yield item

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import codecs
import json


class ShijingPipeline(object):

    def process_item(self, item, spider):
        return item


class PoemPipeline(object):

    def open_spider(self, spider):
        filename = 'poems' + \
            datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + '.json'

        self.file = codecs.open(
            filename, 'wb', encoding='utf-8')
        self.file.write(u'[')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ','
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.write(u']')
        self.file.close()


class ArticalPipeline(object):

    def open_spider(self, spider):
        basename = 'artical'
        now_str = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
        filename = basename + now_str + '.json'
        self.file = codecs.open(filename, 'wb', encoding='utf-8')
        self.file.write('[')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ','
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.write(']')
        self.file.close()

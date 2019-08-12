# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KjdsItems(scrapy.Item):
    seq=scrapy.Field()
    trans_amt=scrapy.Field()
    create_date=scrapy.Field()

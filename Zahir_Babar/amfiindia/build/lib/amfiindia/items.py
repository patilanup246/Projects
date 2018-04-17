# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmfiindiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    ARN    = scrapy.Field()
    ARN_Holder_Name    = scrapy.Field()
    Address    = scrapy.Field()
    Pin    = scrapy.Field()
    Email    = scrapy.Field()
    City    = scrapy.Field()
    Telephone_R    = scrapy.Field()
    Telephone_O= scrapy.Field()
    ARN_Valid_Till    = scrapy.Field()
    ARN_Valid_From    = scrapy.Field()
    KYD_Compliant    = scrapy.Field()
    EUIN= scrapy.Field()

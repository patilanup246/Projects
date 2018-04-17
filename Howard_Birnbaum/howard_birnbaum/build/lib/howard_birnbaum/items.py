# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HowardBirnbaumItem(scrapy.Item):
    company = scrapy.Field()
    address = scrapy.Field()
    state = scrapy.Field()
    country = scrapy.Field()
    phone_number = scrapy.Field()
    web_site_url = scrapy.Field()
    email = scrapy.Field()
    city = scrapy.Field()
    postal_code =  scrapy.Field()

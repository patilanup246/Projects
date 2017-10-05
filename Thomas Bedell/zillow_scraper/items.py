# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZillowScraperItem(scrapy.Item):
    # define the fields for your item here like:

    address = scrapy.Field()
    street_address = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    zip_code = scrapy.Field()
    property_url = scrapy.Field()
    property_owner = scrapy.Field()
    price = scrapy.Field()
    zestimate = scrapy.Field()
    property_description = scrapy.Field()
    zillow_id = scrapy.Field()
    beds = scrapy.Field()
    baths = scrapy.Field()
    sq_ft = scrapy.Field()
    HOA_Fee = scrapy.Field()
    rental_value = scrapy.Field()
    image_url = scrapy.Field()
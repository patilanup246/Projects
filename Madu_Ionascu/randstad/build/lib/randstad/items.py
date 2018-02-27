# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RandstadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    source                  = scrapy.Field()
    country                 = scrapy.Field()
    job_title_raw           = scrapy.Field()
    source_post_id          = scrapy.Field()
    posted                  = scrapy.Field()
    location                = scrapy.Field()
    category                = scrapy.Field()
    type                    = scrapy.Field()
    salary_from             = scrapy.Field()
    salary_to               = scrapy.Field()
    salary_currency         = scrapy.Field()
    salary_period           = scrapy.Field()
    description             = scrapy.Field()
    url                     = scrapy.Field()
    reference               = scrapy.Field()
    recruiter_raw           = scrapy.Field()
        
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TotaljobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    source                            = scrapy.Field()
    source_post_id                    = scrapy.Field()
    url                               = scrapy.Field()
    sponsored                         = scrapy.Field()
    posted_date                       = scrapy.Field()
    close_date                        = scrapy.Field()
    location                          = scrapy.Field()
    city                              = scrapy.Field()
    state                             = scrapy.Field()
    country                           = scrapy.Field()
    latitude                          = scrapy.Field()
    longitude                         = scrapy.Field()
    job_title_raw                     = scrapy.Field()
    type                              = scrapy.Field()
    description                       = scrapy.Field()
    company_raw                       = scrapy.Field()
    company_ad_type                   = scrapy.Field()
    company_totaljobs_profile         = scrapy.Field()
    company_logo                      = scrapy.Field()
    industry_raw                      = scrapy.Field()
    recruiter_raw                     = scrapy.Field()
    salary_from                       = scrapy.Field()
    salary_to                         = scrapy.Field()
    salary_currency                   = scrapy.Field()
    salary_period                     = scrapy.Field()

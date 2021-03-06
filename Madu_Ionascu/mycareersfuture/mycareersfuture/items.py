# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MycareersfutureItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    source_post_id    = scrapy.Field()
    url               = scrapy.Field()
    applications      = scrapy.Field()
    posted_date       = scrapy.Field()
    close_date        = scrapy.Field()
    job_title_raw     = scrapy.Field()
    job_level         = scrapy.Field()
    job_category      = scrapy.Field()
    job_type          = scrapy.Field()
    description       = scrapy.Field()
    job_requirements  = scrapy.Field()
    skills_reference  = scrapy.Field()
    company_raw       = scrapy.Field()
    company_logo      = scrapy.Field()
    company_type      = scrapy.Field()
    country           = scrapy.Field()
    location          = scrapy.Field()
    salary_from       = scrapy.Field()
    salary_to         = scrapy.Field()
    salary_currency   = scrapy.Field()
    salary_period     = scrapy.Field()

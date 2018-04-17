# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobstreetItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    source_post_id = scrapy.Field()
    url= scrapy.Field()
    posted_date= scrapy.Field()
    close_date= scrapy.Field()
    job_title_raw= scrapy.Field()
    job_level= scrapy.Field()
    company_raw= scrapy.Field()
    company_url= scrapy.Field()
    company_type= scrapy.Field()
    company_uen= scrapy.Field()
    company_domain= scrapy.Field()
    company_size= scrapy.Field()
    company_facebook= scrapy.Field()
    company_phone= scrapy.Field()
    industry_raw= scrapy.Field()
    min_years_experience= scrapy.Field()
    country= scrapy.Field()
    location= scrapy.Field()
    description= scrapy.Field()

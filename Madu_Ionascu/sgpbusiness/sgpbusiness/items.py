# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SgpbusinessItem(scrapy.Item):
    # define the fields for your item here like:
    company_sgp_url                = scrapy.Field()
    company_uen                    = scrapy.Field()
    company_raw                    = scrapy.Field()
    company_description            = scrapy.Field()
    company_domain                 = scrapy.Field()
    company_registration_date      = scrapy.Field()
    company_registration_type      = scrapy.Field()
    company_status                 = scrapy.Field()
    company_status_date            = scrapy.Field()
    industry_raw                   = scrapy.Field()
    company_phone                  = scrapy.Field()
    email                          = scrapy.Field()
    company_social_media           = scrapy.Field()
    address                        = scrapy.Field()
    postal_code                    = scrapy.Field()

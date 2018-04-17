# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy 
from scrapy.item import Item, Field 


class JobportalItem(scrapy.Item):

    job_url = scrapy.Field()
    job_title_raw = scrapy.Field()
    source_post_id = scrapy.Field() 
    posted = scrapy.Field()
    close_date = scrapy.Field()
    applications = scrapy.Field()
    view_count = scrapy.Field()
    industry = scrapy.Field()
    type = scrapy.Field()
    no_of_vacancies = scrapy.Field()
    min_years_experience = scrapy.Field()
    category = scrapy.Field()
    job_level = scrapy.Field()
    working_hours = scrapy.Field()
    location = scrapy.Field()
    job_description = scrapy.Field()
    job_requirements = scrapy.Field()
    skills = scrapy.Field()
    source = scrapy.Field()



    
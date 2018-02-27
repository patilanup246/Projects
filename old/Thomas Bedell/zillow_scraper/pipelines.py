# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem
from datetime import datetime

from zillow_scraper import settings

import os
import re
import shutil
import csv


class ZillowScraperPipeline(object):

    def __init__(self):
        today = datetime.today().strftime("%Y-%m-%d")
        storage = settings.FILES_STORE
        if not os.path.exists(storage):
            os.makedirs(storage)
        csv_file_name = 'Zillow_Listing_' + today + '.csv'
        full_path = os.path.join(storage, csv_file_name)
        
        self.csv_file = open(full_path, 'wb')
        self.csvwriter = csv.writer(self.csv_file)
        self.csvwriter.writerow([
            'Address', 'Street Address', 'City', 'State', 'Zip Code',
            'Property URL', 'Property Owner', 'Price', 'Zestimate', 'Property Discussion',
            'Zillow ID','Beds','Baths','sq_ft','HOA_Fee','Rental Value','Image URL'
        ])

    def process_item(self, item, spider):
        self.csvwriter.writerow([
            item.get('address'), item.get('street_address'), item.get('city'), item.get('state'),
            item.get('zip_code'), item.get('property_url'), item.get('property_owner'),
            item.get('price'), item.get('zestimate'), item.get('property_description'),
            item.get('zillow_id'),item.get('beds'),item.get('baths'),item.get('sq_ft'),item.get('HOA_Fee'),item.get('rental_value'),item.get('image_url')
        ])
        return item

    def close_spider(self, spider):
        # close csv file
        self.csv_file.close()


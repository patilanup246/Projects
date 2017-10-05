from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import re
from zillow_scraper.items import ZillowScraperItem

import re


def lowercase(string):
    string = string.lower().strip()
    return re.sub(r'\s+', '_', string)


class TestSpider(BaseSpider):
    name = "zillowspider"
    allowed_domains = ["zillow.com"]
    start_urls = [
        "http://www.zillow.com/homes/fsbo/FL/house,condo_type/14_rid/1_days/31.559814,-78.920289,23.795397,-88.698121_rect/6_zm/0_mmm/",
    ]

    # override parse method
    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        # extract the links for detail page
        links = hxs.xpath("//a[contains(@class,'hdp-link routable')]/@href").extract()
        for link in links:
            full_url = "http://zillow.com" + link

            # create new request for details page
            yield Request(full_url, callback=self.parse_home, meta={'url': full_url})

            url = response.urljoin(response.xpath("//a[contains(.//text(), \'Next\')]/@href").extract_first())
            # create new request for next page
            yield Request(url, callback=self.parse)

    # callback for parsing details page
    def parse_home(self, response):
        hxs = HtmlXPathSelector(response)
        item = ZillowScraperItem()

        item['property_url'] = response.meta['url']
        item['zillow_id'] = response.meta['url'].split('/')[-2].replace('_zpid', '')

        # extract locations
        street_address = response.xpath("//header[@class='zsg-content-header addr']/h1/text()").extract_first()
        if street_address:
            street_address = street_address.strip()[:-1]
            item['street_address'] = street_address

        city_state_code = response.xpath("//header[@class='zsg-content-header addr']/h1/span/text()").extract_first()
        if city_state_code:
            city_state_code = city_state_code.split(",")
            state_code = city_state_code[1].strip().split(" ")
            item['city'] = city_state_code[0].strip()
            item['state'] = state_code[0].strip()
            item['address'] = item['street_address'] + ', ' + item['city'] + ', ' + item['state']
            item['zip_code'] = state_code[1].strip()

        # extract price
        item['price'] = response.xpath("//div[contains(@class, 'main-row')]/span/text()").extract_first()
        if item['price']:
            item['price'] = item['price'].strip()[1:].replace(',', '')
        description_values = response.xpath("//div[contains(@class, 'zsg-content-item')]/text()").extract()
        description_values = [i.replace('\n', '').strip() for i in description_values if i.replace('\n', '').strip()]
        description_text = ' '.join(description_values)
        item['property_description'] = description_text
        item['zestimate'] = response.xpath(
            "//div[contains(@class, 'main-row')]/following-sibling::div[contains(@class, 'home-summary-row')]/span[2]/text()").extract_first()
        if item['zestimate']:
            item['zestimate'] = item['zestimate'].strip()[1:].replace(',', '')
        phone = response.xpath(
            "//span[@class='snl name notranslate'][contains(text(), 'Property Owner')]/following-sibling::span/text()").extract_first()
        if phone:
            item['property_owner'] = phone.replace("(", '').replace(")", '').replace('-', '').replace(' ', '')

        beds = [s for s in response.xpath('//div[@id="hdp-content"]/div[2]/div[1]/header/h3//text()').extract() if
                "bed" in s]
        if beds:
            item['beds'] = re.sub("\D", "", beds[0].replace(',', ''))

        baths = [s for s in response.xpath('//div[@id="hdp-content"]/div[2]/div[1]/header/h3//text()').extract() if
                 "bath" in s]
        if baths:
            item['baths'] = re.sub("\D", "", baths[0].replace(',', ''))

        sq_ft = [s for s in response.xpath('//div[@id="hdp-content"]/div[2]/div[1]/header/h3//text()').extract() if
                 "sqft" in s]
        if sq_ft:
            item['sq_ft'] = re.sub("\D", "", sq_ft[0].replace(',', ''))

        HOA_fee = response.xpath(
            '//*[@class="hdp-fact-category"][contains(text(), "HOA")]/..//span[@class="hdp-fact-value"]/text()').extract_first()
        if HOA_fee:
            item['HOA_Fee'] = re.sub("\D", "", HOA_fee.replace(',', ''))

        rental_value = response.xpath(
            '//*[@class="zest-title"][contains(text(), "Rent Zestimate")]/..//div[@class ="zest-value"]/text()').extract_first()
        if rental_value:
            item['rental_value'] = re.sub("\D", "", rental_value.replace(',', ''))

        image_url = response.xpath('//*[@class="lg-tile current"]/div/img/@src').extract_first()
        if image_url:
            item['image_url'] = image_url

        yield item


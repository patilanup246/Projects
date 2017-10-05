
from selenium import webdriver
from pyquery import PyQuery
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1280, 1024))
display.start()
import time
import re, csv
import datetime
def start_driver():
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images":2}
    chromeOptions.add_experimental_option("prefs",prefs)
    chromeOptions.add_argument("--no-sandbox")
    chromeOptions.add_extension('./anticaptcha.crx')
    chromeOptions.add_argument("--disable-setuid-sandbox")
    driver = webdriver.Chrome('./chromedriver',chrome_options=chromeOptions)
    #driver = webdriver.Chrome(chrome_options=chromeOptions)
    driver.get('chrome-extension://neodgnejhhhlcdoglifbmioajmagpeci/options.html')
    driver.find_element_by_id('auto_submit_form').click()
    driver.find_element_by_name('account_key').send_keys('5f6b75f0738a1bd09cf717392c9804a3')
    driver.find_element_by_id('save').click()
    return driver




file_input = open('urls_for_zillow_spider-50-states.txt').read().split("\n")
#print file_input[1]

def get_all_urls(driver,number):
    urls = []
    global_page = []
    global_page.append(file_input[number])
    for url_to_scrap in global_page:
        #print url_to_scrap
        page=1
        while True:
            print (url_to_scrap.replace('/0_mmm','/{}_p/0_mmm'.format(str(page))))
            try:
                driver.get(url_to_scrap.replace('/0_mmm','/{}_p/0_mmm'.format(str(page))))
            except:
                pass
            #print resp.text
            for listing in driver.find_elements_by_css_selector('.zsg-photo-card-overlay-link   '):
                #print listing.get_attribute('href')
                urls.append(listing.get_attribute('href'))
            #print urls
            page+=1

            try:
                driver.find_element_by_css_selector('.off')
            except Exception as e:
                break
    print (urls)
    return urls




for i in range(0,50):
    try:
        driver = start_driver()
        file_export = open('data/csv_all/Zillow_Listing_' + str(i) + '.csv','wb')
        wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
        headers = ['Address', 'Street Address', 'City', 'State', 'Zip Code', 'Property URL', 'Property Owner', 'Price',
                   'Zestimate', 'Property Description', 'Zillow ID', 'Beds', 'Baths', 'sq_ft', 'HOA_Fee',
                   'Rental Value', 'Image URL']
        wr.writerow(headers)
        for url in get_all_urls(driver,i):
            #print url
            try:
                driver.get(url)
            except:
                continue

            start = datetime.datetime.now()
            while True:
                try:
                    address = driver.find_element_by_css_selector('h1.notranslate').text
                    print (address)
                    break
                except Exception as e:
                    print ('waiting for -'+str(datetime.datetime.now()- start))
                    if (datetime.datetime.now()- start).total_seconds() > 150:
                        break
                    print ('sleeping')
                    time.sleep(1)
                    address = ''

            try:
                street_address = address.split(',')[0]
                #print street_address
            except Exception as e:
                street_address = ''

            try:
                city = driver.find_element_by_css_selector('.zsg-h2.addr_city').text.split(',')[0]
                #print city
            except Exception as e:
                city = ''

            try:
                state = driver.find_element_by_css_selector('.zsg-h2.addr_city').text.split(',')[1].strip().split(' ')[0]
                #print state
            except Exception as e:
                state = ''

            try:
                zipcode = driver.find_element_by_css_selector('.zsg-h2.addr_city').text.split(',')[1].strip().split(' ')[1]
                #print zipcode
            except Exception as e:
                zipcode = ''

            try:
                property_url = url
                #print property_url
            except Exception as e:
                property_url = ''

            try:
                property_owner = driver.find_element_by_xpath('//span[text()="Property Owner"]/parent::node()').find_element_by_css_selector('.snl.phone').text
                #print property_owner
            except Exception as e:
                property_owner = ''

            try:
                price = driver.find_element_by_css_selector('.estimates .main-row.home-summary-row span').text
                #print price
            except Exception as e:
                price = ''

            try:
                zestimate = driver.find_element_by_xpath('//span[text()="Zestimate"]/parent::node()').find_element_by_css_selector('span[class=""]').text
            except Exception as e:
                zestimate = ''

            try:
                property_description = driver.find_element_by_css_selector('.hdp-header-description [class="zsg-content-component"]').text
                #print property_description
            except Exception as e:
                property_description = ''

            try:
                zillow_id = url.split('/')[-2].replace('_zpid', '')
            except Exception as e:
                zillow_id = ''

            try:
                bed = driver.find_element_by_css_selector('.zsg-content-header.addr h3 span:nth-child(2)').text
            except Exception as e:
                bed = ''

            try:
                bath = driver.find_element_by_css_selector('.zsg-content-header.addr h3 span:nth-child(4)').text
            except Exception as e:
                bath = ''

            try:
                sqft = driver.find_element_by_css_selector('.zsg-content-header.addr h3 span:nth-child(6)').text
            except Exception as e:
                sqft = ''

            try:
                hoa_fees = driver.find_element_by_id('zmm-mortgage-module-data').get_attribute('data-hoa-fees')
            except Exception as e:
                print (e)
                hoa_fees = ''

            try:
                alltext = driver.page_source
                rental_value = re.findall('restimate\\\\\\\\\\\\&quot;:(.*?),',alltext)[0]
            except Exception as e:
                print (e)
                rental_value = ''

            try:
                image = driver.find_element_by_css_selector('.lg-tile.current img').get_attribute('src')
            except Exception as e:
                image = ''

            product_row = []

            product_row.append(address.encode('ascii', 'ignore'))
            product_row.append(street_address.encode('ascii', 'ignore'))
            product_row.append(city.encode('ascii', 'ignore'))
            product_row.append(state.encode('ascii', 'ignore'))
            product_row.append(zipcode.encode('ascii', 'ignore'))
            product_row.append(property_url.encode('ascii', 'ignore'))
            product_row.append(re.sub("\D", "", property_owner.replace(',', '')))
            product_row.append(re.sub("\D", "", price.replace(',', '')))
            product_row.append(re.sub("\D", "", zestimate.replace(',', '')))
            product_row.append(property_description.encode('ascii', 'ignore'))
            product_row.append(zillow_id)
            product_row.append(re.sub("\D", "", bed.replace(',', '')))
            product_row.append(re.sub("\D", "", bath.replace(',', '')))
            product_row.append(re.sub("\D", "", sqft.replace(',', '')))
            product_row.append(str(hoa_fees))
            product_row.append(str(rental_value))
            product_row.append(image)

            # wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
            wr.writerow(product_row)
        file_export.close()

#print driver.page_source
    except Exception as e:
        print (e)
    finally:
        driver.quit()
        display.popen.kill()
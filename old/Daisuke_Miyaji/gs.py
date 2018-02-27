from pyvirtualdisplay import Display

display = Display(visible=0, size=(1280, 1024))
display.start()
from selenium import webdriver
import time
import scrapy
import os
import re
import yagmail
import requests
from pyquery import PyQuery
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep
import json
import threading
from threading import Thread
from Queue import Queue
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class GS(scrapy.Spider):
    user_from = 'talibhmukadam@gmail.com'
    user_pass = 'muidsa!12@'
    user_to = 'agoop.miyaji@gmail.com'
    user_to2 = 'talibhmukadam@gmail.com'

    def __init__(self,category='',shops_root_url='',via_page_url_regex='',single_shop_url_regex='',single_sleep='',via_page_sleep='',*args,**kwargs):



        try:
            chromeOptions = webdriver.ChromeOptions()
            prefs = {"profile.managed_default_content_settings.images": 2}
            chromeOptions.add_experimental_option("prefs", prefs)
            # chromeOptions.add_argument('headless')
            chromeOptions.add_argument('disable-gpu')
            driver = webdriver.Chrome('./chromedriver', chrome_options=chromeOptions)

            file_json = open('file_json.txt', 'w')
            file_json.write('100')
            file_json.close()


            url_array = []
            url_array.append(shops_root_url)
            print(shops_root_url)
            via_page_url_regex = via_page_url_regex
            print (via_page_url_regex)
            Single_shop_url_regex = single_shop_url_regex
            print (single_shop_url_regex)

            single_sleep = int(single_sleep)
            via_page_sleep = int(via_page_sleep)

            # url_array = ['https://www.redlobster.com/locations/list']
            # via_page_url_regex = '\/locations\/list\/[^\/]+\/[^\/]+\/$'
            # Single_shop_url_regex = '\/locations\/list\/[^\/]+\/[^\/]+\/[^\/]+\/'

            if not via_page_url_regex:
                print('page url is empty')
                final_url_array = self.get_links(driver, url_array, Single_shop_url_regex, single_sleep)
            else:
                print('inside page regex')
                for r in via_page_url_regex.split(';'):
                    print( r)
                    url_array = self.get_links(driver, url_array, r, via_page_sleep)
                    # print url_array

                print  ('going for single shop + ')
                # print url_array
                final_url_array = self.get_links(driver, url_array, Single_shop_url_regex, single_sleep)

            final_json_list = []

            q = Queue()
            map(q.put, final_url_array)

            for i in range(10):
                t = Thread(target=self.worker, args=(q, final_json_list))
                t.start()
            q.join()

            #        for url in final_url_array:
            #            print 'Extracting title - '+url
            #            json_obj = {}
            #            resp = requests.get(url,verify=False)
            #            pq = PyQuery(resp.text)
            #            json_obj['url'] = url
            #            json_obj['title'] = pq('title').text()
            #            final_json_list.append(json_obj)
            file_export = open('exported_scraper_.csv', 'wb')
            wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
            headers = ['URL', 'Title']
            wr.writerow(headers)

            for x in final_json_list:
                wr.writerow([x['url'], x['title']])
            file_export.close()
            # yagmail.SMTP(user_from, user_pass).send(user_to, 'Daisuke API', json.dumps(final_json_list))
            yagmail.SMTP(self.user_from, self.user_pass).send(self.user_to, 'Daisuke API', open('exported_scraper_.csv', 'r').read())
            yagmail.SMTP(self.user_from, self.user_pass).send(self.user_to2, 'Daisuke API', open('exported_scraper_.csv', 'r').read())
            file_json = open('file_json.txt', 'w')
            file_json.write(json.dumps(final_json_list))
            file_json.close()
            return 'true'

            # print json.dumps(final_json_list)
        except Exception as e:
            print (e)
            yagmail.SMTP(self.user_from, self.user_pass).send(self.user_to, 'Daisuke API', 'Couldnt get response for ' + shops_root_url + '. Contact developer')
            file_json = open('file_json.txt', 'w')
            file_json.write('400')
            file_json.close()

        finally:
            driver.quit()


    def worker(self,q, final_json_list):
        while not q.empty():
            try:
                url = q.get()
                print('Extracting title - ' + url)
                json_obj = {}
                resp = requests.get(url, verify=False)
                pq = PyQuery(resp.content)
                json_obj['url'] = url
                json_obj['title'] = pq('title').text()
                final_json_list.append(json_obj)
            except Exception as e:
                pass
            finally:
                q.task_done()




    def get_links(self,dr, urls_array, apply_regex, sleeping):
        link_container = []
        main_window = dr.current_window_handle
        href_strings = ['javascript:', '#']
        for url in urls_array:
            dr.get(url)
            time.sleep(sleeping)
            # print dr.page_source
            try:
                dr.execute_script("$('head').append('<base target=\"_blank\">');")
            except Exception as e:
                dr.execute_script(
                    "link=document.createElement('base');link.target='_blank';document.getElementsByTagName('head')[0].appendChild(link);")

            get_all_hrefs = dr.find_elements_by_css_selector('[href]')
            # print get_all_hrefs
            for href in get_all_hrefs:
                try:
                    ele_href = href.get_attribute("href")
                except Exception as e:
                    continue
                # print ele_href
                if ele_href:
                    if not any(x in ele_href for x in href_strings):
                        try:
                            re.search(apply_regex, ele_href).group()
                            if not ele_href in link_container:
                                print(ele_href)
                                link_container.append(ele_href)
                                # print ele_href
                        except Exception as e:
                            pass

                    else:
                        # print href


                        try:
                            href.send_keys(Keys.CONTROL + Keys.RETURN)
                            dr.switch_to_window(dr.window_handles[1])
                            # print dr.current_url
                            try:
                                re.search(apply_regex, dr.current_url).group()
                                if not dr.current_url in link_container:
                                    link_container.append(dr.current_url)
                                    print (dr.current_url)
                            except Exception as e:
                                # print e
                                pass
                            all_handles = dr.window_handles
                            for handle in all_handles:
                                if not handle == main_window:
                                    dr.switch_to_window(handle)
                                    dr.close()
                            dr.switch_to_window(main_window)
                        except Exception as e:
                            # print dr.current_url
                            # dr.execute_script("window.history.go(-1)")
                            # dr.back()
                            # print e
                            pass
            try:
                link_container.remove(url)
            except Exception as e:
                pass

        # print link_container
        return list(set(link_container))

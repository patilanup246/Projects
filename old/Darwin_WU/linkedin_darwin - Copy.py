#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import json
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import pickle
from selenium import webdriver
import time
import os

from flask import Flask
from flask import request

app = Flask(__name__)

import re

print 'abc'
json_all = {}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
print 'abc'

print 'starting chrome'

a = ''
# driver = webdriver.PhantomJS()
# driver.set_window_size(1280, 1024)
driver.get('https://www.linkedin.com/fizzy/admin')
driver.delete_all_cookies()
try:
    cookies = pickle.load(open("linkedin_cookies.pkl", "rb"))
    driver.delete_all_cookies()

    for cookie in cookies:
        try:
            driver.add_cookie({k: cookie[k] for k in ('name', 'value', 'domain', 'path')})
        except Exception, e:
            pass
    a = 'loggedin'
except Exception, e:
    print e
    print 'No cookies saved yet'
    a = check_login(driver)
    print a


def login_to_linkedin(dri):
    # global driver
    print 'Logging in'
    dri.get(
        'https://www.linkedin.com/uas/login?session_redirect=%2Fvoyager%2FloginRedirect%2Ehtml&fromSignIn=true&trk=uno-reg-join-sign-in')
    print 'fill user'
    dri.find_element_by_css_selector('.form-email input').send_keys('darwin9204@gmail.com')
    print 'fill password'
    dri.find_element_by_css_selector('.form-password input').send_keys('darwinupwork01')
    print 'click button'
    get_url_now = dri.current_url
    dri.find_element_by_css_selector('.form-buttons input').click()
    print 'save cookies'
    # try:
    #     os.remove("linkedin_cookies.pkl")
    # except Exception,e:
    #     print e

    while True:
        print dri.current_url

        if get_url_now == dri.current_url:
            print dri.current_url
            time.sleep(1)
            print 'Sleeping'
            # dri.get_screenshot_as_file('google.png')
        else:
            # dri.get_screenshot_as_file('google.png')
            # pickle.dump(dri.get_cookies() , open("linkedin_cookies.pkl","wb"))
            break

            # check_login(dri)


# check if cookies are valid







def check_login(dr):
    print 'Checking Login'
    dr.get("https://www.linkedin.com/premium/manage")
    if not "https://www.linkedin.com/premium/manage" in dr.current_url:
        print 'Not logged In'
        login_to_linkedin(dr)
    else:
        return 'loggedin'


# pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
def check_loaded(dr):
    while True:
        dr.execute_script('x = 0')
        time.sleep(0.5)
        print dr.execute_script('return x')
        if dr.execute_script('return x') == 0:
            print 'everything loaded'
            break


def expand_resource(dr, query):
    while True:
        try:
            # print dr.execute_script("return document.querySelectorAll('"+query+"').length");
            dr.execute_script("$('" + query + "')[0].click()")
            try:
                WebDriverWait(dr, 30).until_not(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '[type="loader"][size="small"]')))
            except Exception, e:
                pass
                # check_loaded(dr)
        except Exception, e:
            print 'resource complete'
            # print e
            break


def wait_for_dom(dr):
    while True:
        print dr.execute_script("return document.readyState")
        if dr.execute_script("return document.readyState") == 'complete':
            break


@app.route('/linkedin')
def index():
    try:
        print a
        if 'loggedin' == a:
            args = request.args
            profile_page = args['profile']
            username = args['user']
            driver.get(profile_page)
            driver.get_screenshot_as_file('user1.png')

            
            name = ''
            try:
                name = driver.find_element_by_css_selector('.pv-top-card-section__name').text
            except:
                pass
            headline = ''
            try:
                headline = driver.find_element_by_css_selector('.pv-top-card-section__headline').text
            except:
                pass
            json_all['name'] = name
            json_all['title'] = headline

            

    finally:
    # driver.quit()
        pass


    return json.dumps(json_all)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
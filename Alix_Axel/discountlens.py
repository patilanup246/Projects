'''
Created on Jun 1, 2017

@author: Tasneem
'''

from selenium import webdriver
import logging
import json
import ConfigParser
from selenium.webdriver.support.ui import Select
import time
import editdistance
import sys
from datetime import datetime
properties_filename = 'discountlens.properties'
country_lookup_filename = 'country_lookup.properties'
config = ConfigParser.RawConfigParser()
config_country_lookup = ConfigParser.RawConfigParser()
try:
    config.read(properties_filename)    
except Exception,e:
        print 'Property file missing'
        logging.error(e)

try:
    config_country_lookup.read(country_lookup_filename)
except Exception,e:
        print 'Country Lookup file missing'
        logging.error(e)

    

try:
    #driver = webdriver.PhantomJS(service_args=['--load-images=no'])
    #driver.set_window_size(1280, 1024)
    driver = webdriver.Chrome()
    #driver = webdriver.PhantomJS()
    
    
except Exception,e:
    logging.error(e)
    

def get_index(json_key):
    try:
        elements = driver.find_elements_by_css_selector('#optiontable tbody tr th')
        for item in elements:
            if item.text.lower() == config.get('Info', json_key).lower():
                #print item.text
                return elements.index(item)
    except Exception,e:
        logging.error(e)
        pass



logging.basicConfig(filename='discountlens_execution_log_debug.log',level=logging.DEBUG)


    
def access_page(url):
    try:
        print 'Accessing {}'.format(url),
        driver.get(url)
        driver.find_element_by_id('top-container')
        print ' - Successful'
    except Exception,e:
        print ' - Failure'
        logging.error(e)
        sys.exit()
#     finally:
#         driver.quit()
        
        
def select_color(key_index,key_value):        
    
    color_options = driver.find_elements_by_css_selector('.eye.{} td:nth-child({}) select option'.format(key_index,str(get_index('color')+1)))
    
    available_colors = []
    for colors in color_options:
        available_colors.append(colors.text.lower())

    if key_value.lower() in (name.lower() for name in available_colors):
        print 'color available - '+key_value
        
        try:
            select =  Select(driver.find_element_by_css_selector('.eye.{} td:nth-child({}) select'.format(key_index,str(get_index('color')+1))))
            select.select_by_visible_text(str(key_value))
            print 'Selected color'
        except Exception,e:
            logging.error(e)
            print 'Cannot select color'
    else:
        edit_distance_num = []
        for c in color_options:
            edit_distance_num.append(editdistance.eval(c.text, 'Green'))
        try:
            select = Select(driver.find_element_by_css_selector(
                '.eye.{} td:nth-child({}) select'.format(key_index, str(get_index('color') + 1))))
            select.select_by_visible_text(str(color_options[edit_distance_num.index(min(edit_distance_num))].text))
            print 'Selected color '+str(color_options[edit_distance_num.index(min(edit_distance_num))].text)+' - By edit distance '
        except Exception, e:
            logging.error(e)
            print 'Cannot select color'





def get_json(json_filename):
    try:
        json_file = open(json_filename,'r').read()
    except Exception,e:
        print 'File not found - "{}"'.format(json_filename)
        logging.error(e)
    
    try:
        #print json.loads(json_file)
        return json.loads(json_file)
    except Exception,e:
        print 'Json file appears to be corrupted'
        logging.error(e)
        

    
try:
    #input_json = get_json('air-optix-colors.json')
    input_json = get_json(sys.argv[1])
    product_json = input_json['product']
    
      
    access_page(product_json['url'])


    right_config_success = False
    try:
        right_config = product_json['configuration']['R']  
        right_config_success = True
    except Exception,e:
        logging.error(e)
        print 'Node R not present in json'
    if right_config_success:        
        for key in right_config:  
            if get_index(key):
                
                selection_value = right_config[key]
                
                if key == 'color':
                    select_color('r',selection_value)
                    continue

                try:
                    select = Select(driver.find_element_by_css_selector('.eye.r td:nth-child({}) select'.format(str(get_index(key)+1))))
                    select.select_by_value(str(selection_value))
                    print 'Selected {}'.format(str(key))
                except Exception,e:
                    print 'Cannot select {}'.format(str(key))
                    logging.error(e)
                


    left_config_success= False
    try:
        left_config = product_json['configuration']['L']
        left_config_success = True
    except Exception,e:
        logging.error(e)
        print 'Node L not present in json'
    if left_config_success:           
        for key in left_config: 
            if get_index(key):
                selection_value = left_config[key]
                if key == 'color':
                    select_color('l',selection_value)
                    continue
                try:
                    select = Select(driver.find_element_by_css_selector('.eye.l td:nth-child({}) select'.format(str(get_index(key)+1))))
                    select.select_by_value(str(selection_value))
                    print 'Selected {}'.format(str(key))
                except Exception,e:
                    print 'Cannot select {}'.format(str(key))
                    logging.error(e)
                    logging.error(e)
            
    try:
        driver.find_element_by_id('addToCart').click()
        print 'Selected "Add to cart"'
    except Exception, e:
        print 'Could not select "Add to cart"'
        logging.error(e)
        
    try:
        driver.find_element_by_css_selector('p .btn.btn-default.forward').click()
        print 'Selected "To the checkout"'
    except Exception,e:
        logging.error(e)
        print 'Cant select "To the checkout"' 
        
    try:
        driver.find_element_by_css_selector('.box.guest a.btn.register').click()
        print 'Selected "Continue as Guest"'
    except Exception,e:
        logging.error(e)
        print 'Cant select "Continue as Guest"'
        
        
        
    #fill guest form
    try:
        print 'Filling Guest Form - ',
        client_json = input_json['client']
        
        start_time = datetime.now()
        while True:
            try:
                duration = datetime.now() - start_time
                if duration.total_seconds() > 10:
                    break
                driver.find_element_by_css_selector('[name="guest_account"]')
                break
            
            except Exception,e:
                logging.error(e)
                pass
        
        #gender
        driver.find_element_by_css_selector('input[name="gender"][value="f"]'.format(client_json['gender'].lower())).click()
        #firstname
        driver.find_element_by_css_selector('[name="firstname"]').send_keys(client_json['name']['given'])
        #lastname
        driver.find_element_by_css_selector('[name="lastname"]').send_keys(client_json['name']['family'])
        #email
        driver.find_element_by_css_selector('[name="email_address"]').send_keys(client_json['email'])
        #street
        driver.find_element_by_css_selector('[name="street_address"]').send_keys(client_json['address']['street'])
        #post
        driver.find_element_by_css_selector('[name="postcode"]').send_keys(client_json['address']['postalCode'])
        #city
        driver.find_element_by_css_selector('[name="city"]').send_keys(client_json['address']['city'])
        #country
        select = Select(driver.find_element_by_css_selector('[name="country"]'))
        #select.select_by_visible_text(str(client_json['address']['country']))
        select.select_by_visible_text(str(config_country_lookup.get('Info', client_json['address']['country'])))
        #config.get('Info', json_key).lower()
        
        
        #click Confirm
        driver.find_element_by_css_selector('#checkout-address-submit').click()
        
        print 'Successful'
        
    except Exception,e:
        print 'Fail'
        logging.error(e)
        sys.exit()

        
        
        
        
    try: 
        print 'Agree T&C - ',
            
        #submit card info
        driver.find_element_by_css_selector('#checkout-shipping-submit').click()
        
        #click Agree T&C
        driver.find_element_by_css_selector('#agree').click()
        
        #Agree revocation instruction
        driver.find_element_by_css_selector('#agreeReturn').click()
        
        #Click Buy Now
        driver.find_element_by_css_selector('#checkout-overview-submit').click()
    
        print 'Successful'
    except Exception,e:
        print 'Fail'
        logging.error(e)
        sys.exit()


    try:
        print 'Selecting card ',
        driver.find_element_by_css_selector('[title="{}" i]'.format(client_json['payment']['type'])).click()
        print 'Successful'
    except Exception,e:
        logging.error(e)
        print 'Fail'
        sys.exit()
        
        
    try:
        print 'Entering card info -',
        #name
        driver.find_element_by_css_selector('#Ecom_Payment_Card_Name').clear()
        driver.find_element_by_css_selector('#Ecom_Payment_Card_Name').send_keys(client_json['payment']['card']['name'])
        #card number
        driver.find_element_by_css_selector('#Ecom_Payment_Card_Number').send_keys(client_json['payment']['card']['number'])
        #select Month
        select = Select(driver.find_element_by_css_selector('#Ecom_Payment_Card_ExpDate_Month'))
        select.select_by_visible_text(str(client_json['payment']['card']['expiration']['m']))
        #select Year
        select = Select(driver.find_element_by_css_selector('#Ecom_Payment_Card_ExpDate_Year'))
        select.select_by_visible_text(str(client_json['payment']['card']['expiration']['y']))
       
        #cvv
        driver.find_element_by_css_selector('#Ecom_Payment_Card_Verification').send_keys(client_json['payment']['card']['verification'])
        
        #click submit
        driver.find_element_by_css_selector('[name="payment"]').click()
        
        
        print 'Successful'
    except Exception,e:
        logging.error(e)
        print 'Fail'
        sys.exit()
        #print e
        
        
    
            
        
    
    
    time.sleep(2)
    print '\n**************************************'
        
except Exception,e:
    print 'Main method - '+str(e)
    pass
    #print e
    
finally:
    #pass
    time.sleep(5)
    driver.quit()
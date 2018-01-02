'''
Created on 31-Dec-2017

@author: Administrator
'''
from selenium import webdriver
from PIL import Image
import time
fox = webdriver.Firefox()
fox.set_window_size(1600, 2400)
for c in open('input_codes.txt').read().split('\n'):
    
    fox.get('https://in.oriflame.com/products/product?code='+str(c))
    
    # now that we have the preliminary stuff out of the way time to get that image :D
    try:
        fox.find_element_by_css_selector('.pdp-image-slider')
    except:
        continue
    try:
        
        fox.find_element_by_css_selector('.show-more-text.link').click()
        time.sleep(1) 
    except Exception as e:
        print (e)
    try:
        element = fox.find_element_by_class_name('ui-product-detail') # find part of the page you want image of
    except Exception as e:
        print (e)
    size_2_h = 0
    try:
        element_2 = fox.find_element_by_class_name('pdp-info-tabs')
        size_2 = element_2.size
        size_2_h = size_2['height']
    except Exception as e:
        print (e)
    location = element.location
    size = element.size
    
    
    fox.save_screenshot(str(c)+'.png') # saves screenshot of entire page
    
    
    im = Image.open(str(c)+'.png') # uses PIL library to open image in memory
    
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height'] + size_2_h
    
    
    im = im.crop((left, top, right, bottom)) # defines crop points
    im.save(str(c)+'.png') # saves new cropped image
    
fox.quit()
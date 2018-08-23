# -*- coding: utf-8 -*-
'''
Created on May 21, 2018

@author: tasneem
'''
import linkedin_properties
import start_webdriver
import login_linkedin
import database_connect
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys


def message_profiles(driver):
    print ("Loading Profles")
    profiles = database_connect.get_message_profiles()
    print (profiles)
    for profile in profiles:
        
        try:
            driver.get(profile[0])
            
            try:
                time.sleep(5)
                message_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.pv-s-profile-actions--message')))
                
                #message_button.click()
                time.sleep(5)
                driver.find_element_by_css_selector('html').send_keys(Keys.PAGE_DOWN)
                driver.find_element_by_css_selector('html').send_keys(Keys.PAGE_DOWN)
                driver.find_element_by_css_selector('html').send_keys(Keys.PAGE_DOWN)
                driver.find_element_by_css_selector('html').send_keys(Keys.PAGE_DOWN)
                time.sleep(5)
                designation= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-control-name="background_details_company"] h3')))
                time.sleep(5)
                print ('Click the message button')
                driver.execute_script("$('.pv-s-profile-actions--message')[0].click();")
                print ('Message button clicked')
                time.sleep(5)
                print ("Will get message box")
                message_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[role="textbox"]')))
                print ("Got message box")
                print (message_box)
                time.sleep(5)
                message_box.send_keys('''Hola {},\n\nEn tu rol como {} debes haberte topado ya muchas veces con la dificultad de encontrar buenos desarrolladores. Es por esto que quizás te interese conocer Evalart, una plataforma para evaluar desarrolladores con pruebas de programación en línea donde los candidatos deben escribir código real. Con esto puedes evaluar a los programadores en lo más importante, su capacidad para programar. Todo esto totalmente automatizado y en línea.\n\nSi quieres tener más información por favor no dudes en contactarme o visita: http://evalart.com/es/online-programming-tests\n\nSaludos,\nClaudia'''.format(profile[1],designation.text))
                print ("Message written in message box")
                time.sleep(5)
                driver.find_element_by_css_selector('[type="submit"]').click()
                database_connect.update_message_profile(profile[0],True)
            except Exception as e:
                print("An Error Occured");
                print (e)
                database_connect.update_message_profile(profile[0],False)
       
                
            
            time.sleep(10)
            time.sleep(linkedin_properties.DELAY_INBETWEEN_INVITES)
        except Exception as e:
            print("An Error Occured");
            print (e)
                

#is_session_valid = login_linkedin.login_to_linkedin()
if True:
    try:
        DRIVER = start_webdriver.create_driver()
        login_linkedin.load_cookies(DRIVER)
        
        
        message_profiles(DRIVER)
        
        
    finally:
        DRIVER.quit()
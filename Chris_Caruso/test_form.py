from flask import Flask,redirect
from flask import request
from flask import render_template
import time

app = Flask(__name__)

@app.route('/form.jsp')
def my_form():
    return render_template("my-form.html")

def fill_values(driver,label,value):
    try:
        a = driver.find_element_by_css_selector('form').find_element_by_xpath("//*[self::label or self::div or self::span][contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),' {} ') or contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),' {}') or contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'{} ')]".format(label,label,label))
        print ("//*[self::label or self::div or self::span][contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),' {} ') or contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),' {}') or contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'{} ')]".format(label,label,label))
        count1 = 0
        while True:
            
            if count1 > 2:
                return 0
                
            try:
                a.find_element_by_xpath('..//input').send_keys(value)
                return 1
            except Exception as e:
                print (e)
                
                
            try:
                a.find_element_by_xpath('..//textarea').send_keys(value)
                return 1
            except Exception as e:
                print (e)
                
            try:
                a = a.find_element_by_xpath("..")
            except Exception as e:
                print (e)
                break
            
           
            count1+=1
    except Exception as e:
        return 0
        pass


@app.route('/', methods=['POST'])
def my_form_post():
    url_page = ''
    try:
        url_page = request.form['text']
    except:
        pass    

    try:
        import sys
        from selenium import webdriver 
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")  #Uncomment the following 3 lines to run as headless
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
    except Exception as e:
        print ('Please install selenium.\n >>>pip install selenium')
        sys.exit()
    
    
    email = 'bob@hotmail.com'
    message = 'This is a test.  The quick brown fox jumped over the lazy dog.'
    name    = 'Bob Barker'
    subject = 'This is a subject'
    
    
    try:
        driver = webdriver.Chrome('/home/automation/chromedriver',chrome_options=chrome_options)
        #driver = webdriver.Chrome()
    except Exception as e:
        print ('Please keep chromedriver in the same directory or add the path in environment variables.')
        sys.exit()
        
    try:
        #'https://docs.google.com/forms/d/e/1FAIpQLSdBzvALrGZB3QZqfBA9oomiauKneGrOD6Qiycd536bNsP3tJQ/viewform'
        driver.get(url_page)
        
        cap_in_type = len(driver.find_elements_by_css_selector('[type*="captcha"]'))
        cap_in_class = len(driver.find_elements_by_css_selector('[class*="captcha"]')) 
        cap_in_id = (driver.find_elements_by_css_selector('[id*="captcha"]'))
        
        if cap_in_type or cap_in_class or cap_in_id:
            return 'Form submission status - Failed (Captcha Present)'



        n = fill_values(driver,"name",name)
        e = fill_values(driver,"email",email)
        m = fill_values(driver,"message",message)

        fill_values(driver,"Subject",subject)

        driver.save_screenshot('static/screenshot.png')

        driver.find_element_by_css_selector('form').submit()

        
        if n==0 or e==0 or m ==0:

            return ('Form submission status - Failed')
        else:

            return ('Form submission status - Passed')
    except Exception as e:
        return ('Form submission status - Failed ')
        print (e)
    finally:
        #time.sleep(50)
        driver.quit()
        
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    #app.run(host='127.0.0.1', port=8000)

import requests
import pickle
from selenium import webdriver
import time

json_all = {}

driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/fizzy/admin')
#driver.delete_all_cookies()
try:
    cookies = pickle.load(open("linkedin_cookies.pkl", "rb"))
    driver.delete_all_cookies()

    for cookie in cookies:
        try:
            driver.add_cookie({k: cookie[k] for k in ('name', 'value', 'domain', 'path')})
            #print 'cookies loaded'
        except Exception, e:
            print e

except Exception, e:
    #print e
    print 'No cookies saved yet'


def check_loaded(dr):
    while True:
        dr.execute_script('x = 0')
        time.sleep(1)
        print dr.execute_script('return x')
        if dr.execute_script('return x') == 0:
            print 'everything loaded'
            break


def expand_resource(dr,query):
    while True:
        try:
            #print dr.execute_script("return document.querySelectorAll('"+query+"').length");
            dr.execute_script("$('"+query+"')[0].click()")
            check_loaded(dr)
        except Exception, e:
            print 'resource complete'
            #print e
            break

driver.get('https://www.linkedin.com/in/valentincordier/')
jscript = '''var script = document.createElement('script');
script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);
'''
driver.execute_script(jscript)
driver.execute_script("var x = 0;")
driver.execute_script("$('html').bind(\"DOMSubtreeModified\",function(){ x = 1;});")



expand_resource(driver,'.education-section [aria-expanded="false"]')

expand_resource(driver,'.experience-section [aria-expanded="false"]')

expand_resource(driver,'.pv-featured-skills-section [aria-expanded="false"]')

expand_resource(driver,'[data-control-name="contact_see_more"]')

expand_resource(driver,'[data-control-name="accomplishments_expand_languages"]')

expand_resource(driver,'[data-control-name="accomplishments_expand_certifications"]')

#get realeted profiles
#class = .pv-browsemap-section__member-container.mt4

#-----------------this section is for education -------------
education_profiles = driver.find_elements_by_css_selector('.pv-education-entity')
json_edu_list = []
for edu in education_profiles:
    json_edu_obj = {}
    school_name = ''
    degree_name = ''
    field_of_study = ''
    start_date = ''
    end_date = ''
    try:
        school_name = edu.find_element_by_css_selector('.pv-entity__school-name').text
    except Exception,e:
        pass
    try:
        degree_name = edu.find_element_by_css_selector('.pv-entity__degree-name .pv-entity__comma-item').text
    except Exception,e:
        pass
    try:
        field_of_study = edu.find_element_by_css_selector('.pv-entity__fos .pv-entity__comma-item').text
    except Exception,e:
        pass
    try:
        start_date = edu.find_element_by_css_selector('.pv-entity__dates span:nth-child(2) time:nth-child(1)').text
    except Exception,e:
        pass
    try:
        end_date = edu.find_element_by_css_selector('.pv-entity__dates span:nth-child(2) time:nth-child(2)').text
    except Exception,e:
        pass

    json_edu_obj['school_name'] = school_name
    json_edu_obj['degree_name'] = degree_name
    json_edu_obj['field_of_study'] = field_of_study
    json_edu_obj['start_date'] = start_date
    json_edu_obj['end_date'] = end_date
    json_edu_list.append(json_edu_obj)
#print json_edu_list

#-------------this section is for experience --------------------

experience_profiles = driver.find_elements_by_css_selector('.pv-position-entity')
json_exp_list = []
for exp in experience_profiles:
    json_edu_obj = {}
    title = ''
    company_name = ''
    company_url = ''
    description =''
    start_date = ''
    end_date = ''
    employment_duration =''
    location = ''
    try:
        json_edu_obj['title']  = exp.find_element_by_css_selector('h3').text
    except Exception,e:
        pass
    try:
        json_edu_obj['company_name'] = exp.find_element_by_css_selector('.pv-entity__secondary-title').text
    except Exception,e:
        pass
    try:
        json_edu_obj['company_url'] = exp.find_element_by_css_selector('[data-control-name="background_details_company"]').get_attribute("href")
    except Exception,e:
        pass
    try:
        json_edu_obj['description'] = exp.find_element_by_css_selector('.pv-entity__extra-details').text
    except Exception,e:
        pass
    try:
        json_edu_obj['start_date'] = exp.find_element_by_css_selector('.pv-entity__date-range span:nth-child(2)').text.split('-')[0]
    except Exception,e:
        pass
    try:
        json_edu_obj['end_date'] = exp.find_element_by_css_selector('.pv-entity__date-range span:nth-child(2)').text.split('-')[1]
    except Exception,e:
        pass
    try:
        json_edu_obj['employment_duration'] = exp.find_element_by_css_selector('h4.inline-block  .pv-entity__bullet-item').text
    except Exception,e:
        pass
    try:
        json_edu_obj['location'] = exp.find_element_by_css_selector('.pv-entity__location span:nth-child(2)').text
    except Exception,e:
        pass

    json_exp_list.append(json_edu_obj)

#print json_exp_list


json_all['education '] = json_edu_list
json_all['experience '] = json_exp_list


headline = ''
try:
    headline = driver.find_element_by_css_selector('.pv-top-card-section__headline').text
except:
    pass
json_all['headline'] = headline


email = ''
try:
    email = driver.find_element_by_css_selector('.ci-email .pv-contact-info__contact-item').text
except:
    pass
json_all['email'] = email


phone = ''
try:
    phone = driver.find_element_by_css_selector('.ci-phone .pv-contact-info__contact-item').text
except:
    pass
json_all['phone'] = phone


name = ''
try:
    name = driver.find_element_by_css_selector('.pv-top-card-section__name').text
except:
    pass
json_all['name'] = name


presentation  = ''
try:
    presentation = driver.find_element_by_css_selector('.pv-top-card-section__summary').text
except:
    pass
json_all['presentation '] = presentation





json_lang_list =[]
lang_profiles = driver.find_elements_by_css_selector('.languages .pv-accomplishment-entity')
for lang in lang_profiles:
    json_lang_obj = {}
    language = ''
    language_level = ''
    try:
        language = lang.find_element_by_css_selector('h4').text.replace('Language name','')
    except:
        pass
    try:
        language_level = lang.find_element_by_css_selector('p').text
    except:
        pass

    json_lang_obj['language'] = language
    json_lang_obj['language_level'] = language_level
    json_lang_list.append(json_lang_obj)

json_all['languages '] = json_lang_list



json_cert_list = []
cert_profiles = driver.find_elements_by_css_selector('.certifications .pv-accomplishment-entity')

for cert in cert_profiles:
    certification_name = ''
    start_date = ''
    end_date = ''
    company_name = ''
    company_url = ''
    json_cert_obj = {}

    try:
        certification_name = cert.find_element_by_css_selector('.pv-accomplishment-entity__title').text.replace('Title','')
    except:
        pass
    try:
        start_date = cert.find_element_by_css_selector('.pv-accomplishment-entity__date').text.replace('Certification Date','').split('-')[0]
    except:
        pass
    try:
        end_date = cert.find_element_by_css_selector('.pv-accomplishment-entity__date').text.replace('Certification Date','').split('-')[1]
    except:
        pass
    try:
        company_name = cert.find_element_by_css_selector('[data-control-name="certification_detail_company"]').get_attribute("href")
    except:
        pass
    try:
        company_url = cert.find_element_by_css_selector('[data-control-name="certification_detail_company"] p').text
    except:
        pass

    json_cert_obj['certification_name'] = certification_name
    json_cert_obj['start_date'] = start_date
    json_cert_obj['end_date'] = end_date
    json_cert_obj['company_name'] = company_name
    json_cert_obj['company_url'] = company_url

    json_cert_list.append(json_cert_obj)


json_all['certifications '] = json_cert_list


related_profiles = driver.find_elements_by_css_selector('.pv-browsemap-section__member-container')
json_rel_list = []
for rel in related_profiles:
    json_rel_obj = {}
    name = ''
    url = ''
    headline = ''

    try:
        name = cert.find_element_by_css_selector('.name').text
    except:
        pass
    try:
        url = cert.find_element_by_css_selector('a').get_attribute("href")
    except:
        pass
    try:
        headline = cert.find_element_by_css_selector('.browsemap-headline').text
    except:
        pass

    json_rel_obj['name'] = name
    json_rel_obj['url'] = url
    json_rel_obj['headline'] = headline


    json_rel_list.append(json_rel_obj)

json_all['related_profiles'] = json_rel_list


skills = driver.find_elements_by_css_selector('.pv-skill-entity__skill-name')
json_skills_list = []

for skill in skills:
    json_skills_list.append(skill.text)

json_all['skills'] = json_skills_list





websites = driver.find_elements_by_css_selector('.ci-websites')
json_web_list = []
for web in json_web_list:
    json_web_obj = {}
    name = ''
    url = ''
    try:
        name = web.find_element_by_css_selector('.pv-contact-info__website-type').text
    except:
        pass
    try:
        url = web.find_element_by_css_selector('a').get_attribute("href")
    except:
        pass
    json_web_obj['name'] = name
    json_web_obj['url'] = url

    json_web_list.append(json_web_obj)

json_all['websites'] = json_web_list
driver.quit()
import json
print json.dumps(json_all)




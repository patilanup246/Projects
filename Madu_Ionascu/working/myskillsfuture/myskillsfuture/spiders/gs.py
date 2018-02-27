from myskillsfuture.items import JobportalItem
import scrapy
import json
import datetime
import requests

class myskillsfuture(scrapy.Spider):
    name="myskillsfuture"
    all_urls = []

    def __init__(self,*args,**kwargs):
        try:
            

            
            
            tod = str(datetime.datetime.now().strftime ("%Y-%m-%d"))
            try:
                url = "https://storage.scrapinghub.com/collections/280316/s/myskillsfuture"
                headers = {
                        'Content-Type': "application/json",
                        'Authorization': "Basic MjY5NWZjNjFkMGMxNGUyYWIxMDRlMTgyNTVlN2JiYzQ6"
                    }
    
                response = requests.request("GET", url, headers=headers)
    
                last_run_date = response.json()['value']
            except Exception as e:
                print (e)
                last_run_date = tod
            print(tod)
            print (last_run_date)
            r = requests.get('https://www.myskillsfuture.sg/content/portal/en/jobsbank/job-landing/job_directory/_jcr_content/par/job-directory.search?query=rows%3D15%26sort%3Dnew_posting_date%2520desc%252C%2520modified_on%2520desc%26row%3D15%26q%3D*%253A*%26fq%3Dnew_posting_date%253A%255B{}T00%253A00%253A00Z%2520TO%2520{}T23%253A59%253A59Z%255D%26start%3D{}'.format(last_run_date,tod,'0')).json()
            jobs_found = r['response']['numFound'] / 15
            for d in range(0,jobs_found+2):
                r1 = requests.get('https://www.myskillsfuture.sg/content/portal/en/jobsbank/job-landing/job_directory/_jcr_content/par/job-directory.search?query=rows%3D15%26sort%3Dnew_posting_date%2520desc%252C%2520modified_on%2520desc%26row%3D15%26q%3D*%253A*%26fq%3Dnew_posting_date%253A%255B{}T00%253A00%253A00Z%2520TO%2520{}T23%253A59%253A59Z%255D%26start%3D{}'.format(last_run_date,tod,str(d*15))).json()
                
                for u in r1['response']['docs']:
                    self.all_urls.append(u['job_code']) 
            
            if self.all_urls:
                url = "https://storage.scrapinghub.com/collections/280316/s/myskillsfuture"

                payload = {"_key": "lastdate", "value": str(tod)}
                headers = {
                    'Content-Type': "application/json",
                    'Authorization': "Basic MjY5NWZjNjFkMGMxNGUyYWIxMDRlMTgyNTVlN2JiYzQ6"
                    }

                response = requests.request("POST", url, json=payload, headers=headers)
        except Exception as e:
            print (e)
        
        

    def start_requests(self):
        for url in self.all_urls:
            yield scrapy.Request(url='https://www.myskillsfuture.sg/services/public/jb/publicjobs.{}.N.json'.format(url), callback=self.parse)
    
    def parse(self, response):
        item = JobportalItem()
        jsonresponse = json.loads(response.body_as_unicode())
        item['job_url'] = 'https://www.myskillsfuture.sg/content/portal/en/jobsbank/job-landing/job_directory/job-details.html?jobId=' + str(jsonresponse['jobPostingId'])
        try:
            item['job_title_raw'] = str(jsonresponse['jobTitle'].encode('utf-8'))
        except:
            item['job_title_raw'] = ''
            
            
        try:
            item['source_post_id'] = str(jsonresponse['jobPostingId'])
        except:
            item['source_post_id'] = ''
            
        try:
            item['posted'] = str(jsonresponse['postingDate'])
        except:
            item['posted'] = ''
            
        try:
            item['close_date'] = str(jsonresponse['expiryDate'])
        except:
            item['close_date'] = ''
            
        try:
            item['applications'] = str(jsonresponse['noOfApplied'])
        except:
            item['applications'] = ''
            
        try:
            item['view_count'] = str(jsonresponse['numberOfViewed'])
        except:
            item['view_count'] = ''
            
        try:
            item['industry'] = str(jsonresponse['hiringSsic']['description'].encode('utf-8'))
        except:
            item['industry'] = ''
            
        try:
            item['type'] = str(jsonresponse['employmentType'][0]['employmentType']['employmentTypeName'].encode('utf-8'))
        except:
            item['type'] = ''
            
        try:
            item['no_of_vacancies'] = str(jsonresponse['numberOfVacancies'])
        except:
            item['no_of_vacancies'] =''
            
        try:
            item['min_years_experience'] = str(jsonresponse['minYearsExperience'])
        except:
            item['min_years_experience'] = ''
            
        try:
            item['category'] = str(jsonresponse['jobCategory'][0]['category']['jobCategoryName'].encode('utf-8'))
        except:
            item['category'] = ''
            
        try:
            item['job_level'] = str(jsonresponse['positionLevels'][0]['positionLevel']['description'].encode('utf-8'))
        except:
            item['job_level'] = ''
            
        try:
            item['working_hours'] = str(jsonresponse['workingHours'])
        except:
            item['working_hours'] = ''
            
        try:
            item['location'] = str(jsonresponse['jobLocation'][0]['district']['location'])
        except:
            item['location'] = ''
            
        try:
            item['job_description'] = str(jsonresponse['jobDescriptionTextOnly'].encode('utf-8'))
        except:
            item['job_description'] = ''
            
        try:
            item['job_requirements'] = str(jsonresponse['otherRequirementsTextOnly'].encode('utf-8'))
        except:
            item['job_requirements'] = ''
            
        skills = []
        try:
            for s in jsonresponse['skillsRequired']:
                skills.append(s['skillName'].encode('utf-8'))
        except:
            pass
        
        try:
            item['skills'] = str('$'.join(skills))
        except:
            item['skills'] = ''
            
        try:
            item['source'] = str(jsonresponse['jobSource']['description'].encode('utf-8'))
        except:
            item['source'] = ''
        
        yield item
        

    
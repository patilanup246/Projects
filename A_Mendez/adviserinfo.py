# -*- coding: utf-8 -*-
from selenium import webdriver
import re, time, csv, pyautogui
import threading
from queue import Queue
from pyquery import PyQuery
import requests
output_f = open('adviserinfo.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['Individual CRD#',	'Result Found?',	'Name',	'Individual CRD #',	'Alternate Names',	'Firm 1 Name ',	'Firm 1 CRD # ',	'Firm 2 Name ',	'Firm 2 CRD #',	'Registration Type 1',	'Registration Type 2',	'Registration Status 1',	'Registration Status 2'])


crns = open('input_crns.txt').read().split('\n')


def worker(q):

    while not q.empty():
        try:
            crn = q.get()
            print (crn)

            url = "https://www.adviserinfo.sec.gov/IAPD/default.aspx"

            payload = "__EVENTTARGET=ctl00%24cphMain%24sbox%24searchBtn&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKLTUyNTc5ODEzNw9kFgJmD2QWBAIBDxYCHgRUZXh0BTZJQVBEIC0gSW52ZXN0bWVudCBBZHZpc2VyIFB1YmxpYyBEaXNjbG9zdXJlIC0gSG9tZXBhZ2VkAgMPZBYCAgUPZBYCAgEPDxYCHgtDbGVhclNlYXJjaGdkFgoCAQ8WAh4HVmlzaWJsZWhkAgkPD2QWAh4Kb25LZXlQcmVzcwVBcmV0dXJuIEF1dG9TdWJtaXRPblRleHRCb3goJ2N0bDAwX2NwaE1haW5fc2JveF9zZWFyY2hCdG4nLGV2ZW50KTtkAg0PD2QWAh8DBUFyZXR1cm4gQXV0b1N1Ym1pdE9uVGV4dEJveCgnY3RsMDBfY3BoTWFpbl9zYm94X3NlYXJjaEJ0bicsZXZlbnQpO2QCDw8QDxYGHg5EYXRhVmFsdWVGaWVsZAUCSUQeDURhdGFUZXh0RmllbGQFBVZhbHVlHgtfIURhdGFCb3VuZGcWAh8DBUFyZXR1cm4gQXV0b1N1Ym1pdE9uVGV4dEJveCgnY3RsMDBfY3BoTWFpbl9zYm94X3NlYXJjaEJ0bicsZXZlbnQpOxAVAwc1IE1pbGVzCDE1IE1pbGVzCDI1IE1pbGVzFQMBNQIxNQIyNRQrAwNnZ2dkZAIRDw9kFgIfAwVBcmV0dXJuIEF1dG9TdWJtaXRPblRleHRCb3goJ2N0bDAwX2NwaE1haW5fc2JveF9zZWFyY2hCdG4nLGV2ZW50KTtkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYDBRtjdGwwMCRjcGhNYWluJHNib3gkcmRvSW5kdmwFGmN0bDAwJGNwaE1haW4kc2JveCRyZG9GaXJtBRpjdGwwMCRjcGhNYWluJHNib3gkcmRvRmlybYOn6X3A1%2FfkToB9oSFLeTK2b2FTD%2FupTdzqfIfFqmfl&__VIEWSTATEGENERATOR=B3BE8327&__EVENTVALIDATION=%2FwEdAAsiWdW%2B8TvH6zz2AprlH6%2Fp1ldPi%2BNmWsyZ9j%2B9Ukh8yyTXTCu5PKoKHtvTrDD%2ByWjGgZ%2BqCb%2FTt6O46qY3UtIGe%2BW5OtsFLj1nhfrXYd3Ueryb0TCsorBeQnRZFWZRzEac3LbRP1tOrCsDsAaMwmp2qZCL%2Fhrv6eC9FxxEPmS2dD7WMtZFfP0mzsYsrU6fWou%2BO8vcQy82htdhaRoO306SxraF8PRnNlQTKOVQ14NG9TFKm3ZQkJxCuozf6SRdTp8Wy4zNJvo8UktlA02B64tB&ctl00%24cphMain%24sbox%24searchScope=rdoIndvl&ctl00%24cphMain%24sbox%24txtIndvl="+str(crn)+"&ctl00%24cphMain%24sbox%24txtAtFirm=&ctl00%24cphMain%24sbox%24txtFirm=&ctl00%24cphMain%24sbox%24ddlZipRange=5&ctl00%24cphMain%24sbox%24txtZip="
            headers = {
                'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                'accept-encoding': "gzip, deflate, br",
                'accept-language': "en-US,en;q=0.9",
                'cache-control': "max-age=0",
                'connection': "keep-alive",
                'content-length': "1629",
                'content-type': "application/x-www-form-urlencoded",
                'host': "www.adviserinfo.sec.gov",
                'origin': "https://www.adviserinfo.sec.gov",
                'referer': "https://www.adviserinfo.sec.gov/IAPD/default.aspx",
                'upgrade-insecure-requests': "1",
                'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
                }

            response = requests.request("POST", url, data=payload, headers=headers)

            pq = PyQuery(response.text)

            # crn_input = driver.find_element_by_css_selector('[title="Individual"]')
            # crn_input.clear()
            # crn_input.send_keys(str(crn))

            # driver.find_element_by_css_selector('[id*="searchBtn"]').click()


            if pq('[class="searchresultscriteria"]'):

                details = []

                #crn
                details.append (crn)
                try:
                    #result number
                    details.append (pq('[class="searchresultscriteriacol1"]').text())
                except:
                    details.append ('')

                try:
                    #name
                    details.append (pq('[class="displayname"]').text())
                except:
                    details.append ('')

                try:
                    #crd #
                    details.append (pq('[class="displaycrd"]').text())
                except:
                    details.append ('')

                try:
                    #other names
                    details.append (pq('span[id*="OtherNames"]').text())
                except:
                    details.append ('')

                details.append('')
                details.append('')
                details.append('')
                details.append('')

                try:
                    #separatinf firm and firmid
                    firms = pq('[id*="Item_divAddress"]').text().strip()

                    z = re.finditer('(.*?) \(CRD# (.*?)\)',firms)

                    matches = 5
                    for r in z:
                        details[matches] = r.groups()[0]
                        matches+=1
                        details[matches] = r.groups()[1]
                        matches+=1
                except Exception as e:
                    print (e)


                details.append('')
                details.append('')
                details.append('')
                details.append('')

                try:
                    #broker registration type
                    details[9] = pq('[id$="ucIndvlItem_divBroc"]').text().split('\n')[0]
                except:
                    pass

                try:
                    #broker registration status
                    details[11] = pq('[id$="ucIndvlItem_divBroc"] div').text()
                except:
                    pass

                try:
                    #investor registration type
                    details[10] = pq('[id$="ucIndvlItem_divIA"]').text().split('\n')[0]
                except:
                    pass

                try:
                    #investor registration status
                    details[12] = pq('[id$="ucIndvlItem_divIA"] div').text()
                except:
                    pass

                

            else:
                # # Take screenshot
                # pic = pyautogui.screenshot()
        
                # # Save the image
                # pic.save('IAPD/'+str(crn)+'.png') 
                details = []
                details.append(crn)
                details.append('No match has been found for the information you provided.')
            print (details)
            wr.writerow(details)
        except Exception as e:
            print (e)
        finally:
            q.task_done()

q = Queue()
for i in crns:
    q.put(i)
 
startime = time.time()
for i in range(10):
    #print i
    t = threading.Thread(target=worker, args=(q, ))
    t.start()
q.join()
endtime = time.time()
print (endtime-startime)

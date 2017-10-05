import requests
import re
url = "https://connect.data.com/dwr/call/plaincall/SearchDWR.findContacts.dwr"
import json
import time
headers = {
    'accept': "*/*",
    #'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.8",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'content-length': "477",
    'content-type': "text/plain",
    'cookie': "_ga=GA1.2.1532559694.1503222275; _gid=GA1.2.1469282156.1503222275; webact=%7B%22l_vdays%22%3A-1%2C%22l_visit%22%3A0%2C%22session%22%3A1503222475504%2C%22l_search%22%3A%22%22%2C%22l_dtype%22%3A%22%22%2C%22l_page%22%3A%22%22%2C%22counter%22%3A0%2C%22pv%22%3A0%2C%22f_visit%22%3A1503221527422%2C%22version%22%3A%22w172.1%22%7D; !lithiumSSO=~2oMXV8cuv0O1lLIhr~g2zl2jNSJBcQW00JTFQlqdB5CHVKa1X6jQbzXrow73vGMMLT4Ajb7S_nTDnW02WHkg6NSMhgOWjFmjhOg9lxgOkDfS53CFL_VprlRSeIkRh6RDIE4obWfnn33OPK1RX0RdPohExKs2BFtS7SA44D5ixAqroLspw9Ppxc96ApY85OUqmN3LeEPXtGhhkKo3Mkn05UiPCFA_sGwe2XcR93K1zqgCF7k0ow2FTJNEA6LJRdQmHtwm3WyBdpElDQLuiQkxHVIjY8iYnsPnzm27EzWOJUeivnDYkJ5NAZyyaBpMgfDnYG1ZXXVC6vhrVSnlMCBG8yY-Wlw1B1eDKWILF8nQ..; JSESSIONID=AD84C644104458FFB90981A55257EE97.tc102; mbox=session#1503221527435-781950#1503224450|PC#1503221527435-781950.22_20#1504432190|check#true#1503222650; DWRSESSIONID=ObSUXzmmS6Jkp4vm6GZ1XOfO89118m64~Tl; s_sess=%20s_ppv_x%3D%3B%20c16%3Dflash%252026%257C%3B%20v0%3DTyped/Bookmarked%3B%20c22%3DTyped/Bookmarked%3B%20c40%3Ddid%2520not%2520bounce%3B%20c24%3DTyped/Bookmarked%3B%20c6%3Din%3B%20s_ppv%3D100%257C0%3B%20s_cc%3Dtrue%3B%20s_sq%3D%3B",
    'host': "connect.data.com",
    'origin': "https://connect.data.com",
    'pragma': "no-cache",
    'referer': "https://connect.data.com/search",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.39 Safari/537.36"
    }

f_write = open('data_com.txt','w')
f_json = json.loads(open('convertcsv.json').read())

titles = [
        "Vice President of Operations",
          "Director of Operations",
          "Vice President of Manufacturing",
          "Director of Manufacturing",
          "Vice President of Manufacturing Engineering",
          "Director of Manufacturing Engineering",
          "Vice President of Production",
          "Director of Production",
          "Vice President of Logistics",
          "Director of Logistics",
          "Vice President of Quality",
          "Director of Quality",
          "Vice President of Plant Operations",
          "Director of Plant Operations",
          "Vice President of Good Movement",
          "Director of Good Movement",
          "Vice President of Non Conforming Materials",
          "Director of Non Conforming Materials",
          "RFID",
          "Process Improvement",
          "Founder",
          "Co-Founder"
          ]

for j in f_json:
    if j['J']:
        for title in titles:
            print j['J'] + '\t'+title

            payload = "callCount=1\r\nnextReverseAjaxIndex=0\r\nc0-scriptName=SearchDWR\r\nc0-methodName=findContacts\r\nc0-id=0\r\nc0-param0=string:%7B%22filters%22%3A%7B%22titles%22%3A%5B%22"+title+"%22%5D%2C%22companies%22%3A%5B%22"+j['J']+"%22%5D%7D%2C%22actionsOnColumns%22%3A%7B%22companyName%22%3A%7B%22sort%22%3A%22asc%22%7D%7D%2C%22totalRecordsOnPage%22%3A200%7D\r\nbatchId=10\r\ninstanceId=0\r\npage=%2Fsearch\r\nscriptSessionId=ObSUXzmmS6Jkp4vm6GZ1XOfO89118m64~Tl/du74$Tl-CTu*pLh7f"


            response = requests.request("POST", url, data=payload, headers=headers)
            time.sleep(3)
            print response.text
            r = re.findall('inactive:false,name:"(.*?)"',response.text)
            print r
            if r:
                print r
                for profile in r:
                    j['K'] = profile
                    j['L'] = title
                    f_write.write(json.dumps(j)+',\n')

            else:
                j['K'] = ''
                j['L'] = title
                f_write.write(json.dumps(j)+',\n')
            f_write.flush()

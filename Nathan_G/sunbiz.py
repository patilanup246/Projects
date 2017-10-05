from pyquery import PyQuery
import csv
import requests
import sys
import openpyxl
url = "http://search.sunbiz.org/Inquiry/CorporationSearch/ByDocumentNumber"


headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }
f= open('f_sunbiz.csv','wb')
writer = csv.writer(f)
headers2 = ['Document Number','Company','First_name','Last_name','Address1','Address2','Address3','City','State','Zip','Country']
writer.writerow(headers2)
start = int(str(sys.argv[1])[1:])
end = int(str(sys.argv[2])[1:])
#print start
i=0
while (start+i) <= end:
    try:

        payload = "SearchTerm=N{}&InquiryType=DocumentNumber&SearchNameOrder=".format(str(start+i))
        response = requests.request("POST", url, data=payload, headers=headers)
        pq = PyQuery(response.text)
        #print response.text
        if pq('.validation-summary-errors').text():
            i += 1
            continue

        try:
            officername= str(pq('#maincontent > div.searchResultDetail > div:nth-child(7) > span:nth-child(8)').prev()).split('\n')[1]
            officer_address = str(pq('#maincontent > div.searchResultDetail > div:nth-child(7) > span:nth-child(8) div')).split('\n')
        except IndexError,e:
            officername = str(pq('#maincontent > div.searchResultDetail > div:nth-child(6) > span:nth-child(2)').text())
            officer_address = str(pq('#maincontent > div.searchResultDetail > div:nth-child(6) > span:nth-child(3) div')).split('\n')

        address1 = officer_address[1].replace('<br/>&#13;','')
        address2 = ''
        try:
            #print officer_address[2]
            if ',,' in officer_address[2]:
                city = officer_address[2].replace('<br/>&#13;', '').split(',,')[0].strip()
                state = officer_address[2].replace('<br/>&#13;', '').split(',,')[1].strip().split(' ')[0]
                zip = officer_address[2].replace('<br/>&#13;', '').split(',,')[1].strip().split(' ')[1].replace('<br/></div>&#13;','')
            else:
                city = officer_address[2].replace('<br/>&#13;', '').split(',')[0].strip()
                state = officer_address[2].replace('<br/>&#13;', '').split(',')[1].strip().split(' ')[0]
                zip = officer_address[2].replace('<br/>&#13;', '').split(',')[1].strip().split(' ')[1].replace(
                    '<br/></div>&#13;', '')
        except IndexError,e:
            address2 = officer_address[2].replace('<br/>&#13;', '').strip()
            if ',,' in officer_address[3]:
                city = officer_address[3].replace('<br/>&#13;', '').split(',,')[0].strip()
                state = officer_address[3].replace('<br/>&#13;', '').split(',,')[1].strip().split(' ')[0]
                zip = officer_address[3].replace('<br/>&#13;', '').split(',,')[1].strip().split(' ')[1].replace(
                    '<br/></div>&#13;', '')
            else:
                city = officer_address[3].replace('<br/>&#13;', '').split(',')[0].strip()
                state = officer_address[3].replace('<br/>&#13;', '').split(',')[1].strip().split(' ')[0]
                zip = officer_address[3].replace('<br/>&#13;', '').split(',')[1].strip().split(' ')[1].replace('<br/></div>&#13;','')


        csv_row = []
        csv_row.append('N'+str(start+i))
        csv_row.append(pq('.corporationName p:nth-child(2)').text())
        try:
            csv_row.append(officername.split(',',1)[1].strip())
            csv_row.append(officername.split(',', 1)[0].strip())
        except IndexError,e:
            csv_row.append(officername)
            csv_row.append('')
        csv_row.append(address1)
        csv_row.append(address2)
        csv_row.append('')
        csv_row.append(city)
        csv_row.append(state)
        csv_row.append(zip)
        csv_row.append('')
        writer.writerow(csv_row)
        #print csv_row


        # print pq('.corporationName p:nth-child(2)').text() +'\t'
        #
        #
        # print officername.split(',',1)[1].strip() +'\t'
        # print officername.split(',', 1)[0].strip() +'\t'
        # print address1 +'\t'
        # print address2 +'\t'
        # print city +'\t'
        # print state +'\t'
        # print zip +'\t'
        # print




        #f.write(pq('.corporationName p:nth-child(2)').text()+'\t'+officername.split(',',1)[1].strip() +'\t'+officername.split(',', 1)[0].strip() +'\t'+address1 +'\t'+address2 +'\t'+city +'\t'+state +'\t'+zip +'\n')
        #f.flush()
        print str(start + i)
        i+=1
    except Exception,e:
        print str(start + i)

        i += 1
        pass
f.close()
wb = openpyxl.Workbook()
ws = wb.active

f1 = open('f_sunbiz.csv','rb')
reader = csv.reader(f1)
for row in reader:
    ws.append(row)
f1.close()

wb.save('sunbiz_output.xlsx')
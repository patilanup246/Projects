from threading import Thread
from Queue import Queue
import requests
import csv
import datetime
import sys
reload(sys)

sys.setdefaultencoding('utf-8') #set utf-8 encoding
#Check if pyquery is installed
try:
    from pyquery import PyQuery
except Exception,e:
    print 'Install package using pip - <pip install pyquery>'

#file for storing the results in csv format
file_export = open('columbia_university_professors_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email'] # csv headers
wr.writerow(headers)


primary_url = "https://directory.columbia.edu/people/search"
name_keys = 'abcdefghijklmnopqrstuvwxyz'
school = 'Columbia University'

departments = ['Accounts Payable',
'American Assembly',
'Architecture Planning Preserv',
'Art History & Archaeology',
'AUBURN, Union Theological Seminary',
'Avery Library',
'Burke Library',
'Business & Economics Library',
'Center for Career Education',
'Center for Teaching & Learning',
'Child & Adolescent Psychiatry',
'College of Dental Medicine',
'Columbia College',
'Columbia Health',
'Columbia Scholastic Press',
'Columbia University Press',
'Comm & Public Affairs',
'Community Impact',
'Controller',
'Council European Studies',
'Ctr Digital Rsch & Scholarship',
'Ctr for Environ Sustainability',
'Ctr Intl Earth Sci Info Netwrk',
'CU Human Resources',
'CU Information Technology',
'CUMC HR',
'CUMC Public Safety',
'Department of Anesthesiology',
'Department of Anthropology',
'Department of Astronomy',
'Department of Biostatistics',
'Department of Chemistry',
'Department of Classics',
'Department of Computer Science',
'Department of Dermatology',
'Department of Economics',
'Department of Epidemiology',
'Department of History',
'Department of Italian',
'Department of Mathematics',
'Department of Medicine',
'Department of Music',
'Department of Neurology',
'Department of Ophthalmology',
'Department of Pediatrics',
'Department of Pharmacology',
'Department of Philosophy',
'Department of Physics',
'Department of Psychiatry',
'Department of Psychology',
'Department of Religion',
'Department of Slavic Languages',
'Department of Sociology',
'Department of Surgery',
'Department of Systems Biology',
'Department of Urology',
'Dept Appl Physics & Appl Math',
'Dept Civil Eng & Eng Mechanics',
'Dept Earth & Environmental Eng',
'Dept Environmental Health Sci',
'Dept Health Policy/Management',
'Dept Industrial Eng & Oper Res',
'Dept Intercollegiate Athletics',
'Dept Medicine Infectious Dis',
'Dept Microbiology & Immunology',
'Dept of Biological Sciences',
'Dept of Biomedical Engineering',
'Dept of Electrical Engineering',
'Dept of Genetics & Development',
'Dept of Germanic Languages',
'Dept of Mechanical Engineering',
'Dept of Med Hematology & Onc',
'Dept of Medicine Allen Hospt',
'Dept of Medicine Cardiology',
'Dept of Medicine Family Med',
'Dept of Medicine General Med',
'Dept of Obstetrics/Gynecology',
'Dept of Orthopaedic Surgery',
'Dept of Pathology&Cell Biology',
'Dept of Political Science',
'Dept of Sociomedical Sciences',
'Dept Physiology/CellBiophysics',
'Dept Population&Family Health',
'Developmental Neuroscience',
'Double Discovery Center',
'Earl Hall',
'Earth & Environmental Sciences',
'Earth Institute',
'Ecology Evolution Environ Bio',
'English & Comp Literature',
'Environmental Heath/Safety Off',
'Epidemiology Substance Abuse',
'Experimental Therapeutics',
'Facilities',
'Finance',
'French & Romance Philology',
'Fu Fnd School Eng/Appl Science',
'Gender Sexuality & Health',
'Geriatric Psychiatry',
'Gertrude H. Sergievsky Center',
'Grad School of Arts & Sciences',
'Graduate School of Business',
'Graduate School of Journalism',
'Harlem Hospital Center',
'Inst Data Sciences&Engineering',
'Inst Soc& Econ Research&Policy',
'Internal Audit',
'Italian Academy',
'Journalism Library',
'Kraft Center',
'Lamont-DohertyEarthObservatory',
'Latin American/IberianCultures',
'Law Ethics and Psychiatry',
'LeRoy Neiman Ctr Print Studies',
'Libraries  Social Sciences',
'Mailman School Public Health',
'Mental Health Svcs Rsch Policy',
'Middle East Institute',
'MidEast S Asia African Studies',
'Miller Theatre',
'Molec Imaging & Neuropathology',
'Music Library',
'Naomi Berrie Diabetes Center',
'Natl Ctr on Addict/Subst Abuse',
'Nevis Laboratories',
'Office of Alumni & Development',
'Office of the President',
'Office of the Provost',
'Office of the Secretary',
'Ombuds Office',
'Oral History/Archives',
'Otolaryngology/Head&Neck Surg',
'Psych Clinical Therapeutics',
'Psych Cognitive Neuroscience',
'Psych Integrative Neuroscience',
'Psych Molecular Therapeutics',
'Psych Neuroscience & Behavior',
'Psych Translational Imaging',
'Psychiatry Behavioral Medicine',
'Psychiatry Biostatistics',
'Psychiatry Central Admin',
'Psychiatry Clin Phenomenology',
'Psychiatry Clinical Programs',
'Psychiatry Ctr for Bioethics',
'Psychiatry Epidemiology',
'Psychiatry Medical Genetics',
'Psychiatry Psychoanalytic Ctr',
'Psychiatry Stroud Center',
'Psychiatry Substance Abuse',
'Psychiatry Washington Heights',
'Public Safety',
'Purchasing',
'Rare Book & Manuscript Library',
'Rehab & Regenerative Med OT',
'School Intl & Public Affairs',
'School of General Studies',
'School of Law',
'School of Nursing',
'School of Professional Studies',
'School of Social Work',
'School of the Arts',
'Social Psychiatry',
'Social Work Library',
'South Asia Institute',
'Starr East Asian Library',
'Taub Institute',
'The School at Columbia Univ',
'Treasury',
'University Event Management',
'University Programs & Events',
'University Seminars',
'University Senate',
'UTS, Union Theological Seminary',
'Weatherhead East Asian Inst']

headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.8",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'content-length': "150",
    'content-type': "application/x-www-form-urlencoded",
    'host': "directory.columbia.edu",
    'origin': "https://directory.columbia.edu",
    'referer': "https://directory.columbia.edu/people/search/advanced",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    }

for dep in departments:
    for i in xrange(26):
        for j in xrange(26):
            print dep,name_keys[i],name_keys[j]
            payload = "filter.email=&filter.uni=&filter.phone=&filter.soundex=&filter.searchTerm={}*&filter.title=&filter.department={}".format(name_keys[i]+name_keys[j],dep)
            response = requests.request("POST", primary_url, data=payload, headers=headers)
            #print response.text
            pq = PyQuery(response.text)

            for people in pq('.table_results tr'):
                if pq('.table_results tr').index(people) > 0:
                    #print pq(people)('td:nth-child(1) a').text()
                    csv_row = []
                    csv_row.append(pq(people)('td:nth-child(1) a').text())
                    csv_row.append(pq(people)('td:nth-child(2) a').text())
                    csv_row.append(school)
                    csv_row.append(pq(people)('td:nth-child(4) a').text())
                    wr.writerow(csv_row)

            #print pq('.table_results tr:nth-child(2) > td:nth-child(1) > a').text()
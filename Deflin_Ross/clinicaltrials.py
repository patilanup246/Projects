import requests
from pyquery import PyQuery

# resp = requests.get('https://clinicaltrials.gov/ct2/show/results/NCT01194219')
#
# pq = PyQuery(resp.text)
#
# page_url = 'https://clinicaltrials.gov'+pq('[title="Show all outcome measures"]').attr('href')
page_url = 'https://clinicaltrials.gov/ct2/show/study/NCT01194219?term=psoriasis&rslt=With&sect=X01256#all'
resp = requests.get(page_url)

pq = PyQuery(resp.text)
print pq('#outcome1+br+table+div table:nth-child(2) tr:nth-child(4) .pale_outcome_color').text()
B = page_url
C = ''
D = pq('#sponsor').text()
E = pq(".info-date:contains('First received:')").text().split(',')[1].strip()

G = 'clintrials.gov'
H = ''
I = ''
J = 'clintrials'
K = 'no'
L = 'Celgene'

N = pq('.identifier').text()
O = 'Celgene '+E+' '+'('+N+')'
P = 'nct'
Q = ''
R = ''
S = E
T = pq('#outcome1+br+table+div table:nth-child(2) tr:nth-child(4) .pale_outcome_color').text().replace('Baseline to Week ','')
U = 'parallel'
V = 'double blind'

#https://clinicaltrials.gov/ct2/show/study/NCT01194219?show_locs=Y#locn
F =  pq("tr:nth-child(3) [headers='studyInfoColData']").text()
M = D+' ('+E+'). '+F+'. '+G
W = ''
if 'efficacy' in F.lower():
    W = 'efficacy'
X = pq('.data_table td:nth-child(2) span:nth-child(1)').text()
Y = pq('.data_table td:nth-child(3) span:nth-child(1)').text()
Z =''
AA ='double blind'
AB = pq('ol:nth-child(1)').text()
AC = pq('ol:nth-child(1)').text()
print AB
print AC






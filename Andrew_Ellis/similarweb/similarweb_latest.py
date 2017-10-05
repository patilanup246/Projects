#!/usr/bin/python3
from threading import Thread
from queue import Queue
import time
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
urls = []
from datetime import datetime
import json

countries = {"4":"Afghanistan",
"248":"Åland Islands",
"8":"Albania",
"12":"Algeria",
"16":"American Samoa",
"20":"Andorra",
"24":"Angola",
"660":"Anguilla",
"10":"Antarctica",
"28":"Antigua and Barbuda",
"32":"Argentina",
"51":"Armenia",
"533":"Aruba",
"36":"Australia",
"40":"Austria",
"31":"Azerbaijan",
"44":"Bahamas",
"48":"Bahrain",
"50":"Bangladesh",
"52":"Barbados",
"112":"Belarus",
"56":"Belgium",
"84":"Belize",
"204":"Benin",
"60":"Bermuda",
"64":"Bhutan",
"68":"Bolivia, Plurinational State of",
"535":"Bonaire, Sint Eustatius and Saba",
"70":"Bosnia and Herzegovina",
"72":"Botswana",
"74":"Bouvet Island",
"76":"Brazil",
"86":"British Indian Ocean Territory",
"96":"Brunei Darussalam",
"100":"Bulgaria",
"854":"Burkina Faso",
"108":"Burundi",
"132":"Cabo Verde",
"116":"Cambodia",
"120":"Cameroon",
"124":"Canada",
"136":"Cayman Islands",
"140":"Central African Republic",
"148":"Chad",
"152":"Chile",
"156":"China",
"162":"Christmas Island",
"166":"Cocos (Keeling) Islands",
"170":"Colombia",
"174":"Comoros",
"178":"Congo",
"180":"Congo, the Democratic Republic of the",
"184":"Cook Islands",
"188":"Costa Rica",
"384":"Côte d'Ivoire",
"191":"Croatia",
"192":"Cuba",
"531":"Curaçao",
"196":"Cyprus",
"203":"Czech Republic",
"208":"Denmark",
"262":"Djibouti",
"212":"Dominica",
"214":"Dominican Republic",
"218":"Ecuador",
"818":"Egypt",
"222":"El Salvador",
"226":"Equatorial Guinea",
"232":"Eritrea",
"233":"Estonia",
"231":"Ethiopia",
"238":"Falkland Islands (Malvinas)",
"234":"Faroe Islands",
"242":"Fiji",
"246":"Finland",
"250":"France",
"254":"French Guiana",
"258":"French Polynesia",
"260":"French Southern Territories",
"266":"Gabon",
"270":"Gambia",
"268":"Georgia",
"276":"Germany",
"288":"Ghana",
"292":"Gibraltar",
"300":"Greece",
"304":"Greenland",
"308":"Grenada",
"312":"Guadeloupe",
"316":"Guam",
"320":"Guatemala",
"831":"Guernsey",
"324":"Guinea",
"624":"Guinea-Bissau",
"328":"Guyana",
"332":"Haiti",
"334":"Heard Island and McDonald Islands",
"336":"Holy See (Vatican City State)",
"340":"Honduras",
"344":"Hong Kong",
"348":"Hungary",
"352":"Iceland",
"356":"India",
"360":"Indonesia",
"364":"Iran, Islamic Republic of",
"368":"Iraq",
"372":"Ireland",
"833":"Isle of Man",
"376":"Israel",
"380":"Italy",
"388":"Jamaica",
"392":"Japan",
"832":"Jersey",
"400":"Jordan",
"398":"Kazakhstan",
"404":"Kenya",
"296":"Kiribati",
"408":"Korea, Democratic People's Republic of",
"410":"Korea, Republic of",
"414":"Kuwait",
"417":"Kyrgyzstan",
"418":"Lao People's Democratic Republic",
"428":"Latvia",
"422":"Lebanon",
"426":"Lesotho",
"430":"Liberia",
"434":"Libya",
"438":"Liechtenstein",
"440":"Lithuania",
"442":"Luxembourg",
"446":"Macao",
"807":"Macedonia, the former Yugoslav Republic of",
"450":"Madagascar",
"454":"Malawi",
"458":"Malaysia",
"462":"Maldives",
"466":"Mali",
"470":"Malta",
"584":"Marshall Islands",
"474":"Martinique",
"478":"Mauritania",
"480":"Mauritius",
"175":"Mayotte",
"484":"Mexico",
"583":"Micronesia, Federated States of",
"498":"Moldova, Republic of",
"492":"Monaco",
"496":"Mongolia",
"499":"Montenegro",
"500":"Montserrat",
"504":"Morocco",
"508":"Mozambique",
"104":"Myanmar",
"516":"Namibia",
"520":"Nauru",
"524":"Nepal",
"528":"Netherlands",
"530":"Netherlands Antilles",
"540":"New Caledonia",
"554":"New Zealand",
"558":"Nicaragua",
"562":"Niger",
"566":"Nigeria",
"570":"Niue",
"574":"Norfolk Island",
"580":"Northern Mariana Islands",
"578":"Norway",
"512":"Oman",
"586":"Pakistan",
"585":"Palau",
"275":"Palestine, State of",
"591":"Panama",
"598":"Papua New Guinea",
"600":"Paraguay",
"604":"Peru",
"608":"Philippines",
"612":"Pitcairn",
"616":"Poland",
"620":"Portugal",
"630":"Puerto Rico",
"634":"Qatar",
"638":"Réunion",
"642":"Romania",
"643":"Russian Federation",
"646":"Rwanda",
"652":"Saint Barthélemy",
"654":"Saint Helena, Ascension and Tristan da Cunha",
"659":"Saint Kitts and Nevis",
"662":"Saint Lucia",
"663":"Saint Martin (French part)",
"666":"Saint Pierre and Miquelon",
"670":"Saint Vincent and the Grenadines",
"882":"Samoa",
"674":"San Marino",
"678":"Sao Tome and Principe",
"682":"Saudi Arabia",
"686":"Senegal",
"688":"Serbia",
"891":"SERBIA AND MONTENEGRO",
"690":"Seychelles",
"694":"Sierra Leone",
"702":"Singapore",
"534":"Sint Maarten (Dutch part)",
"703":"Slovakia",
"705":"Slovenia",
"90":"Solomon Islands",
"706":"Somalia",
"710":"South Africa",
"239":"South Georgia and the South Sandwich Islands",
"728":"South Sudan",
"724":"Spain",
"144":"Sri Lanka",
"729":"Sudan",
"736":"Sudan",
"740":"Suriname",
"744":"Svalbard and Jan Mayen",
"748":"Swaziland",
"752":"Sweden",
"756":"Switzerland",
"760":"Syrian Arab Republic",
"158":"Taiwan",
"762":"Tajikistan",
"834":"Tanzania, United Republic of",
"764":"Thailand",
"626":"Timor-Leste",
"768":"Togo",
"772":"Tokelau",
"776":"Tonga",
"780":"Trinidad and Tobago",
"788":"Tunisia",
"792":"Turkey",
"795":"Turkmenistan",
"796":"Turks and Caicos Islands",
"798":"Tuvalu",
"800":"Uganda",
"804":"Ukraine",
"784":"United Arab Emirates",
"826":"United Kingdom",
"840":"United States",
"581":"United States Minor Outlying Islands",
"858":"Uruguay",
"860":"Uzbekistan",
"548":"Vanuatu",
"862":"Venezuela, Bolivarian Republic of",
"704":"Vietnam",
"92":"Virgin Islands, British",
"850":"Virgin Islands, U.S.",
"876":"Wallis and Futuna",
"732":"Western Sahara",
"887":"Yemen",
"894":"Zambia",
"716":"Zimbabwe"}
headers = {
    'accept': "application/json, text/javascript, */*; q=0.01",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.8",
    'cache-control': "no-cache",
    'pragma': "no-cache",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.39 Safari/537.36"
    }

urls = open('urls.txt', 'r').read().split('\n')
#print (urls[1])
f_andrew_output = open('similarweb_output.txt', 'w')
head = ['URL','Visits','PagePerVisit','BounceRate','TimeOnSite','Direct','Referrals','Search','Social','Paid Referrals','Appstore Internals','Self Referrals',
        'Mail','Paid Search Share','Top Categories And Fills','Top Also Visited','Top Referring','Top Country Shares','Similar Sites', 'Time']
f_andrew_output.write('\t'.join(head)+'\n')

def worker(q):
    #print (q)
    while not q.empty():

        try:
            url = q.get()
            #print (url)
            #url_id = url.rsplit('-->')[0]
            #site = url.rsplit('-->')[1]
            
            #response = requests.get("https://api.similarweb.com/SimilarWebAddon/"+site.replace('\n','').strip()+"/all",proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050'))
            response = requests.get("https://api.similarweb.com/SimilarWebAddon/"+url.replace('\n','').strip()+"/all", headers=headers)
            website_details =''
            try:
                j = json.loads(response.text)


                #print len(j.keys())
                website_details = (url+'\t'+
                str(int(j['Engagments']['Visits'])) + '\t' +
                str(j['Engagments']['PagePerVisit']) + '\t' +
                str(j['Engagments']['BounceRate'] * 100) + '\t' +
                str(j['Engagments']['TimeOnSite']) + '\t' +
                str(j['TrafficSources']['Direct'] * 100) + '\t' +
                str(j['TrafficSources']['Referrals'] * 100) + '\t' +
                str(j['TrafficSources']['Search'] * 100) + '\t' +
                str(j['TrafficSources']['Social'] * 100) + '\t' +
                str(j['TrafficSources']['Paid Referrals'] * 100) + '\t' +
                str(j['TrafficSources']['Appstore Internals'] * 100) + '\t' +
                str(j['TrafficSources']['Self Referrals'] * 100) + '\t' +
                str(j['TrafficSources']['Mail'] * 100) + '\t' +
                str(j['PaidSearchShare'] * 100) + '\t')
                
                
                #f_andrew_output.write()
                website_details+=('"')
                for a in j['TopCategoriesAndFills']:
                    website_details+=(a['Category'] + ', ')
                website_details+=('"\t')
                website_details+=('"')
                for a in j['TopAlsoVisited']:
                    website_details+=(a + ', ')
                website_details+=('"\t')
                website_details+=('"')
                for a in j['TopReferring']:
                    website_details+=(a['Site'] + ' ' + str(a['Value'] * 100) + ',')
                website_details+=('"\t')
        
                similar_sites = []
                for sim in j['SimilarSites']:
                    similar_sites.append(sim['Site'])

                c =[]
                for coun in j['TopCountryShares']:
                    if j['TopCountryShares'].index(coun) < 3:
                       #print (coun['Country'])
                       c.append(countries[str(coun['Country'])]+'-->'+str(coun['Value']*100))

                #website_details+=(str(j['EstimatedMonthlyVisits']['2016-12-01']) + '\t')
                # website_details+=(str(j['EstimatedMonthlyVisits']['2017-02-01']) + '\t')
                # website_details+=(str(j['EstimatedMonthlyVisits']['2017-03-01']) + '\t')
                # website_details+=(str(j['EstimatedMonthlyVisits']['2017-04-01']) + '\t')
                # website_details+=(str(j['EstimatedMonthlyVisits']['2017-05-01']) + '\t')
                # website_details+=(str(j['EstimatedMonthlyVisits']['2017-06-01']) + '\t')
                # website_details+=(str(j['EstimatedMonthlyVisits']['2017-07-01']) + '\t')


                website_details+=(','.join(c)+'\t')
                website_details+=(','.join(similar_sites)+'\t')
                website_details+=(str(datetime.now())+'\n')
        
                print ('Site : '+ url+'\t\t : Successful\n')
        
        
        
            except Exception as e:
                #print (e)
                print ('Site : '+ url+'\t\t : No info found\n')
                website_details = (url+'\n')
            finally:
                response.close()
            f_andrew_output.write(website_details)
            f_andrew_output.flush()
        except Exception as e:
            print (e)
        finally:
            q.task_done()

q = Queue()
[q.put(i) for i in urls]
#print(q.qsize())
startime = time.time()
for i in range(1):
    #print (i)
    t = Thread(target=worker, args=(q, ))
    t.start()
q.join()
endtime = time.time()
#print (endtime-startime)
    
    
    
    

import requests
import json
url = "https://www.upwork.com/ab/proposals/api/proposals/type/archived"

applications = []

headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.8",
    'cache-control': "no-cache",
    'cookie': "device_view=full; console_user=rangwala_tasneem; recognized=1; __troRUID=ae6edcf5-cd64-4b42-8852-2d8a98461c5a; __troSYNC=1; __ssid=5643cdb5-7944-4122-9b36-80d57f99b959; mp_b36aa4f2a42867e23d8f9907ea741d91_mixpanel=%7B%22distinct_id%22%3A%20%22469f0ae5-a319-16cd-aeec-e5d259d53be4%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fsupport.upwork.com%2Fhc%2Fen-us%2Fsections%2F202260668-Get-Paid-for-Work%22%2C%22%24initial_referring_domain%22%3A%20%22support.upwork.com%22%7D; __zlcmid=hTgae72zfcNQHq; _ga=GA1.1.2071089916.1497886756; _gid=GA1.1.467494506.1499616206; _br_uid_2=uid%3D5746583369939%3Av%3D11.8%3Ats%3D1499893713104%3Ahc%3D6; bf_lead=piuv3v5geto00; __trossion=1499893714_1800_1__ae6edcf5-cd64-4b42-8852-2d8a98461c5a%3A1499893714_1499893921_6; sc.ASP.NET_SESSIONID=ssepoolp3hxdbhc2o2k0jytu; ki_t=1499893921997%3B1499893921997%3B1499893921997%3B1%3B1; ki_r=; _ceg.s=oszxk2; _ceg.u=oszxk2; wordfence_verifiedHuman=0b266d10d1906d18e4616c1bb05ed58c; __cfduid=dfc14c7cea5fd3b204cf16f7258b5b0361499894431; DA[rangwala_tasneem]=58c3c2af47ef4fca9bf63f28a1edb282%2C0%2Cv8%2C1507670593; acced10826077=11127579; mp_mixpanel__c=25; master_access_token=01471091.oauth2v1_cddaaeea29b73e52700bb203bd69fd92; oauth2_global_js_token=oauth2v1_4f5f9a5fa31f2325a2e176296cc5d431; optimizelySegments=%7B%222772971468%22%3A%22false%22%2C%222800491501%22%3A%22gc%22%2C%222801081125%22%3A%22direct%22%2C%222806681009%22%3A%22none%22%2C%222877800604%22%3A%22true%22%7D; optimizelyEndUserId=oeu1499616631565r0.2750212543708188; optimizelyBuckets=%7B%7D; last_accessed_app=dash; dash_company_last_accessed=705290620522987521; mp_fdf88b8da1749bafc5f24aee259f5aa4_mixpanel=%7B%22distinct_id%22%3A%20%2215d2841aca247a-081653e7752734-333f5902-1d4c00-15d2841aca3fc%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.upwork.com%2Fab%2Ffind-work%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.upwork.com%22%7D; session_id=ced70ca98feccb85faf2e96aef6a3958; _ga=GA1.2.2071089916.1497886756; _gid=GA1.2.467494506.1499616206; _px3=19a9e6f426523b6ab81928a0e5c9630660bd84a4deafdbd666cf46cfd052fb2e:wQ5BNhM9Yq1faHzYccbpuEo8RTY/wjNeVgkf3dpPdpY3ytouC5HNYQv6b6J+2GWRtoqdW4nonWFe2zjId+8flw==:1000:Sso276biqbWF0t0Jy0tYqmVXeHlot9PF+2uOMoVMBu7zCQpA60lvth93WeEwb0WeFLdcpCNbS+zdlrrVgBQQqnV8oNSzEwrqBLZvVTmVy4vtlAQmPSWxVuLbMm9iM+RlUAJm8sn3bkfQk6+s174eq5VyJtK8xliTa/pb9vhZaDo=; visitor_id=103.207.10.146.1499616192364034; current_organization_uid=705290620522987521; company_last_accessed=d10826077; qt_visitor_id=49.202.56.431456989363959580; XSRF-TOKEN=6f2e807fd8bb6c59585383f4f16c6861",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.66 Safari/537.36"
    }

for i in xrange(16):
    print i
    querystring = {"page":str(i)}
    response = requests.request("GET", url, headers=headers, params=querystring)
    for a in response.json()['applications']:
        applications.append(a)

print json.dumps(applications)
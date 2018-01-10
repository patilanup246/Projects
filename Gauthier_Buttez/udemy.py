import requests
from pyquery import PyQuery
import json, re
import os
import urllib

def get_course_id(course_url):
    headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, sdch",
    'accept-language': "en-US,en;q=0.8",
    'Cache-Control': "no-cache",
    'cookie': "ud_firstvisit=2017-12-27T09:40:49.872283+00:00:1eU8Cf:kpv689bNHPcjH86rax3jg7h4K0Y; new_user=true; existing_user=true; optimizelyEndUserId=oeu1514367595072r0.3008683293685195; __ssid=5e6ac83c-4459-4d3c-b121-c8db47997118; IR_gbd=udemy.com; client_id=bd2565cb7b0c313f5e9bae44961e8db2; dj_session_id=50y4uab8omqw53v6x9qgzpg2kmue141q; csrftoken=pmQx1w6TViZZb9JGFZ89B1g5Snb5bMag; access_token=NC0BM3LMlZIZ4GaRmvAyk6bCsklT6iaPBcDGJ01X; __ar_v4=554CPNW4XBAX5EYKBL4HVU%3A20180026%3A3%7COKLCQMMNANCRNGGEOKKR5M%3A20180026%3A3%7CVH5RDLCI7NHB5GFMJDUBVW%3A20180026%3A3; intercom-session-sehj53dd=Q0k3SlZ6bUxOQ0JLUDVZVDdvQ3pRUWRHdFVGamVEL3cyT1Y0cUUwQzRxcks4bU50OXlBTTV2WS9QYnVWNkRIUS0tQlc5NnZ0ZlFNdnJyYjkvZ21haTlSZz09--0c823a71b3cfa1c867410cba02a91a1ac289fb01; intercom-lou-sehj53dd=1; optimizelySegments=%7B%22306102099%22%3A%22gc%22%2C%22306155008%22%3A%22direct%22%2C%22306161004%22%3A%22false%22%2C%227473112303%22%3A%22none%22%2C%227518841116%22%3A%22true%22%2C%227514910721%22%3A%22Marketing%22%7D; optimizelyBuckets=%7B%7D; _ga=GA1.1.901433430.1514367598; _gid=GA1.1.1334547858.1514367598; IR_PI=1514367605222.z2ykoz8l5hgrm; IR_5420=1514373388283%7C0%7C1514372454005; ki_t=1514367609858%3B1514367609858%3B1514373391823%3B1%3B20; ki_r=; _ga=GA1.2.901433430.1514367598; _gid=GA1.2.1334547858.1514367598; ud_rule_vars=\"eJyFjUEKwjAURK8i2WrL_2nSNDlLoCTNV4JKME3dlN7dUBQEF65mMfPerKy4fKFCYXzGOZaUzeQ6EAGUH3gvlPYOJIUOufTaA5EwU0rXSMwc2GrZzc1lzPRYqGZwhWwtLOOAqkHecHUAbQQYoVstpdD8CGAALDvV1TnmSu3Hf9hBAWr1ze7HU1ryTG9DifdfA6JBZYRoJe-wHz6GjW0vu6lGsw==:1eU9iS:sVfa73v9ObBkKm4fPjhQB2q2keM\"; eva=SlFILR5ATzcTQhtwXkBPfgRGGzwT; __udmy_2_v57r=ca304d07b826479ba05ed3125b9b0ee4; seen=1; _px2=eyJ1IjoiNjFiMDIzYjAtZWFmNS0xMWU3LTljZmQtNzUwOWMzNmQ4Y2E5IiwidiI6IjJmYTQxMzgwLWVhZTItMTFlNy05MmJkLThmYjIwNGFiZjdmNyIsInQiOjE1MTQzNzQzMDQ4ODIsImgiOiIzYThmMTgxMjhlM2VmMmFmYmVjOTgwODQzYjExOGEzOWRiMmE1M2NkZWFlNmU1YzQ5OWU4ZTUwZjJlMTdiNjkyIn0=; _px3=0e28647da423ea4f5af65ebeb610b69882aa11573cb3836d1241404294fb52c1:yOnGGypNBPPMB5wd/ITHGFm4xuF44qIT2+Qm/LG/T/diZApv1ipECxcYLiq3yfbsj20UmGtzU+fNSIIFlYNJOA==:1000:N14pLiv7z/BBN/qR/JUbwgi+TnKaLgE/NTcHm6ehRQkZ8F7AhnmsBFgChFDYjQrSZFWQ1Kn/wC29pkeQzsYEieRXYZGoiwD3O9eevGo6M/zxzLr3zfxWx6eXMCLBlWcM9ICXNPAFFm6BvSP4110kxo6bPFV3rHKcZD8nGasNxOs=",
    'pragma': "no-cache",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2683.0 Safari/537.36"
    }
    #print requests.get(course_url,headers=headers).text
    pq = PyQuery(requests.get(course_url,headers=headers).text)
    #return pq('.rating [data-user-tracker-object-id]').attr('data-user-tracker-object-id')
    return pq('.rating [data-user-tracker-object-id]').attr('data-user-tracker-object-id') 
def subscribe(course_id):
    url = "https://www.udemy.com/course/subscribe/"

    querystring = {"courseId":course_id}
    
    headers_subscribe = {
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, sdch",
        'accept-language': "en-US,en;q=0.8",
        'Cache-Control': "no-cache",
        'cookie': "ud_firstvisit=2017-12-27T09:40:49.872283+00:00:1eU8Cf:kpv689bNHPcjH86rax3jg7h4K0Y; new_user=true; existing_user=true; optimizelyEndUserId=oeu1514367595072r0.3008683293685195; __ssid=5e6ac83c-4459-4d3c-b121-c8db47997118; IR_gbd=udemy.com; client_id=bd2565cb7b0c313f5e9bae44961e8db2; dj_session_id=50y4uab8omqw53v6x9qgzpg2kmue141q; csrftoken=pmQx1w6TViZZb9JGFZ89B1g5Snb5bMag; access_token=NC0BM3LMlZIZ4GaRmvAyk6bCsklT6iaPBcDGJ01X; _ga=GA1.1.901433430.1514367598; _gid=GA1.1.1334547858.1514367598; intercom-session-sehj53dd=b1JidzFpSUxOMEVKMVJrQm1jNzZ0aVdGdWc3RTBqUitIS3gzYzJGYlNIV2lER1I3M2VYcDZWMmJQVm53ckloUy0tSUU3QzRaWmZRMkUvWWtKQzl2bjg3QT09--006ed6db9ace059e2fc8103427225bf625e90c10; intercom-lou-sehj53dd=1; optimizelySegments=%7B%22306102099%22%3A%22gc%22%2C%22306155008%22%3A%22direct%22%2C%22306161004%22%3A%22false%22%2C%227473112303%22%3A%22none%22%2C%227518841116%22%3A%22true%22%2C%227514910721%22%3A%22Marketing%22%7D; optimizelyBuckets=%7B%7D; eva=SlFILR5ATzcTQhtwXkBPfgRGGzwT; __udmy_2_v57r=ca304d07b826479ba05ed3125b9b0ee4; ud_rule_vars=eJx9zcEKwjAQBNBfKblqZTdNmma_JVCSZpWgUkxTL6X_bqEKguBpDsObWUTx-cKFY_9MUypjpsE3oCKY0MlWGRs8aI4NSh1sAGZFwzheEwuqxOLEzU-lH8Y5T7wv9CXd2W2tExLQ1ChraSpEAqSmPRloO40HAAJw4li9FzI_Zt4y-vKLwZICUvZktVZWfuNzypvaj__bzgBa87GrWF8gQ0av:1eU9T4:m9Zvn8lRXjHOYm5fBQuN4ADzNVc; seen=1; IR_PI=1514367605222.z2ykoz8l5hgrm; IR_5420=1514372454005%7C0%7C1514372454005; _px2=eyJ1IjoiMzQwMGJjNDAtZWFmNS0xMWU3LThlYzMtOTUwZmE0MjliODdmIiwidiI6IjJmYTQxMzgwLWVhZTItMTFlNy05MmJkLThmYjIwNGFiZjdmNyIsInQiOjE1MTQzNzMwMTQ1OTUsImgiOiJlNjFmZTEyMmNiZGYxNGE2YjEzNGEzODViNjIwNWY2MzE0NThkYmMyNmRiYzI1YzE2Y2UwN2Q1MWIxNTA3MGQ2In0=; _px3=b14cef6ae786e70b44a138e40c06effbc5f400ac66484f1e62fbfffd6411f4b3:XOYDkHXJg1IegSuQPAJfvELwc+3cFZgtsGiL3j4to8FLAZxPdeh5JRheYN94vbQWDbeK2EXPt5nc0ShQ6Q/xEA==:1000:ikNPXzFWgjEYwHYqKp6hqcA2OhM1gkDJkC7Lg3l6ljjk6nN43zgivLt/NjzaLlQMlNDWLp3o9jCfm3SKEXJtMS5cKrTmBmNDPiFnZqSVVq4fgCt497sfr8qA91i0MMz+GL5QE2S+/0IUCemz9vyr1AaZQ8kknjO0lPfiPIloyrU=; ki_t=1514367609858%3B1514367609858%3B1514372460623%3B1%3B15; ki_r=; _ga=GA1.2.901433430.1514367598; _gid=GA1.2.1334547858.1514367598",
        'pragma': "no-cache",
        'referer': "https://www.udemy.com/wordpress-seo-the-complete-yoast-seo-plugin-tutorial/",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2683.0 Safari/537.36"
        }
    
    response = requests.request("GET", url, headers=headers_subscribe, params=querystring)
    
    
def get_videos_id(course_id):
    try:
        url = "https://www.udemy.com/api-2.0/courses/{}/cached-subscriber-curriculum-items".format(course_id)
        
        querystring = {"fields[asset]":"@min,title,filename,asset_type,external_url,length,status","fields[chapter]":"@min,description,object_index,title,sort_order","fields[lecture]":"@min,object_index,asset,supplementary_assets,sort_order,is_published,is_free","fields[practice]":"@min,object_index,title,sort_order,is_published","fields[quiz]":"@min,object_index,title,sort_order,is_published","page_size":"9999","fields%5Bquiz%5D":"@min,object_index,title,sort_order,is_published","fields%5Bpractice%5D":"@min,object_index,title,sort_order,is_published","fields%5Blecture%5D":"@min,object_index,asset,supplementary_assets,sort_order,is_published,is_free","fields%5Bchapter%5D":"@min,description,object_index,title,sort_order","fields%5Basset%5D":"@min,title,filename,asset_type,external_url,length,status"}
        
        headers = {
            'accept': "application/json, text/plain, */*",
            'accept-encoding': "gzip, deflate, sdch",
            'accept-language': "en-US,en;q=0.8",
            'authorization': "Bearer NC0BM3LMlZIZ4GaRmvAyk6bCsklT6iaPBcDGJ01X",
            'Cache-Control': "no-cache",
            'cookie': "ud_firstvisit=2017-12-27T09:40:49.872283+00:00:1eU8Cf:kpv689bNHPcjH86rax3jg7h4K0Y; new_user=true; existing_user=true; optimizelyEndUserId=oeu1514367595072r0.3008683293685195; __ssid=5e6ac83c-4459-4d3c-b121-c8db47997118; IR_gbd=udemy.com; client_id=bd2565cb7b0c313f5e9bae44961e8db2; dj_session_id=50y4uab8omqw53v6x9qgzpg2kmue141q; csrftoken=pmQx1w6TViZZb9JGFZ89B1g5Snb5bMag; access_token=NC0BM3LMlZIZ4GaRmvAyk6bCsklT6iaPBcDGJ01X; optimizelySegments=%7B%22306102099%22%3A%22gc%22%2C%22306155008%22%3A%22direct%22%2C%22306161004%22%3A%22false%22%2C%227473112303%22%3A%22none%22%2C%227518841116%22%3A%22true%22%2C%227514910721%22%3A%22Marketing%22%7D; optimizelyBuckets=%7B%7D; IR_PI=1514367605222.z2ykoz8l5hgrm; IR_5420=1514368485969%7C0%7C1514367605222; _ga=GA1.2.901433430.1514367598; _gid=GA1.2.1334547858.1514367598; _ga=GA1.1.901433430.1514367598; _gid=GA1.1.1334547858.1514367598; ki_t=1514367609858%3B1514367609858%3B1514368512193%3B1%3B13; ki_r=; intercom-session-sehj53dd=STFzSEFjL0VSdzZHaFFtVlF1bjFVenQvTUJVNWFDOE1Ga0NSN0g2ZXFnZ2JXd1BGYWpVZ1BBWTZvWURmbktkZS0tMW9HZ0dqeUh5eEw4dGV3eGdkemJDdz09--029555f334b774cf1275fcfa80d799cddc8c3bbc; intercom-lou-sehj53dd=1; _px2=eyJ1IjoiMDU3MmNhYzAtZWFlYy0xMWU3LWI0ZjUtOWY4MmIyYTJmODBiIiwidiI6IjJmYTQxMzgwLWVhZTItMTFlNy05MmJkLThmYjIwNGFiZjdmNyIsInQiOjE1MTQzNjk5Nzk1ODIsImgiOiIwNDAwYjI3YWM4YjM2NDdhY2IyZDNiZWNhM2FkNmM0MzU3NWI3MGE1NjFkYTI2NWE1NTFhMzM3MGViOGNkMWZkIn0=; _px3=f78b3ffc8a4d45fee7464d6dcaee8a108fff66f6c363b3e2c1c536f32a755c5c:KBWfPg0XsGENva/zMbRK6lw6D7SuKUiDq4LcTuer4R0awp8kzh+X3f2PBXlcl2tJBGDOfttnrAp526XbHc56sA==:1000:rc47jNcltKDDa/QOgzowRLElqKEhQ13mJjDUmG/7ZzrM3n41sHSkHOgclObgTLskD7Af+61M+1+o3psglQJDe+kFnv/4c0Sj9fcXVrYMBbq3TRkEUwLYRVoXfPWleul1A3KOwGCPlSruUfMtSf4bOdRYOIsKJYw8uJhpjg25AyM=; eva=SlFILR5ATzcTQhtwXkBPfgRGGzwT; ud_rule_vars=\"eJx9zcEKwjAQBNBfKblqyybdmG6-JVCSZpWgUkxTL6X_bqEKHsTTHIY3s4ji84ULx_6ZplTGbAffAkYwoVMnNBQ8aI6tVDpQAGa0wzheEwtbicWJm59KP4xznnhf6Eu6s9taJxRIU0tVK1MBWa1tS42WqDo8AFgAJ47VeyHzY-Ytoy8_MYJFakhrJPWNzylvaj_-bzsDkszHrmJ9ASlMRr8=:1eU9DQ:ZA0OPWbF3dOwMlIoEcffR9SBh0s\"; __udmy_2_v57r=ca304d07b826479ba05ed3125b9b0ee4; seen=1",
            'pragma': "no-cache",
            'referer': "https://www.udemy.com/seo-tutorial/learn/v4/t/lecture/7141998?start=0",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2683.0 Safari/537.36",
            'x-requested-with': "XMLHttpRequest",
            'x-udemy-authorization': "Bearer NC0BM3LMlZIZ4GaRmvAyk6bCsklT6iaPBcDGJ01X"
            }
        
        response = requests.request("GET", url, headers=headers, params=querystring)
        
        return (response.json()['results'])
    except:
        return []

# for course in open('udemy_courses.txt','r').read().split('\n'):
#     course_id = str(get_course_id(course))
#     print course_id
#     #subscribe(course_id)

headers1 = {
    'accept': "application/json, text/plain, */*",
    'accept-encoding': "gzip, deflate, sdch",
    'accept-language': "en-US,en;q=0.8",
    'authorization': "Bearer NC0BM3LMlZIZ4GaRmvAyk6bCsklT6iaPBcDGJ01X",
    'Cache-Control': "no-cache",
    'cookie': "ud_firstvisit=2017-12-27T09:40:49.872283+00:00:1eU8Cf:kpv689bNHPcjH86rax3jg7h4K0Y; new_user=true; existing_user=true; optimizelyEndUserId=oeu1514367595072r0.3008683293685195; __ssid=5e6ac83c-4459-4d3c-b121-c8db47997118; IR_gbd=udemy.com; client_id=bd2565cb7b0c313f5e9bae44961e8db2; dj_session_id=50y4uab8omqw53v6x9qgzpg2kmue141q; access_token=NC0BM3LMlZIZ4GaRmvAyk6bCsklT6iaPBcDGJ01X; __ar_v4=554CPNW4XBAX5EYKBL4HVU%3A20180026%3A3%7COKLCQMMNANCRNGGEOKKR5M%3A20180026%3A3%7CVH5RDLCI7NHB5GFMJDUBVW%3A20180026%3A3; optimizelySegments=%7B%22306102099%22%3A%22gc%22%2C%22306155008%22%3A%22direct%22%2C%22306161004%22%3A%22false%22%2C%227473112303%22%3A%22none%22%2C%227518841116%22%3A%22true%22%2C%227514910721%22%3A%22Marketing%22%7D; optimizelyBuckets=%7B%7D; csrftoken=pmQx1w6TViZZb9JGFZ89B1g5Snb5bMag; IR_PI=1514367605222.z2ykoz8l5hgrm; IR_5420=1514437940996%7C0%7C1514437619256; _ga=GA1.2.901433430.1514367598; _gid=GA1.2.1334547858.1514367598; _ga=GA1.1.901433430.1514367598; _gid=GA1.1.1334547858.1514367598; ki_t=1514367609858%3B1514434961071%3B1514438132129%3B2%3B34; ki_r=; intercom-session-sehj53dd=VzVPTHBUK1RIeEN6cmtxSmtZZkxvbmtBa2JjRmU5NHNRbEVFMTl3d3dmWWgzVUtiajYwdmRuZGJaK3NnY1NkNS0tb2RuWFRZYUllMzMrMjV6WDEwTnBWQT09--23421f86a23b949813169df6b26a2506ca832637; intercom-lou-sehj53dd=1; _px2=eyJ1IjoiYWUwZGI3MjAtZWI4ZC0xMWU3LWFiOGUtZWZmYWMxNjIyNzRjIiwidiI6IjJmYTQxMzgwLWVhZTItMTFlNy05MmJkLThmYjIwNGFiZjdmNyIsInQiOjE1MTQ0Mzg4MDc5NjYsImgiOiI0MDQwZjA5YjUxMWRiMDgwMzczOWFkMDQ2N2IyNjZiM2Y1NjA1NTE1Yjg5ZWM4MTUxZTRjYmIxNzY3OGQwMDQzIn0=; _px3=0272b54d9c2fb37697d8ab8564f866a100ed45b68eb1c570b28d71fd4ccffdaf:qtpGI2sqf0Q8XTiHPXPNzh+X54dgBR/O4xYrDBiM0UGmemDFCc33fks3n+GytqIfXEY68LXkxIoaB50owL6blA==:1000:KMUuzQNihNHJ2vZmbUNp5XIZkyD9NJoVKlSCZeeVKiDmHvw4a3mqQ+YDDRUXGyDvnpPW0U5iJNQnuUTd3rXUOMr8nTTkby3TqIWzLPzfSU3ha1l1UY3LJe/dHN29aq45xxyihnzlUKz0SPGMv/CtXBDPQ2UWLePdpgiWAHrJHRo=; eva=SlFILR5ATzcTQhtwXkBPfgRGGzwT; __udmy_2_v57r=ca304d07b826479ba05ed3125b9b0ee4; ud_rule_vars=eJx9jcsKwjAQRX-lZKstk5fT5FsCJWlGCSrFNHVT-u8GqiAIru7ics5ZWfH5QoXi8ExzKlO2o5egImDoxUmhCR40RcmFDiYAkbLjNF0TMduw1bGbn8uQ6bFQ3egLuXo4JoBjy0UrsAFjFVhlOqO1MuIAYAEcOzZveJyWPNOeH0q6_xo4t0JWSac19ii_DeeUq2Jn_9d7BG7ww25sewH0K0a2:1eUQbf:ZFwvtVq4mFQjH7wHMCrrlmieQhU; seen=1",
    'pragma': "no-cache",
    'referer': "https://www.udemy.com/heatmaps/learn/v4/t/lecture/3615464",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2683.0 Safari/537.36",
    'x-requested-with': "XMLHttpRequest",
    'x-udemy-authorization': "Bearer NC0BM3LMlZIZ4GaRmvAyk6bCsklT6iaPBcDGJ01X"
    }
courses_url = open('udemy_courses.txt','r').read().split('\n')
cu = 0
for course in open('udemy_courses_id.txt','r').read().split('\n'):
    primary_folder = PyQuery(requests.get(courses_url[cu],headers=headers1).text)('title').text().split('|')[0].strip()
    #reset_value=1 
    for i in get_videos_id(course):
        if i['_class'] == 'chapter':
            chapter_index = str(i['object_index'])
            chapter = str(i['object_index'])+'_'+i['title']
            reset_value = 1
        else:
            try:
                if i['asset']['asset_type'] == 'Video':
                    print courses_url[cu]+str(i['id'])
                    os.makedirs('udemy'+'/'+primary_folder+'/'+chapter+'/'+chapter_index+'_'+str(reset_value)+'_'+i['title'])
                    pq_r = PyQuery(requests.get('https://www.udemy.com/api-2.0/users/me/subscribed-courses/'+str(course)+'/lectures/'+str(i['id'])+'?fields%5Basset%5D=@min,download_urls,external_url,slide_urls,status&fields%5Bcourse%5D=id,is_paid,url,has_autogenerated_captions&fields%5Blecture%5D=@default,view_html,course,can_give_cc_feedback,can_see_cc_feedback_popup&page_config=ct_v4&tracking_tag=ctp_lecture',headers=headers1).json()['view_html'])
                    
                    
                    #print 'b'
                    #print str(pq_r('react-video-player').attr('text-tracks'))
                    print json.loads(str(pq_r('react-video-player').attr('text-tracks')))[0]['src'].split('?')[0]
                    urllib.urlretrieve(json.loads(str(pq_r('react-video-player').attr('text-tracks')))[0]['src'].split('?')[0], 'udemy'+'/'+primary_folder+'/'+chapter+'/'+chapter_index+'_'+str(reset_value)+'_'+i['title']+'/'+chapter+'_'+str(reset_value)+'_'+i['title']+'.vtt')
                    vtt_file = open('udemy'+'/'+primary_folder+'/'+chapter+'/'+chapter_index+'_'+str(reset_value)+'_'+i['title']+'/'+chapter+'_'+str(reset_value)+'_'+i['title']+'.vtt').read()
                    vtt_file_write = open('udemy'+'/'+primary_folder+'/'+chapter+'/'+chapter_index+'_'+str(reset_value)+'_'+i['title']+'/'+chapter+'_'+str(reset_value)+'_'+i['title']+'.txt','a')
                    for m in re.findall(r'(?P<text>.*?)\n\n', vtt_file+'\n\n'):
                        vtt_file_write.write(m+'\n\n')
                    reset_value+=1
            except Exception as e:
                print e
    cu+=1
    # course_id = str(get_course_id(course))
    # print course_id
    # subscribe(course_id)
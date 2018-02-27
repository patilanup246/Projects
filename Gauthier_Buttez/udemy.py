import requests
from pyquery import PyQuery
import json, re
import os
import urllib

def get_course_id(course_url):
    headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-GB,en;q=0.9,en-US;q=0.8,fr;q=0.7,es;q=0.6",
    'cache-control': "max-age=0",
    'cookie': "ud_firstvisit=2017-06-23T18:55:55.461860+00:00:1dOTkJ:WY2XqecxQcOehOyCoJOpJnh8wjQ; __ssid=398d3243-e4e4-44d6-a7ff-898fd6c19c93; IR_PI=1498244157553-q4zrmr989lr; existing_user=true; optimizelyEndUserId=oeu1498244194449r0.3478516657705435; optimizelyBuckets=%7B%7D; _ga=GA1.1.2004580025.1498244157; ki_r=; _ga=GA1.2.2004580025.1498244157; __udmy_2_v57r=8693e451b3574b22aff387981ba148df; __udmyvstr=a6669421bf9fb59ad18528fcaac67735; EUCookieMessageShown=true; EUCookieMessageState=initial; ki_u=2e55ca0b-1216-413a-d959-ec85; ki_s=179864%3A1.0.0.0.1; seen=1; _gid=GA1.2.470225827.1516627888; _gid=GA1.1.470225827.1516627888; IR_gbd=udemy.com; access_token=ENYRfyPwkhA0dX7WCWBxCxufKPiKFLaQMv2IQPMR; csrftoken=5FdzKL7qBn7Lvw6nc18VguVZdyVshHwO; dj_session_id=hcxkl7jlfmu8xc3dvwb0ej3gd39lrwh2; client_id=bd2565cb7b0c313f5e9bae44961e8db2; __ar_v4=VH5RDLCI7NHB5GFMJDUBVW%3A20180121%3A2%7COKLCQMMNANCRNGGEOKKR5M%3A20180121%3A2%7C554CPNW4XBAX5EYKBL4HVU%3A20180121%3A2; optimizelySegments=%7B%22306102099%22%3A%22gc%22%2C%22306155008%22%3A%22direct%22%2C%22306161004%22%3A%22false%22%2C%227473112303%22%3A%22none%22%2C%227518841116%22%3A%22false%22%2C%227514910721%22%3A%22Business%22%7D; IR_5420=1516628100388%7C0%7C1516627889634; ki_t=1498244158445%3B1516627895031%3B1516628100439%3B3%3B19; eva=\"SlFIIwxATzcTQht5XEBPfgZCGTxCQAY/XgFfY1QZV30BRB1jVFBCfAEOB2MdFVd2SlEacVlaV3YDRBt1E05XL10DCXsVQER8CUMJe1xVRXpMDg==\"; ud_rule_vars=eJx9zUEKgzAUBNCrhGxbJT8_0Z-cJSBRkxLaIo2xG_HuFWyhdNHVLIY3s_Li8yWUMHbPNKcyZUuNwaA09Khb1UvpY0RqDUHvQdEY7TBN1xS4ZXx1_Obn0g3TkudwLHQl3YPbW8elAKoEVFIyQIvKalMrbdCokxBWCMfP7L2Qw2MJe46-_GBomCCLYEHXmohk-41jyrs6jv9bhZIMfuzGtxfmgkZk:1edcFp:K_iqVzzSb4nl3goZJAFMvCBUxSk; _px2=eyJ1IjoiMGI5MGJjOTAtZmY3OS0xMWU3LTkzNTktMjMwMzJiNmI5OGZlIiwidiI6IjA4MmRmMTEwLTdiMWYtMTFlNi05NDdiLTBmZTU5YzMyNzM4MCIsInQiOjE1MTY2Mjk1MDQ1ODgsImgiOiI0NWJjNDUyMDk1NmIzODg4ZTAwNmIwMDMwMDA0NmE4NDQxODA3MDNhNDRkYmE4YTM4MDVjNDY3ODA2OTRiZGI5In0=; _px3=f88f9a9f06cbcf6a452382d299be98ef8fe2a6eb3693c8e2b2afe3ae4b2f8aa1:QWtAVIvENn7IRwNEokhfQA989MTFIiOlfBtviXmMLzL9ioEyYzuWgRJJNrSkEIygniQnHpGMCcoUzEcmwgKNVg==:1000:UnB60Fg9L5AnoSK4uRJiZ1celL+qTExtAJXy3c+Xm1iFKsudtPqBos0Ds5BxwVEiSWF5bvLJ3ykLDfA6Bye9hlLMeGAqmOvmKtNk0twS8TYVZNVkv0GO1naDoe5MCoffvPUbBss+kdFDNDikFv/yAx+9GrntTBwHyVTsUoAtmck=",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    #print requests.get(course_url,headers=headers).text
    pq = PyQuery(requests.get(course_url,headers=headers).text)
    #return pq('.rating [data-user-tracker-object-id]').attr('data-user-tracker-object-id')
    return pq('.rating [data-user-tracker-object-id]').attr('data-user-tracker-object-id') 
def subscribe(course_id):
    url = "https://www.udemy.com/course/subscribe/"

    querystring = {"courseId":course_id}
    
    headers_subscribe = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-GB,en;q=0.9,en-US;q=0.8,fr;q=0.7,es;q=0.6",
    'cookie': "ud_firstvisit=2017-06-23T18:55:55.461860+00:00:1dOTkJ:WY2XqecxQcOehOyCoJOpJnh8wjQ; __ssid=398d3243-e4e4-44d6-a7ff-898fd6c19c93; IR_PI=1498244157553-q4zrmr989lr; existing_user=true; optimizelyEndUserId=oeu1498244194449r0.3478516657705435; optimizelyBuckets=%7B%7D; _ga=GA1.1.2004580025.1498244157; ki_r=; _ga=GA1.2.2004580025.1498244157; __udmy_2_v57r=8693e451b3574b22aff387981ba148df; __udmyvstr=a6669421bf9fb59ad18528fcaac67735; EUCookieMessageShown=true; EUCookieMessageState=initial; ki_u=2e55ca0b-1216-413a-d959-ec85; ki_s=179864%3A1.0.0.0.1; seen=1; _gid=GA1.2.470225827.1516627888; _gid=GA1.1.470225827.1516627888; IR_gbd=udemy.com; access_token=ENYRfyPwkhA0dX7WCWBxCxufKPiKFLaQMv2IQPMR; csrftoken=5FdzKL7qBn7Lvw6nc18VguVZdyVshHwO; dj_session_id=hcxkl7jlfmu8xc3dvwb0ej3gd39lrwh2; client_id=bd2565cb7b0c313f5e9bae44961e8db2; __ar_v4=VH5RDLCI7NHB5GFMJDUBVW%3A20180121%3A2%7COKLCQMMNANCRNGGEOKKR5M%3A20180121%3A2%7C554CPNW4XBAX5EYKBL4HVU%3A20180121%3A2; optimizelySegments=%7B%22306102099%22%3A%22gc%22%2C%22306155008%22%3A%22direct%22%2C%22306161004%22%3A%22false%22%2C%227473112303%22%3A%22none%22%2C%227518841116%22%3A%22false%22%2C%227514910721%22%3A%22Business%22%7D; ki_t=1498244158445%3B1516627895031%3B1516629276945%3B3%3B20; _px2=eyJ1IjoiYzg4YWE4NDAtZmY3Yi0xMWU3LWFjN2QtN2ZkYWFkMzcyNGRjIiwidiI6IjA4MmRmMTEwLTdiMWYtMTFlNi05NDdiLTBmZTU5YzMyNzM4MCIsInQiOjE1MTY2Mjk3Nzk1MjMsImgiOiI3YzA0OGYzOWRmYTg3ZGYyNDgwMmJjNmQ1N2MxNTliYTkwMmJhNTVjNTI0NDVmYTA2MGJhNThkNzNjNjQ2ZDVmIn0=; _px3=f2b8e5540389ed533e6073afef0c2398e40dcd7d2f3fce074aa30e8fec88ddb9:uDV/QiE5+1AtAVpPzvX6AsCgAU+rwkqH2M4o930KBXirhzpouasNVhbrlpuA5iWh/6eQVq19VvNYYo94SrSUCA==:1000:o8gHzdLwQtwAh2iB2Ix9V2oO33Y9Wm8UvMEFcGhGSL5Sd0zYhVxe0HpyF7Zmi81sxi4Vm1dQsZ+mLXsyK5R5+Nckq4SREBW7UHztwpcUExn0zgUW8q93GPZFoXdzteflCx4rvW63/ZZm6TlEtdkcxE++JHsqFibG4LR1ugUuDkg=; ud_rule_vars=\"eJyFzc0KgzAQBOBXkVxbJZsf3eyzBCRqUkJbpEnsRXz3SqVQeul55ptZWXHp4ouf-mfMscyJsDXSKw2D1J0ahHAhSOwMwuBA4RRonOdr9Iwqtlp2c7n047yk7I-FvsS7t3tqmeCANYdaiAokaUVSNWAMB33inDi37Ly3Qkz7xGEnV34stBVHkkCgGyUFGvlt3-_JPxaf_2GNiKL74I1tL9SiRlY=:1edcYZ:rh6s-dDqUSxP9UYpJpJqT1Rg-u8\"; eva=\"SlFIIwxATzcTQht5XEBPfgZCGTxCQBYgQVEROkxTRXQBURFzWVJDMR1RWDZMWA5uAEMceUxYR3sBR1ZtTBEGI0MHCXsVQER8BkUJe1xVRXxMDg==\"; IR_5420=1516629281316%7C0%7C1516627889634; optimizelyPendingLogEvents=%5B%22n%3Dengagement%26u%3Doeu1498244194449r0.3478516657705435%26wxhr%3Dtrue%26time%3D1516629343.53%26f%3D8897772323%26g%3D305018473%22%5D",
    'referer': "https://www.udemy.com/personalbrand/",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    
    response = requests.request("GET", url, headers=headers_subscribe, params=querystring)
    
    
def get_videos_id(course_id):
    try:
        url = "https://www.udemy.com/api-2.0/courses/{}/cached-subscriber-curriculum-items".format(course_id)
        
        

        querystring = {"fields[asset]":"@min,title,filename,asset_type,external_url,length,status","fields[chapter]":"@min,description,object_index,title,sort_order","fields[lecture]":"@min,object_index,asset,supplementary_assets,sort_order,is_published,is_free","fields[practice]":"@min,object_index,title,sort_order,is_published","fields[quiz]":"@min,object_index,title,sort_order,is_published","page_size":"9999","fields%5Bquiz%5D":"@min,object_index,title,sort_order,is_published","fields%5Bpractice%5D":"@min,object_index,title,sort_order,is_published","fields%5Blecture%5D":"@min,object_index,asset,supplementary_assets,sort_order,is_published,is_free","fields%5Bchapter%5D":"@min,description,object_index,title,sort_order","fields%5Basset%5D":"@min,title,filename,asset_type,external_url,length,status"}

        headers = {
    'accept': "application/json, text/plain, */*",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-GB,en;q=0.9,en-US;q=0.8,fr;q=0.7,es;q=0.6",
    'authorization': "Bearer ENYRfyPwkhA0dX7WCWBxCxufKPiKFLaQMv2IQPMR",
    'cookie': "ud_firstvisit=2017-06-23T18:55:55.461860+00:00:1dOTkJ:WY2XqecxQcOehOyCoJOpJnh8wjQ; __ssid=398d3243-e4e4-44d6-a7ff-898fd6c19c93; IR_PI=1498244157553-q4zrmr989lr; existing_user=true; optimizelyEndUserId=oeu1498244194449r0.3478516657705435; optimizelyBuckets=%7B%7D; _ga=GA1.1.2004580025.1498244157; ki_r=; _ga=GA1.2.2004580025.1498244157; __udmy_2_v57r=8693e451b3574b22aff387981ba148df; __udmyvstr=a6669421bf9fb59ad18528fcaac67735; EUCookieMessageShown=true; EUCookieMessageState=initial; ki_u=2e55ca0b-1216-413a-d959-ec85; ki_s=179864%3A1.0.0.0.1; seen=1; _gid=GA1.2.470225827.1516627888; _gid=GA1.1.470225827.1516627888; IR_gbd=udemy.com; access_token=ENYRfyPwkhA0dX7WCWBxCxufKPiKFLaQMv2IQPMR; csrftoken=5FdzKL7qBn7Lvw6nc18VguVZdyVshHwO; dj_session_id=hcxkl7jlfmu8xc3dvwb0ej3gd39lrwh2; client_id=bd2565cb7b0c313f5e9bae44961e8db2; __ar_v4=VH5RDLCI7NHB5GFMJDUBVW%3A20180121%3A2%7COKLCQMMNANCRNGGEOKKR5M%3A20180121%3A2%7C554CPNW4XBAX5EYKBL4HVU%3A20180121%3A2; optimizelySegments=%7B%22306102099%22%3A%22gc%22%2C%22306155008%22%3A%22direct%22%2C%22306161004%22%3A%22false%22%2C%227473112303%22%3A%22none%22%2C%227518841116%22%3A%22false%22%2C%227514910721%22%3A%22Business%22%7D; IR_5420=1516629347118%7C0%7C1516627889634; ki_t=1498244158445%3B1516627895031%3B1516629347163%3B3%3B21; _px2=eyJ1IjoiZjJjN2YzNjAtZmY3Yi0xMWU3LWE1NjktZjVmYTA3NDljYjEzIiwidiI6IjA4MmRmMTEwLTdiMWYtMTFlNi05NDdiLTBmZTU5YzMyNzM4MCIsInQiOjE1MTY2Mjk4NDkyMzksImgiOiJjOTAzZTFhNzkyZTkwN2UzNGU3ZTU3Mzg1YTJiYTRiNjI0ZWIwYzZmN2Y2NjdhZTRkMzcxNDBhYWQ3ODYzOTgxIn0=; _px3=88d80501ee134e0f8f8a71b6fa8befc6aff0c4eb92e9a2a03c1c9d78fb5614da:b8UuK/Kf8UHksZrELzRefUgHOH+9nqntfaPB+4giI6wqPtKU93infJsbSZLldWWn2uenYwvKkQaDKxInI42P2g==:1000:q616mIiuLnJMYU1k+y+zAkrkSn+DmB/hKkTxwLr6DobtHfxMp+FLhvzJv5bK1SKzFd065EzzQBdIUTLZgrQrsQV5URdVvz33KpP9Q1/c8ubUZ70UL7dW0RywHBy7UNCgQowXh2LvMysawyksGzFqb8rKJAh2acTSG8mHMNT3G+w=; ud_rule_vars=\"eJyFjcsKgzAURH9Fsm2Ve_PQm3xLQKImJbRFGmM34r83SAulm65mMXPObCy7dPHZT_0zLjHPyVCrhZcKB6E6OXDuQhDUacLBoaQpmHGer9EzU7HNsptbcp_8Y_UlJ5e9LYVlHJBqwBrbCsgINKgaRUS8OwEYAMvOZRViKtRx_IeVgpMW3-xxPM5rWvzbkOP9x8B5hcIoaYRsUGtA9THsbH8BdMRGVg==:1edccV:kaOnDWYHtsBJbUE1KeqLmHF15_k\"; eva=\"SlFILR5ATzcTQht5XkBPfgZDHTxCQBYuU1EROkxTRXQDURFzWVNHMR1RWDZMWA5uAEMceUxYR3sBR1ZtTBEGI0MHCXsVQER8BkUJe1xVRXxMDg==\"",
    'referer': "https://www.udemy.com/personalbrand/learn/v4/overview",
    'user-agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'x-requested-with': "XMLHttpRequest",
    'x-udemy-authorization': "Bearer ENYRfyPwkhA0dX7WCWBxCxufKPiKFLaQMv2IQPMR"
    }
        
        response = requests.request("GET", url, headers=headers, params=querystring)
        #print (response.json())
        return (response.json()['results'])
        
    except Exception as e:
        print (e)
        return []
o_course_id_file = open('udemy_courses_id.txt','w')
for course in open('udemy_courses.txt','r').read().split('\n'):
    course_id = str(get_course_id(course))
    o_course_id_file.write (course_id)
    o_course_id_file.flush()
    print (course_id)
    subscribe(course_id)
o_course_id_file.close()
headers1 = {
    'accept': "application/json, text/plain, */*",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-GB,en;q=0.9,en-US;q=0.8,fr;q=0.7,es;q=0.6",
    'authorization': "Bearer ENYRfyPwkhA0dX7WCWBxCxufKPiKFLaQMv2IQPMR",
    'cookie': "ud_firstvisit=2017-06-23T18:55:55.461860+00:00:1dOTkJ:WY2XqecxQcOehOyCoJOpJnh8wjQ; __ssid=398d3243-e4e4-44d6-a7ff-898fd6c19c93; IR_PI=1498244157553-q4zrmr989lr; existing_user=true; optimizelyEndUserId=oeu1498244194449r0.3478516657705435; optimizelyBuckets=%7B%7D; _ga=GA1.1.2004580025.1498244157; ki_r=; _ga=GA1.2.2004580025.1498244157; __udmy_2_v57r=8693e451b3574b22aff387981ba148df; __udmyvstr=a6669421bf9fb59ad18528fcaac67735; EUCookieMessageShown=true; EUCookieMessageState=initial; ki_u=2e55ca0b-1216-413a-d959-ec85; ki_s=179864%3A1.0.0.0.1; seen=1; _gid=GA1.2.470225827.1516627888; _gid=GA1.1.470225827.1516627888; IR_gbd=udemy.com; access_token=ENYRfyPwkhA0dX7WCWBxCxufKPiKFLaQMv2IQPMR; csrftoken=5FdzKL7qBn7Lvw6nc18VguVZdyVshHwO; dj_session_id=hcxkl7jlfmu8xc3dvwb0ej3gd39lrwh2; client_id=bd2565cb7b0c313f5e9bae44961e8db2; __ar_v4=VH5RDLCI7NHB5GFMJDUBVW%3A20180121%3A2%7COKLCQMMNANCRNGGEOKKR5M%3A20180121%3A2%7C554CPNW4XBAX5EYKBL4HVU%3A20180121%3A2; optimizelySegments=%7B%22306102099%22%3A%22gc%22%2C%22306155008%22%3A%22direct%22%2C%22306161004%22%3A%22false%22%2C%227473112303%22%3A%22none%22%2C%227518841116%22%3A%22false%22%2C%227514910721%22%3A%22Business%22%7D; IR_5420=1516629347118%7C0%7C1516627889634; ki_t=1498244158445%3B1516627895031%3B1516629347163%3B3%3B21; _px2=eyJ1IjoiZjJjN2YzNjAtZmY3Yi0xMWU3LWE1NjktZjVmYTA3NDljYjEzIiwidiI6IjA4MmRmMTEwLTdiMWYtMTFlNi05NDdiLTBmZTU5YzMyNzM4MCIsInQiOjE1MTY2Mjk4NDkyMzksImgiOiJjOTAzZTFhNzkyZTkwN2UzNGU3ZTU3Mzg1YTJiYTRiNjI0ZWIwYzZmN2Y2NjdhZTRkMzcxNDBhYWQ3ODYzOTgxIn0=; _px3=88d80501ee134e0f8f8a71b6fa8befc6aff0c4eb92e9a2a03c1c9d78fb5614da:b8UuK/Kf8UHksZrELzRefUgHOH+9nqntfaPB+4giI6wqPtKU93infJsbSZLldWWn2uenYwvKkQaDKxInI42P2g==:1000:q616mIiuLnJMYU1k+y+zAkrkSn+DmB/hKkTxwLr6DobtHfxMp+FLhvzJv5bK1SKzFd065EzzQBdIUTLZgrQrsQV5URdVvz33KpP9Q1/c8ubUZ70UL7dW0RywHBy7UNCgQowXh2LvMysawyksGzFqb8rKJAh2acTSG8mHMNT3G+w=; ud_rule_vars=\"eJyFjcsKgzAURH9Fsm2Ve_PQm3xLQKImJbRFGmM34r83SAulm65mMXPObCy7dPHZT_0zLjHPyVCrhZcKB6E6OXDuQhDUacLBoaQpmHGer9EzU7HNsptbcp_8Y_UlJ5e9LYVlHJBqwBrbCsgINKgaRUS8OwEYAMvOZRViKtRx_IeVgpMW3-xxPM5rWvzbkOP9x8B5hcIoaYRsUGtA9THsbH8BdMRGVg==:1edccV:kaOnDWYHtsBJbUE1KeqLmHF15_k\"; eva=\"SlFILR5ATzcTQht5XkBPfgZDHTxCQBYuU1EROkxTRXQDURFzWVNHMR1RWDZMWA5uAEMceUxYR3sBR1ZtTBEGI0MHCXsVQER8BkUJe1xVRXxMDg==\"",
    'referer': "https://www.udemy.com/personalbrand/learn/v4/overview",
    'user-agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'x-requested-with': "XMLHttpRequest",
    'x-udemy-authorization': "Bearer ENYRfyPwkhA0dX7WCWBxCxufKPiKFLaQMv2IQPMR"
    }
courses_url = open('udemy_courses.txt','r').read().split('\n')
cu = 0
#print ('I am here')
for course in open('udemy_courses_id.txt','r').read().split('\n'):
    primary_folder = PyQuery(requests.get(courses_url[cu],headers=headers1).text)('title').text().split('|')[0].strip()
    print (primary_folder)
    #reset_value=1 
    for i in get_videos_id(course):
        if i['_class'] == 'chapter':
            chapter_index = str(i['object_index'])
            chapter = str(i['object_index'])+'_'+i['title']
            print (chapter)
            reset_value = 1
        else:
            try:
                if i['asset']['asset_type'] == 'Video':
                    print (courses_url[cu]+str(i['id']))
                    course_name = primary_folder
                    chapter_name = chapter
                    video_name = chapter_index+'_'+str(reset_value)+'_'+i['title']
                    try:
                        course_name1= course_name[0:20].strip().replace('<','').replace('>','').replace(':','').replace('"','').replace('/','').replace('\\','').replace('|','').replace('?','').replace('*','')
                    except Exception as e:
                        course_name1= course_name.strip().replace('<','').replace('>','').replace(':','').replace('"','').replace('/','').replace('\\','').replace('|','').replace('?','').replace('*','')
                    try:
                        chapter_name1 = chapter_name[0:20].strip().replace('<','').replace('>','').replace(':','').replace('"','').replace('/','').replace('\\','').replace('|','').replace('?','').replace('*','')
                    except Exception as e:
                        chapter_name1 = chapter_name.strip().replace('<','').replace('>','').replace(':','').replace('"','').replace('/','').replace('\\','').replace('|','').replace('?','').replace('*','')
                    try:
                        video_name1 =video_name[0:20].strip().replace('<','').replace('>','').replace(':','').replace('"','').replace('/','').replace('\\','').replace('|','').replace('?','').replace('*','')
                    except Exception as e:
                        video_name1 =video_name.strip().replace('<','').replace('>','').replace(':','').replace('"','').replace('/','').replace('\\','').replace('|','').replace('?','').replace('*','')
                    os.makedirs('udemy'+'/'+course_name1+'/'+chapter_name1+'/'+video_name1)
                    pq_r = PyQuery(requests.get('https://www.udemy.com/api-2.0/users/me/subscribed-courses/'+str(course)+'/lectures/'+str(i['id'])+'?fields%5Basset%5D=@min,download_urls,external_url,slide_urls,status&fields%5Bcourse%5D=id,is_paid,url,has_autogenerated_captions&fields%5Blecture%5D=@default,view_html,course,can_give_cc_feedback,can_see_cc_feedback_popup&page_config=ct_v4&tracking_tag=ctp_lecture',headers=headers1).json()['view_html'])
                    
                    
                    #print 'b'
                    #print str(pq_r('react-video-player').attr('text-tracks'))
                    vtt_file_path = json.loads(str(pq_r('react-video-player').attr('text-tracks')))[0]['src'].split('?')[0]
                    print (vtt_file_path)
                    vtt_filename = chapter_name1+'_'+str(reset_value)+'_'+i['title']
                    vtt_filename = vtt_filename.strip().replace('<','').replace('>','').replace(':','').replace('"','').replace('/','').replace('\\','').replace('|','').replace('?','').replace('*','')
                    urllib.request.urlretrieve(vtt_file_path, 'udemy'+'/'+course_name1+'/'+chapter_name1+'/'+video_name1+'/'+vtt_filename+'.vtt')
                    vtt_file = open('udemy'+'/'+course_name1+'/'+chapter_name1+'/'+video_name1+'/'+vtt_filename+'.vtt').read()
                    vtt_file_write = open('udemy'+'/'+course_name1+'/'+chapter_name1+'/'+video_name1+'/'+vtt_filename+'.txt','a')
                    file_path = open('udemy'+'/'+course_name1+'/'+chapter_name1+'/'+video_name1+'/'+'filepath.txt','w')
                    file_path.write('udemy'+'-->'+course_name+'-->'+chapter_name+'-->'+video_name)
                    for m in re.findall(r'(?P<text>.*?)\n\n', vtt_file+'\n\n'):
                        vtt_file_write.write(m+'\n\n')
                    reset_value+=1
            except Exception as e:
                print (e)
    cu+=1
    # course_id = str(get_course_id(course))
    # print course_id
    # subscribe(course_id)
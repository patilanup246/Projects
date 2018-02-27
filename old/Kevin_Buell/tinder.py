# -*- coding: UTF-8 -*-
'''
Create - 11 May 2017
Author - 

'''


import requests
import urllib,sys,os
import math
import argparse
import logging
import json
from datetime import datetime
from random import shuffle
import time
from random import randint
facebook_connecting = "Connecting to Facebook"





parser = argparse.ArgumentParser()
#parser.add_argument("-H", "--help", help="Enter a number", type=int)
parser.add_argument("-W", "--max_wait", help="The maximum number of seconds to wait before each event (each interaction w/ Tinder). Actual wait shall be a random number of seconds between 0 - NUMBER, and shall differ for each event", type=int)
parser.add_argument("-O", "--output_log", help="Logs program output to file ", type=bool)
parser.add_argument("-D", "--debug", help="Produce verbose, detailed output suitable for debugging", type=bool)
parser.add_argument("-C", "--cards", help="Whether to Like/Ignore cards", type=bool)
parser.add_argument("-S", "--max_cards_swipe", help="Maximum number of cards to swipe(Like/Ignore)", type=int)
parser.add_argument("-L", "--like", help="Percent share of cards to Like (swipe right). The rest (1-?) are ignored (swiped left)", type=int)
parser.add_argument("-M", "--messages", help="Whether to send message to new contacts", type=bool)
parser.add_argument("-F", "--file_message", help="File containing the message to send to new contacts", type=str)
parser.add_argument("-I", "--save_images", help="Whether to save images", type=bool)

args = parser.parse_args()

maximum_wait  = args.max_wait if args.max_wait else 5
output_logging = args.output_log if args.output_log else False
debugging = args.debug if args.debug else False
cards = args.cards if args.cards else False
max_cards_swipe = args.max_cards_swipe if args.max_cards_swipe else 11
like = args.like if args.like else False
messages = args.messages if args.messages else False
file_message = args.file_message if args.file_message else None
save_images = args.save_images if args.save_images else False

if debugging:
    logging.basicConfig(filename='tinder_execution_log_debug.log',level=logging.DEBUG)
if output_logging:
    logging.basicConfig(filename='tinder_execution_log_info.log',level=logging.INFO)
#logging.basicConfig(filename='tinder_execution_log_error.log',level=logging.ERROR)

def random_waits():
    wait_s = randint(0,maximum_wait)
    print 'Random wait - '+str(wait_s) + ' s'
    time.sleep(wait_s)
    logging.info('Random wait - '+str(wait_s) + ' s')

def get_auth_token():
    random_waits()
    logging.info(facebook_connecting)
    print(facebook_connecting)
    url = "https://api.gotinder.com/v2/auth/login/facebook"
    
    headers = {
    'user-agent': "Tinder Android Version 6.11.0",
    'os-version': "23",
    'app-version': "2082",
    'platform': "android",
    'accept-language': "en",
    'content-type': "application/json; charset=UTF-8",
    'content-length': "302",
    'host': "api.gotinder.com",
    'connection': "Keep-Alive",
    'accept-encoding': "gzip",
    'cache-control': "no-cache"
    }
    data = {
    "token": "EAAGm0PX4ZCpsBANUi0qwZCZC0zzWEWfxqwYXYggD1GFRhZC5EvzsTqnNCFnVsJdQHjwVWoKA3ztcYjvBC5iAc1c8Ah4095B3SUuZCDf6ov2ZC1YSGs2nNftjl40ZAX0dPpbN869MbxAjuVdWcqSTZASYuktfcnZBkFfNYxVDjt9LXYkEEvXuOkmiYMSTGLmzjsEfHZB9VyEqH9kQZDZD"
    }
    
    
    response = requests.request("POST", url, json=data, headers=headers)

    auth_key = ''
    try:
        auth_key = response.json()['data']['api_token']
    except KeyError,e:
        print 'Facebook authentication failed. Get new facebook token from https://gist.github.com/taseppa/66fc7239c66ef285ecb28b400b556938'
    
    return auth_key




recs_url = 'https://api.gotinder.com/recs/core?locale=en'
meta_url = 'https://api.gotinder.com/meta'
profile_url = 'https://api.gotinder.com/v2/profile?include=boost'
updates_url = 'https://api.gotinder.com/updates'

profile_details = []
like_pass_urls = []

swipe_count = 0

file_images = open('file_images.txt','a')
#i=1


 
logging.info('Starting execution - ')
print 
logging.info(str(datetime.now()))

headers = {
    'platform': "android",
    'user-agent': "Tinder Android Version 6.11.0",
    'os-version': "23",
    'accept-language': "en",
    'app-version': "2082",
    'connection': "Keep-Alive",
    'accept-encoding': "gzip",
    'if-none-match': "W/\"-380394419\"",
    'x-auth-token': get_auth_token(),
    'cache-control': "no-cache"
    }

file_profile = open('file_profile.txt','w')



for swipes in xrange(int(math.ceil(max_cards_swipe/11.0))):
    
    response = requests.request("GET", recs_url, headers=headers)
    
    random_waits()
    
    try:
        recs = response.json()
        #file_profile.write(json.dumps(recs))
        #file_profile.flush()
        recs['results']
    except KeyError, e:
        logging.warning('x-auth-token has expired')
        logging.error(e)
        sys.exit()
    
    print 'Getting profiles ...'
    random_waits()
    logging.info('Getting profiles ...')
    for profile in recs['results']:
        logging.info(json.dumps(profile))
        random_waits()
        swipe_count+=1
        user_profile = profile['user']
         
        print 'Profile - {}'.format(str(swipe_count))
         
        try:
            print '\t\t Name : {}'.format(user_profile['name'].encode('ascii','ignore'))
        except Exception,e:
            logging.error(e)
        
        try:
            print '\t\t Id : {}'.format(user_profile['_id'])
        except Exception,e:
            logging.error(e) 
           
        try:
            print '\t\t Bio : {}'.format(user_profile['bio'].encode('ascii','ignore').replace('\n',''))
        except Exception,e:
            logging.error(e)    
         
        try:
            print '\t\t Distance from you : {} miles'.format(str(user_profile['distance_mi']).replace('\n',''))
        except Exception,e:
            logging.error(e)    
     
        try:
            print '\t\t Photos : {}'.format(', '.join(photo['url'] for photo in user_profile['photos']))    
            if save_images:
                if not os.path.exists('Images'):
                    os.makedirs('Images')
                for photo1 in user_profile['photos']:
                    photo1 = photo1['url']
                    urllib.urlretrieve(photo1, 'Images/'+photo1.replace('http://images.gotinder.com/','').rsplit('/')[1])
        except Exception,e:
            logging.error(e)
            
        try:
            print '\t\t Common Connections : {}'.format(user_profile['common_connections'])
        except Exception,e:
            logging.error(e)    
         
        try:
            print '\t\t Common Likes : {}'.format(user_profile['common_likes'])
        except Exception,e:
            logging.error(e)    
         
        try:
            print '\t\t Common Interests : {}'.format(', '.join(interest['name'] for interest in user_profile['common_interests']))
        except Exception,e:
            logging.error(e)    
         
        try:
            print '\t\t Common Friends : {}'.format(user_profile['common_friends'])
        except Exception,e:
            logging.error(e)    
        
        
        try:
            profile_details.append(user_profile['name']+' ('+user_profile['_id']+')')
            #like_urls.append('https://api.gotinder.com/like/{}?content_hash={}&s_number={}'.format(user_profile['_id'],user_profile['content_hash'],user_profile['s_number']))
            #pass_urls.append('https://api.gotinder.com/pass/{}?content_hash={}&s_number={}'.format(user_profile['_id'],user_profile['content_hash'],user_profile['s_number']))
            like_pass_urls.append('/{}?content_hash={}&s_number={}'.format(user_profile['_id'],user_profile['content_hash'],user_profile['s_number']))
        except Exception,e:
            logging.error(e)
        #print  requests.get('https://api.gotinder.com/pass/{}?content_hash={}&s_number={}'.format(user_profile['_id'],user_profile['content_hash'],user_profile['s_number']),headers=headers).json()
        #print requests.get(meta_url,headers=headers).text
        #sys.exit()
        #print 'Like Profile - Done. Likes Remaining - {} '.format(likes['likes_remaining'])
        #print 'Liked {}? - Successful'.format(user_profile['name'])
        print '\n\n' 
        
        
     
#print requests.get(meta_url,headers=headers).text
     
shuffled_likes = []
actual_profile_like = int(math.ceil((like/100.00)*swipe_count))

for i in xrange(actual_profile_like):
    shuffled_likes.append(True)

for i in xrange(swipe_count-actual_profile_like):
    shuffled_likes.append(False)
     

#shuffle(shuffle(shuffled_likes))
shuffle(shuffled_likes)
shuffle(shuffled_likes)
#print shuffled_likes
logging.info('shuffled_likes '+str(shuffled_likes))
if like:
    #actual_profile_like = int(math.ceil((like/100.00)*swipe_count))
    print 'You have specified to like {} (i.e {}%) out of {} profiles found'.format(str(actual_profile_like),str(like),str(swipe_count))
    logging.info('You have specified to like {} (i.e {}%) out of {} profiles found'.format(str(actual_profile_like),str(like),str(swipe_count)))
    for l,p,pd in zip(shuffled_likes,like_pass_urls,profile_details):
        random_waits()
        if l:
            try:   
                like_requests =  requests.get('https://api.gotinder.com/like'+p,headers=headers)
                logging.info(like_requests.text.encode('ascii','ignore'))
                if like_requests.json()['likes_remaining']:
                    print 'Liked profile -'+str(pd)+' Successful'
                    logging.info('Liked profile -'+str(pd)+' Successful')
            except Exception,e:
                print 'Couldnt like profiles. Check Logs'
                logging.error(e)
        else:
            try:       
                pass_requests = requests.get('https://api.gotinder.com/pass'+p,headers=headers)
                logging.info(pass_requests.text.encode('ascii','ignore'))
                if pass_requests.json()['status'] == 200:
                    print 'Pass profile -'+str(pd)+' Successful'
                    logging.info('Pass profile -'+str(pd)+' Successful')
            except Exception,e:
                print 'Couldnt pass profiles. Check Logs'
                logging.error(e)
                
 
if messages:
    random_waits()
    try:
        matches = requests.post(updates_url, headers=headers,data ='{}')
        logging.info('matches - '+matches.text) 
        logging.info('\n\nTotal matches found = '+str(len(matches.json()['matches']))) 
        print '\n\nTotal matches found = '+str(len(matches.json()['matches']))
        #for match in matches:
            #resp_message = requests.post()
            
    except Exception,e:
        logging.error(e)

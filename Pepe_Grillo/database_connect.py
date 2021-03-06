'''
Created on May 19, 2018

@author: tasneem
'''

import sqlite3
import linkedin_properties

def is_exists(linkedin_url):
    conn = sqlite3.connect('linkedin_database.db')
    cur = conn.execute("SELECT profile_url from profiles where profile_url = '{}'".format(linkedin_url))
    data = cur.fetchall()
    exists = False
    
    if len(data) == 0 :
        exists = False
    else:
        exists = True

    conn.close()
    
    return exists

def get_profiles():
    conn = sqlite3.connect('linkedin_database.db')
    profiles = []
    try:
        cur = conn.execute("SELECT profile_url from profiles")
        for row in cur:
            profiles.append(row[0])
    except Exception as e:
        print (e)
    
    conn.close()
    
    return profiles



def save_messages(details):
    conn = sqlite3.connect('linkedin_database.db')
    print ("INSERT INTO profile_info (name, firstname, job_alert_url, message_thread_no, profile_url, to_send, messages) \
                     VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(details[0], details[1], details[2], details[3], details[4], details[5], details[6]))
    conn.execute("INSERT INTO profile_info (name, firstname, job_alert_url, message_thread_no, profile_url, to_send, messages) \
                     VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(details[0], details[1], details[2], details[3], details[4], details[5], details[6]));
    conn.commit()
    conn.close()

def insert_profiles(profile_url, is_new_message):
    conn = sqlite3.connect('linkedin_database.db')
    try:
        if not is_exists(profile_url):
            conn.execute("INSERT INTO profiles (profile_url, has_new_message) \
                VALUES ('{}', {} )".format(profile_url, is_new_message));
        else:
            if is_new_message:
                conn.execute("UPDATE profiles SET has_new_message = 1 WHERE profile_url = '{}'".format(profile_url));
            
        
        conn.commit()
    except Exception as e:
        print (e)
    
    conn.close()

    
# def insert_profile(profiles):
#     conn = sqlite3.connect('linkedin_database.db')
#     try:
#         for profile in profiles:
#             if not is_exists(profile['linkedin_url']):
#                 
#                 names = profile['name'].split(' ',1)
#                 
#                 if len(names) > 1:
#                     firstname = names[0]
#                     lastname = names[1]
#                 else:
#                     firstname = names[0]
#                     lastname = names[0]
#                 
#                 
#                 
#                 conn.execute("INSERT INTO user_profile (firstname, lastname, linkedin_url, location, designation, is_connected, is_messaged, is_tried_message, is_tried_connect) \
#                     VALUES ('{}', '{}', '{}', '{}', '{}', 0, 0, 0, 0 )".format(firstname, lastname, profile['linkedin_url'], profile['location'], profile['designation']));
#                 conn.commit()
#     except Exception as e:
#         print (e)
#     
#     conn.close()


def get_connect_profiles():
    conn = sqlite3.connect('linkedin_database.db')
    profiles = []
    try:
        cur = conn.execute("SELECT linkedin_url from user_profile where is_connected = 0 and is_tried_connect = 0 LIMIT {}".format(linkedin_properties.MAX_PROFILES_TO_CONNECT))
        for row in cur:
            profiles.append(row[0])
    except Exception as e:
        print (e)
    
    conn.close()
    
    return profiles


def get_message_profiles():
    conn = sqlite3.connect('linkedin_database.db')
    profiles = []
    try:
        cur = conn.execute("SELECT linkedin_url, firstname from user_profile where is_connected = 1 and is_messaged = 0 and is_tried_message = 0 LIMIT {}".format(linkedin_properties.MAX_PROFILES_TO_MESSAGE))
        for row in cur:
            profiles.append((row[0],row[1]))
    except Exception as e:
        print (e)
    
    conn.close()
    
    return profiles



def update_connect_profile(linkedin_url,success):
    conn = sqlite3.connect('linkedin_database.db')
    if success:
        try:
            conn.execute("UPDATE user_profile SET is_connected = 1  WHERE linkedin_url = '{}'".format(linkedin_url))
            conn.execute("UPDATE user_profile SET is_tried_connect = 1 WHERE linkedin_url = '{}'".format(linkedin_url))
            conn.commit()
        except Exception as e:
            print (e)
        
    else:
        try:
            
            conn.execute("UPDATE user_profile SET is_connected = 0 WHERE linkedin_url = '{}'".format(linkedin_url))
            conn.execute("UPDATE user_profile SET is_tried_connect = 1 WHERE linkedin_url = '{}'".format(linkedin_url))
            conn.commit()
        except Exception as e:
            print (e)
    
    conn.close()
    
def update_message_profile(linkedin_url,success):
    conn = sqlite3.connect('linkedin_database.db')
    if success:
        try:
            conn.execute("UPDATE user_profile SET is_messaged = 1  WHERE linkedin_url = '{}'".format(linkedin_url))
            conn.execute("UPDATE user_profile SET is_tried_message = 1 WHERE linkedin_url = '{}'".format(linkedin_url))
            conn.commit()
        except Exception as e:
            print (e)
        
    else:
        try:
            
            conn.execute("UPDATE user_profile SET is_messaged = 0 WHERE linkedin_url = '{}'".format(linkedin_url))
            conn.execute("UPDATE user_profile SET is_tried_message = 1 WHERE linkedin_url = '{}'".format(linkedin_url))
            conn.commit()
        except Exception as e:
            print (e)
    
    conn.close()
    
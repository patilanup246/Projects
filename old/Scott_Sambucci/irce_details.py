'''
Created on May 18, 2017

@author: Mukadam
'''
import requests
from pyquery import PyQuery
file_speaker = open('speaker_info.txt','w')
resp_speakers = requests.get('http://irce.a2zinc.net/IRCE2017/Public/speakers.aspx')

pq_speakers = PyQuery(resp_speakers.text)

for speaker in pq_speakers('.media-body a'):
    print speaker.text
    
    resp_speaker_profile = requests.get('http://irce.a2zinc.net/IRCE2017/Public/'+speaker.attrib['onclick'].replace("javascript:window.location ='","")[:-1])
    pq_speaker_profile = PyQuery(resp_speaker_profile.text)
    
    speaker_sessions = []
    info = ''
    info += pq_speaker_profile('.media-heading').text().encode('ascii','ignore') + '\t'
    info += pq_speaker_profile('.SpeakerTitle').text().encode('ascii','ignore') + '\t'
    info += pq_speaker_profile('.SpeakerCompany').text().encode('ascii','ignore') + '\t'
    info += pq_speaker_profile('contactprofile').text().replace('\n', '').replace('\r', '').encode('ascii','ignore') + '\t'
    
    for session in pq_speaker_profile('.fa-ul a'):
        speaker_sessions.append('http://irce.a2zinc.net/IRCE2017/Public'+session.attrib['href'].encode('ascii','ignore'))
    
    info += str(speaker_sessions)
    
    print info 
    
    file_speaker.write(info+'\n')
    file_speaker.flush()
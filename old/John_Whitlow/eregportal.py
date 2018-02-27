import requests
import yagmail
import time
import sys

user_from = 'baltimoremdjohn@gmail.com'
user_pass = 'PassW0rd69'
user_to = 'baltimoremdjohn@gmail.com'

while True:
    url = "https://eregportal.helpresearch.com/PivotalUX/api/Form/Load/"

    querystring = {"form":"gAAAAAAAA1o=","metadata":"0","recordId":"AAAAAAAFwCQ="}
    f_read = open('current_study.txt')
    payload = "{\"parameterList\":[{\"value\":\"\",\"type\":\"System.String\"},{\"value\":\"\",\"type\":\"System.String\"},{\"value\":[[],[]],\"type\":\"System.Object[,]\"},{\"value\":\"\",\"type\":\"System.String\"},{\"value\":null,\"type\":\"System.Object\"},{\"value\":[],\"type\":\"System.Object[]\"}],\"id\":\"AAAAAAAFwCQ=\"}"
    headers = {
        'authorization': "bearer dc625a7165244771afeab5b18a3d68565d016eb32b3b468f9b1838ea9aeecf68e049b4047bde48df92ff05f4781622e2",
        'content-type': "application/json",
        'pivotalenvironmentname': "Production"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    #print(response.text)
    existing_study_list = f_read.read().split(',')
    fetched_study_list = []
    fetched_study_desc = []
    new_study_list = []
    try:
        for study in response.json()['payload']['data']['primary']['MatchingStudies__Secondary']:
            study_id = study['Study_Group']
            fetched_study_list.append(study_id)
            fetched_study_desc.append(study['CL_Study_Group_Id__Rn_Descriptor'])
            if not study_id in existing_study_list:
                new_study_list.append(study['CL_Study_Group_Id__Rn_Descriptor'])
    except Exception,e:
        yagmail.SMTP(user_from, user_pass).send(user_to, 'New Studies','Sign-In failed')
        sys.exit()

    f_read.close()

    if new_study_list:
        text = "New Studies - \n" + '\n'.join(new_study_list)

        text += '\n\nFetched Studies - \n' + '\n'.join(fetched_study_desc)

        yagmail.SMTP(user_from, user_pass).send(user_to, 'New Studies', text)

    f_write = open('current_study.txt','w')
    #','.join(list(set(fetched_study_list+existing_study_list)))
    f_write.write(','.join(list(set(fetched_study_list+existing_study_list))))
    f_write.close()




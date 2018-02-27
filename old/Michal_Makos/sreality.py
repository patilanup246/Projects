import requests


i=1
f_out = open('sreality','w')
while True:
    r = requests.get('https://www.sreality.cz/api/cs/v2/companies?page='+str(i)).json()
    print (i)
    if r['_embedded']['companies']:
        for c in r['_embedded']['companies']:
            f_out.write (c['url']+'/'+str(c['id']))
            f_out.flush()
    else:
        break
    i+=1

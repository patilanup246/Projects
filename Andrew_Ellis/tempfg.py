import json
f = open('C:\\Users\\Administrator\\Desktop\\temp_delete.txt').read()
print (f)
j = json.loads(f)
for i in j:
    print ('"'+str(i['id'])+'":"'+i['name']+'",')
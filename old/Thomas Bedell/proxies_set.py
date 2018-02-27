import requests
for i in xrange(10):
    print requests.get('https://api.proxicity.io/v2/proxy?httpsSupport=true').json()['ipPort']
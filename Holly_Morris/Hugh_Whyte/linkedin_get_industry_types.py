'''
Created on May 9, 2017

@author: Mukadam
'''
'''
Last Finding - The industry codes varies from 1 to 148 except 2

'''


import requests

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
headers = {
    'accept': "application/vnd.linkedin.normalized+json",
    'cookie': "bcookie=\"v=2&d2dcf2f4-2537-4feb-88ff-b52230db61cc\"; bscookie=\"v=1&201705031540523b8a7068-3525-488d-8283-fff58f865f0fAQF1o6JsAJDisi3v0q1AnmPk-oa4HG_9\"; visit=\"v=1&M\"; li_at=AQEDAQdhrlYAAYj0AAABW88J_uMAAAFb7w1UY1YArktdIdXJj74dV5r68UK3LGZQeGhjy7pDNs7QlMql1xUZg7bvTbB9SMXIEBUQd4Z_thtrp1_YCwGhCPiH0nednJ5HFhhOYVnXOJwc5mEXY4tP6aG5; liap=true; sl=\"v=1&ucHiv\"; JSESSIONID=\"ajax:5198578620785389827\"; _ga=GA1.2.852648120.1493827549; lidc=\"b=SB34:g=8:u=100:i=1494335513:t=1494412311:s=AQEObpXkdHOJlyG0mHFtF1r0-twm9SnF\"; li_a=AQJ2PTEmc2FsZXNfY2lkPTI4MDQ5MDgwOSUzQSUzQTgzMjQ4MzA5GVogw5YsGHmJsPC1xRCLuZBcBs8; lang=\"v=2&lang=en-us\"; sdsc=22%3A1%2C1494335890029%7ECAOR%2C0Aauf0eowzg%2B%2BfX2O3HImRXcDROw%3D; _lipt=CwEAAAFb7XLnJ4S38AfhsrE-OWkEOZocDE_Ik4dojrXD39KxVCCfHnbznlQAN5nyL2gpzwMUo8rLIw42dZbuqvfemY1aNtzEpVltbbZ-Id_jkVlrhaUimJtmV6zuXNKtAsJsJ_E6FjpYFWGTWXBf50gbS4_UmsfhHrwF0IZlefKlNqDDi4oh41obFhXao-DMXZgCflyCu3X4L9gVDzaD51tPNwq4CuOPP-wAk-OdK80TTkHj3nuPWFkCJTjLFQMiszw9vDgb1bsyJMxRKUab13TEM2ETPgMt37CuUcqE-W80Wv-Vwkz_l6lAi0E3C_mXMNSzwkExxGIg73Of1jmIB4BklqgcczdmXhucZIZ_WNsUtjJcJPLiwaUV1oMLDUogOux4St5SeHHMvkG7D_6qR9PYn08GoJR2BbeEqcuN5lZjhRPiZQGFg99roo-bkr5QMTn5ag",
    'csrf-token': "ajax:5198578620785389827",
    'x-restli-protocol-version': "2.0.0"
    }
print 'start '
for alphabet in alphabets:
    response = requests.request("GET", 'https://www.linkedin.com/voyager/api/typeahead/hits?q=federated&query={}&types=List(INDUSTRY)'.format(alphabet), headers=headers)
    #print len(response.json()['included'])
    for industry in response.json()['included']:
        try:
            print industry['backendUrn']
        except KeyError,e:
            pass
    
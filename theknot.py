# -*- coding: utf-8 -*-
'''
Created on Aug 23, 2018

@author: talib
'''
import requests

# url = "https://prod-marketplace-api.localsolutions.theknot.com/graphql"
# o= open('abc.txt','w',encoding='utf-8')
# offset = 0
# while True:
#     payload = {"query":"\n  query(\n    $categoryGuid: String!,\n    $city: String,\n    $filters: [String],\n    $isSeo: Boolean,\n    $limit: Int,\n    $offset: Int,\n    $seed: String!\n    $sort: [SortInput!],\n    $state: String,\n  ){\n    search(\n      filters: $filters,\n      isSeo: $isSeo,\n      limit: $limit,\n      location: { city: $city, state: $state },\n      offset: $offset,\n      seed: $seed\n      sort: $sort\n    ) {\n      marketCode\n      profiles {\n        ...ProfileProperties\n      }\n      total {\n        profiles\n      }\n      supplemental {\n        ...ProfileProperties\n      }\n    }\n    filterSummary(categoryGuid: $categoryGuid) {\n      name\n      filters {\n        name\n        isSingleSelect\n        slug\n        filterOptions {\n          id\n          name\n          display {\n            patternsIconClass\n          }\n          singular {\n            slug\n            term\n          }\n        }\n      }\n    }\n    ads(categoryGuid: $categoryGuid, location: { city: $city, state: $state }) {\n      adSummaries {\n        count\n        badgeId\n        badgeCode\n      }\n      tierSummaries {\n        count\n        tierCode\n      }\n    }\n  }\n  \n  fragment ProfileProperties on Storefront {\n    id\n    vendorId\n    accountId\n    accountStatus\n    name\n    displayId\n    description\n    headline\n    websiteUrl\n    displayWebsiteUrl\n    purchaseStatus\n    claimedStatus\n    adTier\n    salesProfiles {\n      vendorTier\n      marketCode\n      addOns {\n        code\n        name\n      }\n    }\n    addOns {\n      code\n    }\n    vendorTier\n    movedProfileId\n    location {\n      address {\n        address1\n        address2\n        city\n        state\n        postalCode\n        latitude\n        longitude\n        isPublic\n      }\n      serviceArea\n    }\n    mediaSummary {\n      total\n    }\n    storefrontCard {\n      height\n      id\n      mediaType\n      url\n      width\n    }\n    logo {\n      url\n    }\n    reviewSummary {\n      count\n      overallRating\n    }\n    siteUrls {\n      siteId\n      siteName\n      uri\n      relativeUri\n    }\n    categories {\n      code\n      name\n      displayName\n    }\n    marketCode\n    settings {\n      pricing\n      enhancedRFQ\n    }\n    facets {\n      id\n      name\n      ...facetsRecurse\n    }\n    affiliates {\n      id\n      name\n      description\n      singular {\n        slug\n        term\n      }\n      plural {\n        slug\n        term\n      }\n      isSelected\n      ...affiliatesRecurse\n    }\n    categoryInfo {\n      plural {\n        slug\n        term\n      }\n   }\n}\n\nfragment affiliatesRecurse on Affiliates {\n  affiliates {\n    ...affiliateFields\n    affiliates {\n      ...affiliateFields\n      affiliates {\n        ...affiliateFields\n          affiliates {\n            ...affiliateFields\n          }\n      }\n    }\n  }\n}\n\nfragment affiliateFields on Affiliates {\n  id\n  name\n  description\n  singular {\n    slug\n    term\n  }\n  plural {\n    slug\n    term\n  }\n  isSelected\n}\n\nfragment facetsRecurse on Facets {\n  facets {\n    ...facetFields\n    facets{\n      ...facetFields\n      facets {\n        ...facetFields\n        facets {\n          ...facetFields\n          facets {\n              ...facetFields\n              facets {\n                  ...facetFields\n                  facets {\n                      ...facetFields\n                  }\n              }\n          }\n        }\n      }\n    }\n  }\n}\n\nfragment facetFields on SubFacet {\n  id\n  name\n  description\n  singular {\n    slug\n    term\n  }\n  plural {\n    slug\n    term\n  }\n  isSelected\n}\n\n\n","variables":{"categoryGuid":"a520ad92-ff3f-4869-a382-92c87a5d809e","city":"","filters":["a520ad92-ff3f-4869-a382-92c87a5d809e"],"isSeo":'false',"limit":150,"offset":offset,"seed":"2018082218","state":""}}
#     headers = {
#         'accept': "application/json, text/plain, */*",
#         'accept-encoding': "gzip, deflate, br",
#         'accept-language': "en-US,en;q=0.9",
#         'connection': "keep-alive",
#         'content-length': "3929",
#         'content-type': "application/json;charset=UTF-8",
#         'host': "prod-marketplace-api.localsolutions.theknot.com",
#         'origin': "https://www.theknot.com",
#         'referer': "https://www.theknot.com/marketplace/wedding-photographers-new-york-ny?offset=66",
#         'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
#         }
#     
#     response = requests.request("POST", url, json=payload, headers=headers)
#     
#     r = response.json()
#     
#     if not r['data']['search']['profiles']:
#         break
#     
#     for a in r['data']['search']['profiles']:
#         o.write (a['siteUrls'][0]['uri']+'\n')
#         
#     print (offset)
#     offset+=150


import re, time
import webbrowser
i = 1
for a in open('theknot_list.txt',encoding='utf-8').read().split('\n')[100:]:
    
    if i%5 ==0 :
        time.sleep(10)
    webbrowser.open_new_tab(a)
    i+=1
#     r = requests.get(a)
#     
#     print (r.text)
#     
#     print (re.findall('"emails":\[{"address":"(.*?)"', r.text))
from pyquery import PyQuery
import requests
import xmltodict
import json
import csv
input_urls = open('input_urls.txt').read().split('\n')


def get_data(data_part,reportype, cik, filename,wr):
    
    
    
    
    if type(data_part)==list:
        for ndh in data_part:
            details = []
            details.append('https://www.sec.gov/Archives/edgar/data/{}/{}'.format(cik,filename))
            details.append(cik)
            details.append(filename)
            details.append(reportype)
            try:
                details.append (ndh.get('securitytitle',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (ndh.get('conversionorexerciseprice',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (ndh.get('transactiondate',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (ndh.get('deemedexecutiondate','').get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (ndh.get('transactioncoding',{}).get('transactionformtype',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (ndh.get('transactioncoding',{}).get('transactioncode',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (ndh.get('transactioncoding',{}).get('equityswapinvolved',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (ndh.get('transactiontimeliness',{}).get('value',''))
            except Exception as e:
                details.append ('')
                
                
            try:    
                details.append (ndh.get('transactionamounts',{}).get('transactionshares',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (ndh.get('transactionamounts',{}).get('transactiontotalvalue',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (ndh.get('transactionamounts',{}).get('transactionpricepershare',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (ndh.get('transactionamounts',{}).get('transactionacquireddisposedcode',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (ndh.get('exercisedate',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (ndh.get('expirationdate',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (ndh.get('underlyingsecurity',{}).get('underlyingsecuritytitle',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (ndh.get('underlyingsecurity',{}).get('underlyingsecurityshares',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (ndh.get('underlyingsecurity',{}).get('underlyingsecurityvalue',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (ndh.get('posttransactionamounts',{}).get('sharesownedfollowingtransaction',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (ndh.get('posttransactionamounts',{}).get('valueownedfollowingtransaction',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (ndh.get('ownershipnature',{}).get('directorindirectownership',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (ndh.get('ownershipnature',{}).get('natureofownership',{}).get('value',''))
            except Exception as e:
                details.append ('')
            
            wr.writerow(details)
            
    else:
        if data_part:
            details = []
            details.append('https://www.sec.gov/Archives/edgar/data/{}/{}'.format(cik,filename))
            details.append(cik)
            details.append(filename)
            details.append(reportype)
            try:
                details.append (data_part.get('securitytitle',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (data_part.get('conversionorexerciseprice',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (data_part.get('transactiondate',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (data_part.get('deemedexecutiondate','').get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (data_part.get('transactioncoding',{}).get('transactionformtype',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (data_part.get('transactioncoding',{}).get('transactioncode',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (data_part.get('transactioncoding',{}).get('equityswapinvolved',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (data_part.get('transactiontimeliness',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:    
                details.append (data_part.get('transactionamounts',{}).get('transactionshares',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (data_part.get('transactionamounts',{}).get('transactiontotalvalue',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (data_part.get('transactionamounts',{}).get('transactionpricepershare',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (data_part.get('transactionamounts',{}).get('transactionacquireddisposedcode',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (data_part.get('exercisedate',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (data_part.get('expirationdate',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (data_part.get('underlyingsecurity',{}).get('underlyingsecuritytitle',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (data_part.get('underlyingsecurity',{}).get('underlyingsecurityshares',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (data_part.get('underlyingsecurity',{}).get('underlyingsecurityvalue',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (data_part.get('posttransactionamounts',{}).get('sharesownedfollowingtransaction',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (data_part.get('posttransactionamounts',{}).get('valueownedfollowingtransaction',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (data_part.get('ownershipnature',{}).get('directorindirectownership',{}).get('value',''))
            except Exception as e:
                details.append ('')
            try:
                details.append (data_part.get('ownershipnature',{}).get('natureofownership',{}).get('value',''))
            except Exception as e:
                details.append ('')
            
            wr.writerow(details)
    

output_f = open('sec_export.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['URL',
            'CIK',
            'FileName',    'RecordType',    'securityTitle',    'conversionOrExercisePrice',
                 'transactionDate',    'deemedExecutionDate',    'transactionFormType',    'transactionCode',    'equitySwapInvolved', 
                    'transactionTimeliness',    'transactionShares',    'transactionTotalValue',    'transactionPricePerShare',  
                      'transactionAcquiredDisposedCode',    'exerciseDate',    'expirationDate',    'underlyingSecurityTitle',    'underlyingSecurityShares', 
                'underlyingSecurityValue',    'sharesOwnedFollowingTransaction',    'valueOwnedFollowingTransaction',    'directOrIndirectOwnership', 'natureOfOwnership'])

for url in input_urls:#reversed(input_urls):#['https://www.sec.gov/Archives/edgar/data/1105078/0001127602-17-021121.txt']:
    print (url)
    r = requests.get(url).text
    pq = PyQuery(r)

    
     
    j = json.loads(json.dumps(xmltodict.parse(str(pq('XML').children()).replace('??>','?>'))))
    #print (json.dumps(j))
    try:
        nonDerivativeHolding        =   j.get('ownershipdocument',{}).get('nonderivativetable',{}).get('nonderivativeholding')
    except:
        pass    
    
    try:
        derivativeHolding           =   j.get('ownershipdocument',{}).get('derivativetable',{}).get('derivativeholding')
    except:
        pass
    
    try:
        nonderivativetransaction    =   j.get('ownershipdocument',{}).get('nonderivativetable',{}).get('nonderivativetransaction')
    except:
        pass
    
    try:
        derivativeTransaction       =   j.get('ownershipdocument',{}).get('derivativetable',{}).get('derivativetransaction')
    except:
        pass
    

    
    CIK = url.replace('https://www.sec.gov/Archives/edgar/data/','').split('/')[0]
    FileName= url.replace('https://www.sec.gov/Archives/edgar/data/','').split('/')[1]
    
    get_data(nonDerivativeHolding,'nonDerivativeHolding',CIK,FileName,wr)
    get_data(derivativeHolding,'derivativeHolding',CIK,FileName,wr)
    get_data(nonderivativetransaction,'nonderivativetransaction',CIK,FileName,wr)
    get_data(derivativeTransaction,'derivativeTransaction',CIK,FileName,wr)
        

    

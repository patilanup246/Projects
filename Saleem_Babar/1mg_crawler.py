'''
Created on 31-Dec-2017

@author: Administrator
'''
import requests
from pyquery import PyQuery
input_file =  open('1mg_input.txt').read().split('\n')
output_file = open('1mg_output.txt','w',encoding='utf-8')
for drug in input_file:
    try:
        r = requests.get(drug).text
        pq = PyQuery(r)
        if '/otc/'  in  drug:
            drug_name =             str(pq('[class^="ProductTitle__product-title___"]').text())
            drug_company =          str(pq('[class^="ProductTitle__manufacturer___"]').text())
            drug_salt =             str('')
            drug_prescription =     str('')
            drug_price =            str(pq('[class^="OtcPriceBox__box___"] div[style="font-size:30px;display:block;font-weight:bold;color:#212121;"]').text())
            drug_quantity =         str('')
            drug_availability =     str(pq('[class^="AvailableStatus__container___"]').text())
            drug_uses =             str('')
            drug_uses_content =     str('')
            drug_side_effects =     str('')
            drug_consumption =      str('')
            drug_interaction =      str('')
        else:
            drug_name =             str(pq('[class^="DrugInfo__drug-name-heading___"]').text())
            drug_company =          str(pq('[class^="DrugInfo__company-name___"]').text())
            drug_salt =             str(pq('[class^="saltInfo DrugInfo__salt-name___"]').text())
            drug_prescription =     str(pq('[class^="col-xs-4 DrugInfo__prescription-requirement___"]').text())
            drug_price =            str(pq('[class^="DrugPriceBox__price___"]').text())
            drug_quantity =         str(pq('[class^="DrugPriceBox__quantity___"]').text())
            drug_availability =     str(pq('[class^="DrugPriceBox__add-box___"]').text())
            drug_uses =             str(pq('[class^="DrugInfo__uses___"]').text())
            drug_uses_content =     str(pq('[class^="DrugUses__content___"]').text())
            drug_side_effects =     str(pq('[class^="DrugSideEffects__content___"] p').text())
            drug_consumption =      str(pq('[class^="DrugConsumption__content___"]').text())
            drug_interaction =      str(pq('[class^="MedicineInteraction__text___"]').text())
        
        print (drug_name)
        o = drug_name + '\t'+ drug_company + '\t'+ drug_salt    + '\t'+ drug_prescription + '\t'+ drug_price     + '\t'+ drug_quantity + '\t'+ drug_availability    + '\t'+ drug_uses + '\t'+ drug_uses_content    + '\t'+ drug_side_effects + '\t'+ drug_consumption    + '\t'+ drug_interaction+'\n'
        
        output_file.write(o)
        output_file.flush()
    except Exception as e:
        print (e)
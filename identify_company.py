'''
Method to identify the company and call the needed module
'''



def identify_company(txt):
    
    from fuzzywuzzy import fuzz
    from jain import arrange_dump
    from unitron import unitron
    from table_extract import extract
    from sherays import Sheryas
    
    
    list_of_companies = ['SINo Particular Batch Expiry Date HSN/SAC Actual Qty Billed Qty Rate Discount Amount','Description of Goods HSN/SAC Quantity Rate per Amount',
    'MKTD NO. RATE AMOUNT']

    lst = []
    for i in list_of_companies:
        lst.append(fuzz.token_set_ratio(i.lower(),txt.lower()))
            
    i  = lst.index(max(lst))
   
    table = extract(txt)
    print("Table extracted")
    
    if i == 0:
        table.pop(0)
        #print(table)
        unitron(table)

    elif i == 1:
        table.pop(0)
        arrange_dump(table)

    elif i == 2:
        table.pop(0)
        table.pop(1)
        Sheryas(table)


    return
        

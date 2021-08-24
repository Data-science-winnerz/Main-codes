'''
Method to identify the company and call the needed module
'''
def identify_company(txt):
    from jain import arrange_dump
    from unitron2 import unitron
    from table_extract import extract
    from sherays import Sheryas
    
    
    list_of_companies = ['Unitron','JAINCHEMICALS','REYAS SURGICALS']

    for i,name in enumerate(list_of_companies):
        if txt.rfind(name)>-1:
            
            if i == 0:
            
                print('Company name',list_of_companies[0])
                table = extract(txt)
                table.pop(0)
                print("Table extracted")
                unitron(table)
            
            elif i == 1:

                print('Company name',list_of_companies[1])
                table = extract(txt)
                print("Table extracted")
                table.pop(0)
                arrange_dump(table)
            elif i == 2:
                print('Company name',list_of_companies[2])
                table = extract(txt) 
                print("Table extracted")
                print(table)
                table.pop(0)
                Sheryas(table)


    return
        
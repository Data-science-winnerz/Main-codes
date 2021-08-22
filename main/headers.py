'''
Method to identify the company and call the needed module
'''
def identify_company(txt):
    from jain import arrange_dump

    from unitron2 import unitron
    from table_extract import clean_extract

    list_of_companies = ['Unitron','JAINCHEMICALS']
    for i in list_of_companies:
        if txt.rfind(i) > 0 :
            
            if list_of_companies.index(i) == 0:
            
                print('Company name',list_of_companies[0])
                table = clean_extract(txt=txt)
                print("Table extracted")
                unitron(table)
            
            elif list_of_companies.index(i) == 1:

                print('Company name',list_of_companies[1])
                table = clean_extract(txt=txt)
                print("Table extracted")
                arrange_dump(table)
        else: 
            print('Company not found')
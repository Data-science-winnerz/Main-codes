
''''
This module is to convert the rows of Unitron into a table and store the json file
'''


def unitron(A):
    
    import json
    from utilites import listToString, rev_sentence
    
    # Intializing
    d=['SINo', 'Particular', 'Batch', 'Expiry Date', 'HSN/SAC', 'Actual Qty', 'Billed Qty', 'Rate', 'Discount', 'Amount']
    org=['SINo', 'Particular', 'Batch', 'Expiry Date', 'HSN/SAC', 'Actual Qty', 'Billed Qty', 'Rate', 'Discount', 'Amount']
    n=len(org)
    c=[]
    a = ''
    file = open('Unitron.json','a')



    for t in A:
        a = t.split(' ')
        a = a[::-1]
        a.insert(1,' ')

        for i in range(n):

            if i==8:
                c.append(a[i])
                i=i+1
                ##print(c)
                for j in range(len(a)):
                    if a[i].isdigit():
                        break
                    else:
                        c.append(a[i])
                        del(a[i])
                        #i=i+1

                y=listToString(c)
                w=rev_sentence(y)
                org[1]=w
            else:
                org[n-i-1] = a[i]


        c = []
        dict_from_list = dict(zip(d, org))
        ##print(dict_from_list)
        json_object = json.dump(dict_from_list, file,indent = 4)  
        #print(json_object)
    file.close()

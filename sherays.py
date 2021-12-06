
''''
This module is to convert the rows of Shreyas Surgicals into a table and store the json file
'''

def Sheryas(Shreya):
    
    import json
    from utilites import listToString,rev_sentence
    
    # Intializing the necessary elements
    file = open('Sherya Surgical.json','a')
    a = ['MFD','ITEM DESCRIPTION','PKG','QTY','HSN','BATCH','EXP','MRP','SALE RATE','VALUE','DISC','TAX','NET AMOUNT']
    o = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    

   

# Iterating through each row and fitiing it into respective columns
    for g in range(len(Shreya)):
        shreya = Shreya[g]
        shreya = shreya.replace("  "," ")
        shreya = shreya.split(" ")
        
        if shreya[-1]==".":
            del shreya[-1]
        shreya.reverse()
        n=len(o)
        c=[]
        for i in range(n):
            if i==11:
                c.append(shreya[i])
                i=i+1
                for j in range(6):
                    c.append(shreya[i])
                    del(shreya[i])
                y=listToString(c)
                w=rev_sentence(y)
                o[1]=w
            else:
                o[n-i-1] = shreya[i]
        ##print(o)

        dict_from_list = dict(zip(a,o))
        ##print(dict_from_list)
        json_object = json.dump(dict_from_list, file,indent = 4)  
    
    file.close()


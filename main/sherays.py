

def Sheryas(Shreya):
    
    import json
    a = ['MFD','ITEM DESCRIPTION','PKG','QTY','HSN','BATCH','EXP','MRP','SALE RATE','VALUE','DISC','TAX','NET AMOUNT']
    o = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    

    def listToString(s): 
        str1 = " " 
        return (str1.join(s))

    def rev_sentence(sentence): 

        words = sentence.split(' ') 
        reverse_sentence = ' '.join(reversed(words)) 
        return reverse_sentence

    for g in range(len(Shreya)):
        shreya = Shreya[g]
        shreya = shreya.replace("  "," ")
        shreya = shreya.split(" ")

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
        #print(o)

        dict_from_list = dict(zip(a,o))
        #print(dict_from_list)
        json_object = json.dumps(dict_from_list, indent = 4)  
        print(json_object)



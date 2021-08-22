
def Fairdeal_Pharma(op):
    import json
    d = ['MFR', 'QTY', 'FREE', 'DESCRIPTION', 'PKG', 'BATCH', 'EXP.', 'HSN', 'MRPs', 'RATE', 
    'DIS%', 'VALUE', 'GST%', 'GST AMT.']
    org = ['MFR', 'QTY', 'FREE', 'DESCRIPTION', 'PKG', 'BATCH', 'EXP.', 'HSN', 'MRPs', 'RATE', 
    'DIS%', 'VALUE', 'GST%', 'GST AMT.']

    def listToString(s): 
        str1 = " " 
        return (str1.join(s))

    def rev_sentence(sentence): 

        words = sentence.split(' ') 
        reverse_sentence = ' '.join(reversed(words)) 
        return reverse_sentence 

    for i in range(len(op)):
        h=op[i]
        h=h.replace("  "," ")
        a=h.split(" ")
        a = [string for string in a if string != ""]

        a.reverse()
        #rint(d)
        #print(a)

        n=len(d)
        m=len(a)
        i=0
        while i<m:
            if i==0:
                org[n-1]=a[i]
                i=i+1
            elif i==10:
                p=[]
                j=i
                while j<m:
                    if a[j].isdigit():
                        j=j+1
                        break
                    else:
                        p.append(a[j])
                        j=j+1
                #print(len(p))
                k=len(p)
                y=listToString(p)
                w=rev_sentence(y)
                #print(w)

                org[n-i-1]=w
                #print(org)
                #print(i)
                i=i+len(p)
            elif i>10:
                org[n-i+1]=a[i]
                i=i+1
            else:
                org[n-i-1] = a[i]
                i=i+1
        #print(org)

        dict_from_list = dict(zip(d, org))
        #print(dict_from_list)
        json_object = json.dumps(dict_from_list, indent = 4)  
        print(json_object)


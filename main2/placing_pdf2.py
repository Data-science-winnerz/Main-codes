import json
d = ['MFD', 'QTY', 'PKG','FREE', 'DESCRIPTION', 'HSN Code', 'BATCH', 'EXP.','MRP', 'RATE', 
'VALUE','DIS%', 'GST%', 'NET AMT.']
org = ['MFD', 'QTY', 'PKG','FREE', 'DESCRIPTION', 'HSN Code', 'BATCH', 'EXP.','MRP', 'RATE', 
'VALUE','DIS%', 'GST%', 'NET AMT.']
op = ['WIN 50 010ml  MULTIVITAMIN.INJ 30045090 MA7G36 12/18 25.00 12.78 639.00 12.00 715.68',
 "SGKL l 0  1x2's ABGEL REGULAR 30061000 110616 10/19 250.00 189.61  189.61  12.00  212.37",
 "SGKL l 0  1x2's ABGEL REGULAR 30061000 080717 07/20 250.00 189.61  189.61 12.00  212.37",
 'ROMS‘ 10 0  Pcs VACCU SUCTION SET 90189099 17062314 05/22 338.00 98.60  986.00 12.00  1104.32',
 'ALKEN  50 0  Per Vail TAXIM1GM.INJ  30042019 7181018 11/19 34.09 24.36, 1218.00 12.00  1364.16',
 'ARI 150 0  Per Pc DIST.WATER 1OML 30049099  C271275 03/20 2.32 1.89  283.50 12.00 317.52',
 'ST 50 0 11x11 ABDOMINAL MOPS 30059040 106 06/20 44.00 24.78  1239.00 12.00  1387.68',
 'NEON 4 0  5xIml_ RIDOFF.INJ  30042019  43277 03/19 29.50 24.50 98.00 12.00  109.76',
 'NEON 10 0 5xIml_ EVATOCIN.INJ 30043911 _KPO9110 03/19 87.00 67.00  670.00 12.00  750.40']
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
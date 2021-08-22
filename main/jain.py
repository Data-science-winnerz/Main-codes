"""
To arrange the items as per the columns
"""




#num=['540.00', 'Nos', '45.00', '12Nos', 'LARGE', 'BAG', 'GARBAGE']
#num=['101.64', 'Nos', '8.47' ,'12Nos' ,'10','Soap','Boy','Life']

'''From Reverse:
1 ---> n=len(headers) ---> 6

num[0] ---> n   ---> headers[n-1]
num[1] ---> n-1 ---> headers[n-1-1]
num[2] ---> n-2 ---> headers[n-2-1]
num[3] ---> n-3 ---> headers[n-3-1]
num[4] ---> If it is a number then only insert or else leave it ---> n-4
num[4] ---> Concatenate the left out list elements and rev them ---> n-5 --->headers[n-5-1]

'''



def listToString(s): 
    str1 = " " 
    return (str1.join(s))

def rev_sentence(sentence): 
  
    words = sentence.split(' ') 
    reverse_sentence = ' '.join(reversed(words)) 
    return reverse_sentence 




   
        

def arrange_dump(contents):
    heads = ['Description of Goods', 'HSN/SAC', 'Quantity', 'Rate', 'per', 'Amount']
    
    import json
    import copy
    key_list = heads
    headers = copy.deepcopy(heads)

    final = []
    
    # Reverse sorting the list
    for i in contents:
        # Separating to individual contents
        temp = i.split(' ')
        temp = ' '.join(temp).split()        
        #print(temp)
        if len(temp) == 0:
            continue

        # Merging the quantity column
        try:
            #print(temp.index('Nos'))
            index_pos = temp.index('Nos')
        except ValueError:
            #print(temp.index('KGS'))
            index_pos = temp.index('KGS')
        k=(temp[index_pos-1]+temp[index_pos])
        # print(k)
        n=index_pos
        del temp[n-1:n+1]
        temp.insert(n-1,k)
        #print(temp)
        temp.reverse()
        #Storing the reversed list
        final.append(temp)



    
    file = open('bill.json','a')

    
      # file_out = open('bill.json','a')
    for st in final:
    
        n=len(headers)
        m=len(st)
        for i in range(n):
            if i==0:
                headers[n-1]=st[i]
            elif i==4:
                if st[i].isdigit():
                    headers[n-i-1] = st[i]
                    a=i+1
                else:
                    headers[n-i-1] = " "
                    a=i

            elif i==n-1:
                c=[]
                for i in range(a,m):
                    c.append(st[i])
                    y=listToString(c)
                    w=rev_sentence(y)
                    headers[0]=w

            else:
                headers[n-i-1] = st[i]

        #print(headers)

        
        dict_from_list = dict(zip(key_list, headers))   # json_object = json.dump(dict_from_list,file,indent = 4)  
        print(dict_from_list)
        json.dump(dict_from_list,file,indent=4)
    file.close()



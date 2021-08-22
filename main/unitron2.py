
def unitron(A):
    import json
    d=['SINo', 'Particular', 'Batch', 'Expiry Date', 'HSN/SAC', 'Actual Qty', 'Billed Qty', 'Rate', 'Discount', 'Amount']

    org=['SINo', 'Particular', 'Batch', 'Expiry Date', 'HSN/SAC', 'Actual Qty', 'Billed Qty', 'Rate', 'Discount', 'Amount']


    n=len(org)
    c=[]

    def listToString(s): 
        str1 = " " 
        return (str1.join(s))

    def rev_sentence(sentence): 

        words = sentence.split(' ') 
        reverse_sentence = ' '.join(reversed(words)) 
        return reverse_sentence 


    # for w in range(len(a)):
    #     a=a[w]
    #     a = a.split(" ")
    #     q=len(a)
    #     a.insert(q-1," ")
    #     a.reverse()
    #     print(a)
    #a=['1 Lyse 400ml, AbxMicro60 171019Y2 19Oct2018 38220019 1.00 1.00 4,257.00 4,257']
    #a=['1,925', ' ', '1,925.00', '1.00', '1.00', '38220019', '25Sep2018', '17091271', 'Micro60', 'Abx', '1It', 'Cleaner', '2']
    # a=['4,257', ' ', '4,257.00', '1.00', '1.00', '38220019', '19Oct2018', '171019Y2', 'AbxMicro60', '400ml,', 'Lyse', '1']

    a = ''
    for t in A:
        a = t.split(' ')
        a = a[::-1]
        a.insert(1,' ')

        for i in range(n):

            if i==8:
                c.append(a[i])
                i=i+1
                #print(c)
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
        #print(dict_from_list)
        json_object = json.dumps(dict_from_list, indent = 4)  
        print(json_object)


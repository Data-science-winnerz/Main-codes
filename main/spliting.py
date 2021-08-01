'''
Organizing the header names
'''

def head_extract(a):
    
    original_contents = ['Description of Goods', 'HSN/SAC', 'Quantity', 'Rate', 'per', 'Amount']

    b = a.split(" ")
    b.remove('')
    c=[]

    ''' a-->String
        b-->List'''

    # c=b[0]+" "+b[1]
    # print(c)
    for i in range(len(b)):
        if b[i] not in original_contents:
            q=b[i]+" "+b[i+1]
            if q not in original_contents:
                q=q+" "+b[i+2]
                if q not in original_contents:
                    q=q+" "+b[i+3]
                else:
                    c.append(q)
            else:
                c.append(q)
        else:
            c.append(b[i])
    return c


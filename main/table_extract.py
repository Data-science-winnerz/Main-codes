
'''
This module is used to clean the text and extract the table
'''


def Clean_Text(txt):

    import re  
    output = re.sub(r'[^ \nA-Za-z0-9/]+', '', txt)
    return output.split('\n')



def find_heading(clean):
    from fuzzywuzzy import fuzz
    to_find = 'SI NO Description Particular HSN Rate Amount'
    starting  = 0
    for t in clean:
        if (fuzz.token_set_ratio(to_find.lower(),t.lower())) > 70:
            starting = clean.index(t)
    
    
    return starting

def find_ending_serial(txt,loc):
    
    prev = 0
    t = ''
    
    for i in range(loc+1, len(txt)-1):
        temp = txt[i]
        
        if temp[0].isdigit() and int(temp[0]) == prev+1:
            
            print('item detected',temp)
            prev = int(temp[0])
            t = temp
        else:
            continue
    return (txt.index(t))

def find_ending(txt):
    from fuzzywuzzy import fuzz
    
    to_find = ['Recieved','output','FLASH']
    lst = []
    highestacc = -1
    index = -1
    
    for i in to_find:
        for t in txt:
            lst.append(fuzz.token_set_ratio(i.lower(),t.lower()))
    
        if highestacc < max(lst):
        
            index  = lst.index(max(lst))
            highestacc = max(lst)
            lst = []
       
        else:
            lst = []
            continue
       

    return index



def extract(txt):
    
    
    clean = Clean_Text(txt)  

    starting = find_heading(clean)
    ending = -1
    if 'SINo' in clean[starting]:
        print('SERIAL EXECUTED')
        ending = find_ending_serial(clean,starting) +2
 
    else:
        print('THE OTHER ONE EXECUTED')
        ending = find_ending(clean)
 
    print(starting)
    print(ending)
    
    # Extracting the rows of the table
    op = []
  
    for i in range(starting,ending-1):
        op.append(clean[i])
    return op



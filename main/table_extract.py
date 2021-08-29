
'''
This module is used to clean the text and extract the table
'''

# This method to clean the text
def Clean_Text(txt):

  
    Txt = txt.split('\n')
    bad_chars = ["'",'=','\n','|\n','|','~~','_ ï¿½\n','-','ï¿½','_ ï¿½','\x0c','�','?','#','$',';','~',
    '!','\\','""','(',')','“',']','}']

    clean = []
    for t in Txt:
        for i in bad_chars :
            t = t.replace(i,'')
        clean.append(t)

    return clean


   
# Method to extract the table

def extract(txt):
    
    from fuzzywuzzy import fuzz
    clean = Clean_Text(txt)
    # Detecting the headings
    to_find = 'SI NO Description Particular HSN Rate Amount'
    index  = 0
    for t in clean:
        if (fuzz.token_set_ratio(to_find.lower(),t.lower())) > 70:
            index = clean.index(t)

    # Extracting the rows of the table
    ending = int(input("Enter the number of rows in the table"))
    op = []
  
    for i in range(index,(index+ending+1)):
        op.append(clean[i])


    return op

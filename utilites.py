'''
This modules contain all the utility scripts that are commonly used across the modules

'''

def listToString(s): 
        str1 = " " 
        return (str1.join(s))

def rev_sentence(sentence): 

    words = sentence.split(' ') 
    reverse_sentence = ' '.join(reversed(words)) 
    return reverse_sentence
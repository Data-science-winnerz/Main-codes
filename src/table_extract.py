
from fuzzywuzzy import fuzz,process
import nltk

ending = int(input())
with open(r'E:\Projects\Data winnerz ocr\outputs\output_bw.txt','r') as file:
    txt = file.readlines()


# Cleaning the text
bad_chars = ['\n','|\n','|','~~','_ ï¿½\n','-','ï¿½','_ ï¿½','\x0c','�','?','#','$',';','~','!','\\','""','(',')']

clean = []
for t in txt:
    for i in bad_chars :
        t = t.replace(i,'')
    clean.append(t)

# #print(clean)


# Extracting the headings
to_find = 'Description Qty Rate Amount'


# highest = process.extractOne(to_find,clean)
# print(highest)


index = []
for t in clean:
    if (fuzz.token_set_ratio(to_find.lower(),t.lower())) > 80:
        index = clean.index(t)


op = []
for i in range(index,(index+ending+1)):
    op.append(clean[i])

print(op)

with open('something.txt','w') as file:
    for st in op:
        file.writelines(st+'\n') 
# # header = op.pop(0)

# revList = []

# for i in op:
#     i.split(' ')
#     revList.append(i[::-1])
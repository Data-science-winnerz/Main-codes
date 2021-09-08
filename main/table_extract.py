
'''
This module is used to clean the text and extract the table
'''


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


# lst =[ 'ORIGINAL FOR RECIPIENT', 'Oo CSalles TaxiInvoice  . ', 'Unitron Bio Medicals 201819', ', 464/1 , 12 Th Main,17th A Cross', 'oth Phase, J P Nagar , Bangalore 560078', ': 08025187600, 9449009531', 'Email:ubmh63@yahoo.in', ', Email: ', 'Pe _ _GSTIN No:28AOTPP1452J1ZB', 'To OO Invoice No  :UBMGST/3831 Date _: 18Jan2019', '_ Annasawmy Mudaliar General Hospital,Fazer Town Order No Order Date:', '1 ,Moore Market Square ,Bourdillon Road Despatched Through:', 'Frazer Town ,Bangalore560005 Sales Manager:', 'Ph:08042404111/4122, 08025806997 Delivery Person: Sridhar', '. SINo —_—Particular ____Batch Expiry Date HSN/SAC Actual Qty Billed Qty Rate Discount. Amount', '1 ‘Abx Control Normal MX415N  5Apr2019: 38220019 1.00 1.00 2,400.00: 2,400', '   , , :', '   , ,', ' :  ', '   :   ', '    ', ': . A toh  oy', ' :  Cer', 'te LAA FE', 'Te aoF', '  ', ' ir     1', ': NC 4  ', 'Reodit', ' Mac L  :  ', ' y :   : ', ' Kemer Pp', 'a we  :  a oe ee __ eum eS Se', '   Al fia  Total  1.00: 1.00  _ 2,400.00', ', Output CGST@6% : 144.00', 'Output SGST@6% 144.00', 'Grand Total 2,688.00', 'In Words: INR Two Thousand Six Hundred Eighty Eight  , , ', 'HSN/SAC Taxable Central Tax StateTax Total', ', _ Value Rate Amount:Rate Amount Tax Amount', '38220019 2,400.00: 6% 144.00 6% 144.00 288.00', ' Total 2,400.00 _ 144.00 144.00 288.00', ' Bank Details For, Unitgani@igeWiedicals 201819', '‘Bank Name _ : Kotak Mahendra Bank ke A', 'A/C Number  : 8411353920 is, la z', 'IFSC Code. >: KKBK0000433 2 [Baie ORE 9', 'Branch : J.P.Nagar Bangalore Authorisey jgnatory ', 'NAS A.', 'a  Terms & Conidition ised SF', '‘Payment Due On: 18Jan2019', 'Please pay by A/c Cheque/Draft Only ', 'Interest will be charged @24 % p.a, if not paid within 21 days.', ' ‘Goods once sold will not be taken back and subject to Bangalore Jurisdiction', '']
# # loc = 14
# # find_ending_serial(lst,loc)
# txt = "(ORIGINAL FOR RECIPIENT)\nOo CSalles TaxiInvoice | . |\nUnitron Bio Medicals 2018-19\n, #464/1 , 12 Th Main,17th A Cross\noth Phase, J P Nagar , Bangalore -560078\n: 080-25187600, 9449009531\nEmail:ubmh63@yahoo.in\n, Email: |\nPe _ _GSTIN No:28AOTPP1452J1ZB\nTo OO Invoice No  :UBMGST/3831 Date _: 18-Jan-2019\n_ Annasawmy Mudaliar General Hospital,Fazer Town Order No Order Date:\n#1 ,Moore Market Square ,Bourdillon Road Despatched Through:\nFrazer Town ,Bangalore-560005 Sales Manager:\nPh:08042404111/4122, 08025806997 Delivery Person: Sridhar\n. SINo —_—~Particular ____Batch Expiry Date HSN/SAC Actual Qty Billed Qty Rate Discount. Amount\n1 ‘Abx Control Normal MX415N ' 5-Apr-2019: 38220019 1.00 1.00 2,400.00: 2,400\n| | | , , :\n| | | , ,\n| : | |\n! | | : | | |\n| | ! | |\n: . A toh | oy)\n| : | Cer\nte LAA FE\nTe! \\ao'F\n| | |\n| ir | | | ! 1\n: NC 4 | |\nReodit\n| Mac L | : | |\n| y : ; ! : |\n| Kemer? Pp\na we | : = a oe ee __ eum eS Se\n| | ( Al “fia ! Total | 1.00: 1.00 ~ _ 2,400.00\n, Output CGST@6% =: 144.00\nOutput SGST@6% 144.00\nGrand Total 2,688.00\n'In Words: INR Two Thousand Six Hundred Eighty Eight | , , |\nHSN/SAC Taxable Central Tax StateTax Total\n, _ Value Rate Amount:Rate Amount Tax Amount\n38220019 2,400.00: 6% 144.00 6% 144.00 288.00\n| Total! 2,400.00 _ 144.00 144.00 288.00\n| Bank Details For, Unitgani@igeWiedicals 2018-19\n‘Bank Name _ : Kotak Mahendra Bank ke A\nA/C Number ~ : 8411353920 is, la z\nIFSC Code. >: KKBK0000433 \\2 [Baie ORE] 9\nBranch : J.P.Nagar Bangalore \\(Authorisey $jgnatory) ;\nNAS A“.\na | Terms & Conidition ised SF\n‘Payment Due On: 18-Jan-2019\nPlease pay by A/c Cheque/Draft Only |\nInterest will be charged @24 % p.a, if not paid within 21 days.\n| ‘Goods once sold will not be taken back and subject to Bangalore Jurisdiction\n\x0c"
# extract(txt)
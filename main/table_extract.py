
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
    ending = find_ending(clean)
    print(clean[ending])
   # Extracting the rows of the table
    op = []
  
    for i in range(starting,ending-1):
        op.append(clean[i])
    return op


find_ending(['naya NdmMand i H OMUDMaGITdstulu i BsA¢R BLN VY WEN Bs RAR VURAL BEBE SARC Cae', 'REYAS SURGICALS ANNASAWMY MUDALIAR GENERAL HOSP Inv. No.: S / 2090', 'fo. 9, 1st Flr, 60 ft. Rd., Pattegarapalya Main Rd., 1 MOORE MARKET SQUARE, Inv.Date : 17/01/2019 13:22:34', ', Vijayanagar North, Opp. S.H.K Kalyana Mantap BOURDILLION ROAD Due Date : 16022019', ' Bangalore  560079. FRAZER TOWN BANGALORE Sales Exe.: SUNIL  ¢', 'Mob No. 9740328085 / 9741771007 BANGALORE 560005 Mobile : 9741771007', 'Email : shreyassurgicals123@gmail.com PDL: :  Transport :', 'GST No. 29CHFPS0264Q1ZL :', 'DL No.: KAB4220B124715 KAB4221B124716 GST  : No OF C/B : 0', 'MEFD./ ITEM DESCRIPTION PKG QTY HSN BATCH EXP MRP  SALE  VALUE DISC  TAX NET ', 'MKTD NO. RATE % % AMOUNT', 'Ps  J &J VICRYL 30 NW 2328 C.C 90 CM  EACH 12  90189099 T8003 07/23" 594.00 436.59 5239.08 5.00 12.00 5574.39', '0 AI&S PROLENE 30 NW 018 C.C 70 CM  EACH 12  90189099 B6012 11/21,° 344.00 246.08 2952.96 5.00  12.00 3141.95', 'tp IE&IT PROLENE 40 NW 816 C.C  60 CM EACH 9 190189099 B6003.  11/2L. 324.00 238.00 2142.00 5.00 12.00 2279.08 .', 'DER’. 200H   ,', 'anneal', 'YeDauat focal ve , ,', '/ ny', ' @, Taken atodgtoats', 'ZO  1.', 'Lon ©:', '0 D oar d a CU', ' Po/ 208/314 i,', 'FLASH :J&J , SUTURE INDIA, LOTUS, QUILL ..All suture materials are available J&J loose pieces also available', 'Taxable CGSTS% CGST Amt SGSTS SGST Amt Exempted Free GROSS AMT 4 10334.04', '9817.34 6.00 589.04 6.00 589.04 0 DISC.AMT  516.70', 'GST AMT : 1178.08', 'ADDCRDBAMT — :', 'ROUND OFF : 0.42', 'POST.&CHQ.COMM: 0.00 Frieght : 0.00 Page No 1 NET PAYABLE  : 10995.00', 'Rs: Rupees Ten Thousand Nine Hundred Ninety Five Onl', ' E. & O.E. Subject to Bangalore Jurisdiction For SHREYAS SURGICALS', ' NOTE 1. Goods once sold cannot be taken back or exchanged Y', '2. Bills not paid within due date will attract 24% interest. OV', '3. In case of excess charges by oversight kindly bring to our notice for refund .', 'DECLARATION : We Certify that we are registered under VAT Act 2003 and liable to pay tax.', ': BANK DETAILS: STATE BANK OF INDIA, CURRENT A/C No: 34078766799, BRANCH: VIJAYNAGAR, IFSC CODE: SBIN0007985 Authorised Signatory', 'Page No. ', ''])
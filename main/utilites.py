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
'''
This is to detect and return the text
'''
def ocr(image):

    import pytesseract
    # Insert your pytesseract location here after installing
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    data = pytesseract.image_to_string(image, lang='eng',config='--psm 6')
    #print(data)
    return (data)


"""
This module is for converting the pdf to png and handle any rotation detection
"""

# This method is used to convert the pdf
def convo(path):
    from pdf2image import convert_from_path
    
    images = convert_from_path(path,dpi= 500, poppler_path=r'C:\Program Files\poppler-21.03.0\Library\bin')
    #images[0].save("sample.png",format = "PNG")
    
    return images[0]


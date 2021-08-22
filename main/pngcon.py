
"""
This module is for converting the pdf to png and handle any rotation detection
"""

# This method is used to convert the pdf
def convo(path):
    from pdf2image import convert_from_path
    
    images = convert_from_path(path,dpi= 500, poppler_path=r'C:\Program Files\poppler-21.03.0\Library\bin')
    #images[0].save("sample.png",format = "PNG")
    
    return images[0]



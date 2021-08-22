from tesseract_ocr import ocr
from preprocess import *
from pngcon import convo
from table_extract import clean_extract
from spliting_pdf2 import head_extract2
import numpy as np
import cv2



img = convo(r"C:\Users\Vishal\Desktop\Main-codes\Images\s4.pdf")
opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
print("Image conversion successful")


# # Getting the ocr

# txt = ocr(noise_removal(opencvImage))
# print("ocrd successfully")

# table = clean_extract(txt=txt)
# print("Table extracted")


# # For pdf 2
# #some kind of input

# arrange_dump(table,headers)
# # print('JSON created')
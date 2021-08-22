from tesseract_ocr import ocr
from preprocess import *
from pngcon import convo
from table_extract import clean_extract
from spliting import head_extract
from jain import arrange_dump
from fairdealpharam import Fairdeal_Pharma
from unitron2 import unitron
import numpy as np
import cv2



img = convo(r"C:\Users\Vishal\Desktop\Main-codes\Images\fairdeal.pdf")
opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
print("Image conversion successful")

# Getting the ocr
txt = ocr(blackandwhite(opencvImage))
print("ocrd successfully")

table = clean_extract(txt=txt)
print("Table extracted")

# # For pdf 1
table.pop(0)


Fairdeal_Pharma(table)
print('JSON created')


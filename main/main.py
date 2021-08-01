from tesseract_ocr import ocr
from preprocess import *
from pngcon import convo
from table_extract import clean_extract
from spliting import head_extract
from placing import arrange_dump
import numpy as np
import cv2



img = convo(r"E:\Projects\Data winnerz ocr\Images\sample.pdf")
opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
print("Image converted successfully")

# Getting the ocr
txt = ocr(noise_removal(opencvImage))
print("ocrd successfully")

table = clean_extract(txt=txt)
print("Table extracted")

h = table.pop(0)
headers = head_extract(h)
print('headers modified')

arrange_dump(table,headers)
print('JSON created')
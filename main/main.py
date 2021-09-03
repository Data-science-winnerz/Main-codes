'''
This is the main module
'''


from tesseract_ocr import ocr
from preprocess import *
from pngcon import convo
from identify_company import identify_company
import numpy as np
import cv2
import time


start_time = time.time()

img = convo(r"C:\Users\Vishal\Desktop\Main-codes\Images\unitron2.pdf")
opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
print("Image conversion successful")

# Getting the ocr
txt = ocr(blackandwhite(opencvImage))
print("ocrd successfully")

identify_company(txt=txt)
print("--- %s seconds ---" % (time.time() - start_time))
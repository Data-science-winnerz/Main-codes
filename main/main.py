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
from pathlib import Path


start_time = time.time()
folder = r"C:\Users\Vishal\Desktop\Main-codes\Images\unitron.png"

if (Path(folder).suffix == '.pdf'):
    img = convo(folder)
    opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

else:
    opencvImage = cv2.imread(folder)
print("Image conversion successful")

# Getting the ocr
txt = ocr(blackandwhite(opencvImage))
print("ocrd successfully")

identify_company(txt=txt)
print("--- %s seconds ---" % (time.time() - start_time))

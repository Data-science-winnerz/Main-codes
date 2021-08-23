from tesseract_ocr import ocr
from preprocess import *
from pngcon import convo
from headers import identify_company
import numpy as np
import cv2



img = convo(r"C:\Users\Vishal\Desktop\Main-codes\Images\unitron.pdf")
opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
print("Image conversion successful")

# Getting the ocr
txt = ocr(blackandwhite(opencvImage))
print("ocrd successfully")

identify_company(txt=txt)

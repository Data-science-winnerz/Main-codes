
from tesseract_ocr import ocr
from preprocess import *
from pngcon import convo
from identify_company import identify_company
import numpy as np
import cv2
import time
from pathlib import Path

start_time = time.time()
file = r"C:\xampp\htdocs\Android Tutorials\documents\myPDF.pdf"

if (Path(file).suffix == '.pdf'):
    img = convo(file)
    opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

else:
    opencvImage = cv2.imread(file)
print("Image conversion successful")

# Getting the ocr
txt = ocr(blackandwhite(opencvImage))
print("ocrd successfully")

identify_company(txt=txt)
print("--- %s seconds ---" % (time.time() - start_time))

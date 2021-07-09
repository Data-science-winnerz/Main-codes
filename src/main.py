from tesseract_ocr import ocr
from preprocess import *
# from keras import keras_oc
from pngcon import convo
import numpy as np
import cv2
img = convo(r'E:\Projects\Data winnerz ocr\Images\sample.pdf')
opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
ocr(blackandwhite(opencvImage))
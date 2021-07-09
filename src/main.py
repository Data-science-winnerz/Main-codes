from tesseract_ocr import ocr
from preprocess import *
from keras import keras_oc
from pngcon import convo

img = convo(r'E:\Projects\Data winnerz ocr\Images\sample.pdf')
ocr(blackandwhite(img))
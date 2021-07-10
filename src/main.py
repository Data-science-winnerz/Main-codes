from tesseract_ocr import ocr
from preprocess import *
# from keras import keras_oc
from pngcon import convo
import numpy as np
import cv2


img = convo("rotated.pdf")
opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

# Getting the ocr
txt = ocr(noise_removal(opencvImage))

# Saving the text
with open(r'E:\Projects\Data winnerz ocr\outputs\output3_no_noise.txt','w') as file:
    file.write(txt)


# import pandas as pd
# df = pd.read_csv('output_grayscale.txt',error_bad_lines=False)
# print(df)
# js = df.to_json('john.json',)

# print(js)
from __future__ import print_function
import cv2
import numpy as np
from datetime import date

import os
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)
today = date.today()
print("Today's date:", today)
name = input("Enter your name : ")
data = (name+today)
createFolder('./today + name/')
images = [np.random.randn(8, 12) for _ in range(50)]
stacked =  np.stack(images, axis=0)
print(stacked.shape)
h, status = cv2.findHomography(points1, points2)

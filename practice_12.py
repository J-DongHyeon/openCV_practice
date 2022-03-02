# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 17:44:48 2022

@author: jdh38
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('tv_2person.jpg')

cas = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

det = cas.detectMultiScale(img, scaleFactor = 1.3, minNeighbors = 3)

for i in range(0, len(det)) :
    pt1 = (det[i][0], det[i][1])
    pt2 = (det[i][0] + det[i][2], det[i][1] + det[i][3])
    cv2.rectangle(img, pt1, pt2, (0, 0, 255), 3)
    print(pt1, pt2)

plt.imshow(img[:,:,::-1])

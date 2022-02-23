# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 19:36:34 2022

@author: jdh38
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (0,0), (511, 511), (255, 0, 0), 10)
cv2.rectangle(img,(370,3), (510,135),(0,255,0),3)
cv2.circle(img, (440,70),60,(0,0,255),3)
cv2.circle(img, (440,50),30,(255, 255, 255),-1)
cv2.ellipse(img,(256, 256),(100,50),0,0,180,(0,0,255),-1)

pt0 = np.array([[100,5], [100,200], [200,200]], np.int32)
pt = pt0.reshape((-1, 1, 2))
cv2.polylines(img, [pt], True, (255,255,0), 2)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 1, (255,255,255),3,cv2.LINE_AA)
plt.imshow(img)
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 20:09:40 2022

@author: jdh38
"""

import numpy as np
import cv2
#import matplotlib.pyplot as plt

img = cv2.imread('Lenna.png', 0)

cv2.imshow('img', img)

key = cv2.waitKey(0)

if (key == 27) :
    cv2.destroyAllWindows()
elif (key == ord('s')) :
    cv2.imwrite('Lenna_saved.png', img)
    cv2.destroyAllWindows()

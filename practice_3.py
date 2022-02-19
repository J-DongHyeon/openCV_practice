# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:12:17 2022

@author: jdh38
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)
plt.figure(figsize=(10, 5))
plt.imshow(img, cmap = 'gray')

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.figure(figsize=(10, 3))
plt.plot(hist)

equ = cv2.equalizeHist(img)
plt.figure(figsize=(7, 20))
plt.subplot(1, 2, 1); plt.imshow(img, cmap = 'gray')
plt.subplot(1, 2, 2); plt.imshow(equ, cmap = 'gray')

plt.figure(figsize=(10, 3))
plt.hist(equ.ravel(), 256, [0, 256])
plt.show()

imin = img.min()
imax = img.max()
res = (img - imin) * (255 / (imax - imin))
res = res.astype('uint8')

plt.figure(figsize=(7, 20))
plt.subplot(121); plt.imshow(img, vmin=0, vmax=255, cmap='gray')
plt.subplot(122); plt.imshow(res, cmap='gray')
plt.show()

plt.figure(figsize=(10, 3))
plt.hist(res.ravel(), 256, [0, 256])
plt.show()


# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 00:13:25 2022

@author: jdh38
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lenna.png')

#scaled_img = cv2.resize(img, None, fx = 0.4, fy = 0.6)

#plt.subplot(121); plt.imshow(img[:,:,::-1])
#plt.subplot(122); plt.imshow(scaled_img[...,::-1])

rows, cols, ch = img.shape
#matrix = np.float32([[0.4, 0, 0], [0, 0.6, 0]])
#matrix = np.float32([[1, 0, -100], [0, 1, -30]])

#matrix = cv2.getRotationMatrix2D((cols/2, rows/2), 30, 1)

'''
pt1 = np.float32([[40, 40], [250, 40], [100, 200]])
pt2 = np.float32([[40, 80], [220, 30], [150, 200]])
matrix = cv2.getAffineTransform(pt1, pt2)
scaled_img = cv2.warpAffine(img, matrix, (cols, rows))

cv2.circle(img, (40, 40), 5, (255, 0, 0), -1)
cv2.circle(img, (250, 40), 5, (0, 0, 255), -1)
cv2.circle(img, (100, 200), 5, (0, 255, 0), -1)

cv2.circle(scaled_img, (40, 80), 5, (255, 0, 0), -1)
cv2.circle(scaled_img, (220, 30), 5, (0, 0, 255), -1)
cv2.circle(scaled_img, (150, 200), 5, (0, 255, 0), -1)
'''

'''
matrix = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 0.5)
scaled_img = cv2.warpAffine(img, matrix, (cols, rows))
'''

matrix = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
abs_cos = abs(matrix[0,0])
abs_sin = abs(matrix[0,1])
w = int(rows * abs_sin + cols * abs_cos)
h = int(rows * abs_cos + cols * abs_sin)
matrix[0,2] += w/2 - cols/2
matrix[1,2] += h/2 - rows/2
scaled_img = cv2.warpAffine(img, matrix, (w,h))

plt.subplot(121); plt.imshow(img[...,::-1])
plt.subplot(122); plt.imshow(scaled_img[...,::-1])
plt.show()
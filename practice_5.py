# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 00:54:53 2022

@author: jdh38
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
img = cv2.imread('morp.PNG', cv2.IMREAD_GRAYSCALE)

kernel = np.ones((3, 3), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
contour = dilation - erosion

plt.figure(figsize=(10,8))
plt.subplot(231); plt.imshow(img, cmap = 'gray')
plt.subplot(232); plt.imshow(erosion, cmap = 'gray')
plt.subplot(233); plt.imshow(dilation, cmap = 'gray')
plt.subplot(234); plt.imshow(opening, cmap = 'gray')
plt.subplot(235); plt.imshow(closing, cmap = 'gray')
plt.subplot(236); plt.imshow(contour, cmap = 'gray')

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.subplot(121); plt.imshow(img, cmap = 'gray')
plt.subplot(122); plt.imshow(gradient, cmap='gray')

s_vs_p = 0.5
amount = 0.01
img_sp = np.copy(img)

num_salt = np.ceil(amount * img.size * s_vs_p)
coords = [np.random.randint(0, i-1, int(num_salt)) for i in img.shape]
img_sp[tuple(coords)] = 1

num_pepper = np.ceil(amount * img.size * (1. - s_vs_p))
coords = [np.random.randint(0, i-1, int(num_pepper)) for i in img.shape]
img_sp[tuple(coords)] = 0

plt.subplot(111); plt.imshow(img_sp, cmap='gray')

opening2 = cv2.morphologyEx(img_sp, cv2.MORPH_OPEN, kernel)
closing2 = cv2.morphologyEx(opening2, cv2.MORPH_CLOSE, kernel)
plt.subplot(121); plt.imshow(opening2, cmap='gray')
plt.subplot(122); plt.imshow(closing2, cmap='gray')

'''

img = cv2.imread('morp2.PNG', cv2.IMREAD_GRAYSCALE)

img_inv = cv2.bitwise_not(img)
_, bw = cv2.threshold(img_inv, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
'''
plt.figure(figsize=(10,3))
plt.imshow(img, cmap = 'gray')
plt.figure(figsize=(10,3))
plt.imshow(bw, cmap = 'gray')
'''

horizontal = np.copy(bw)
cols = horizontal.shape[1]
horizontal_size = cols // 20

horizontalStruc = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_size, 1))
horizontal = cv2.erode(horizontal, horizontalStruc)
horizontal = cv2.dilate(horizontal, horizontalStruc)

'''
plt.figure(figsize=(10, 3))
plt.imshow(horizontal, cmap = 'gray')
'''

vertical = np.copy(bw)
rows = vertical.shape[0]
vertical_size = rows // 25
verticalStruc = cv2.getStructuringElement(cv2.MORPH_RECT, (1, vertical_size))
vertical = cv2.erode(vertical, verticalStruc)
vertical = cv2.dilate(vertical, verticalStruc)
'''
plt.figure(figsize=(10, 3))
plt.imshow(vertical, cmap = 'gray')
'''
vertical_inv = cv2.bitwise_not(vertical)
'''
plt.figure(figsize=(10, 3))
plt.imshow(vertical_inv, cmap = 'gray')
'''
kernel = np.ones((3, 3), np.uint8)
edges = cv2.morphologyEx(vertical, cv2.MORPH_GRADIENT, kernel)
'''
plt.figure(figsize=(10, 3))
plt.imshow(edges, cmap = 'gray')
'''
smooth = cv2.blur(vertical_inv, (7, 7))
'''
plt.figure(figsize=(10, 3))
plt.imshow(smooth, cmap = 'gray')
'''
(rows, cols) = np.where(edges != 0)
vertical_inv[rows, cols] = smooth[rows, cols]
plt.figure(figsize=(10, 3))
plt.imshow(vertical_inv, cmap = 'gray')



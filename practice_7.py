# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 01:48:46 2022

@author: jdh38
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def sketchify(img, ksize=5) :
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.medianBlur(img_gray, 7)
    
    edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize = ksize)
    ret, sketch = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
    
    sketch_bgr = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)
    
    plt.figure(figsize=(10, 3))
    plt.subplot(141); plt.imshow(img[...,::-1])
    plt.subplot(142); plt.imshow(img_gray, cmap = 'gray')
    plt.subplot(143); plt.imshow(edges, cmap = 'gray')
    plt.subplot(144); plt.imshow(sketch_bgr[...,::-1])
    
    return sketch_bgr
 
def cartoonize(img) :
    num_iter = 5
    ds_factor = 4
    sigma_color = 10
    sigma_space = 8
    
    img_small = cv2.resize(img, None, fx = 1.0/ds_factor, fy = 1.0/ds_factor)
    for i in range(num_iter) :
        img_small = cv2.bilateralFilter(img_small, 0, sigma_color, sigma_space)
        
    img_bilateral = cv2.resize(img_small, None, fx = ds_factor, fy = ds_factor)
    
    img_gaussian = cv2.GaussianBlur(img, (0,0), sigmaX=5)
    
    sketch_bgr = sketchify(img)
    sketch_01 = sketch_bgr / 255
    
    cartoon = img_bilateral * sketch_01
    cartoon = cartoon.astype('uint8')
    
    plt.figure(figsize=(15,10))
    plt.subplot(141); plt.imshow(img[...,::-1])
    plt.subplot(142); plt.imshow(img_bilateral[...,::-1])
    plt.subplot(143); plt.imshow(img_gaussian[...,::-1])
    plt.subplot(144); plt.imshow(cartoon[...,::-1])
    
    return cartoon


if __name__ == '__main__' :
    img = cv2.imread('Lenna.png')
    cartoon = cartoonize(img)
    
    
    
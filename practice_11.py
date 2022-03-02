# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 16:24:50 2022

@author: jdh38
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
import dlib

lmd = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
fd = dlib.get_frontal_face_detector()

img = cv2.imread('tv_2person.jpg')

sun_glass = cv2.imread('sunglasses.png')

sun_b = sun_glass[:,:,0]
sun_b[sun_b == 0] = 200
sun_r = sun_glass[:,:,1]
sun_r[sun_r == 0] = 200

sun_x = sun_glass.shape[1]
sun_y = sun_glass.shape[0]

img = cv2.resize(img, (sun_x, sun_y))

s_gray = cv2.cvtColor(sun_glass, cv2.COLOR_BGR2GRAY)
_, s_mask = cv2.threshold(s_gray, 180, 255, cv2.THRESH_BINARY_INV)

s_mask = s_mask[:,:,np.newaxis]
s_masked = sun_glass * s_mask

s_masked.astype(np.uint8)

left_x = int(sun_x * 0.25)
right_x = int(sun_x - left_x)

y = int(sun_y * 0.45)

eye_p_sun = [(left_x, y), (right_x, y)]

frects = fd(img, 0)

for i in range(0, len(frects)) :
    lm = lmd(img, frects[i])
    left_p = (lm.part(36).x, lm.part(36).y)
    right_p = (lm.part(45).x, lm.part(45).y)
    
    eye_p_img = [left_p, right_p]
    
    t_mat = cv2.estimateAffinePartial2D(np.array(eye_p_sun), np.array(eye_p_img))[0]
    
    s_masked_trans = cv2.warpAffine(s_masked, t_mat, (sun_x, sun_y))
    
    img[s_masked_trans > 0] = img[s_masked_trans > 0] * 0.7 \
                                + s_masked_trans[s_masked_trans > 0] * 0.3
    
img.astype(np.uint8)
    
plt.imshow(img[:,:,::-1])


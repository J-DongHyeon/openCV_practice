# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 20:32:57 2022

@author: jdh38
"""

import numpy as np
import cv2
import math


center = []; circumference = []
source = cv2.imread('Lenna.png')

def drawCircle(event, x, y, flags, userdata) :
    global center, circumference
    
    if event == cv2.EVENT_LBUTTONDOWN :
        center = [(x, y)]
        cv2.circle(source, center[0], 1, (0, 0, 255), 2)
        
    elif event == cv2.EVENT_LBUTTONUP :
        circumference = [(x, y)]
        dx = center[0][0] - circumference[0][0]        
        dy = center[0][1] - circumference[0][1]
        radius = math.sqrt(pow(dx,2) + pow(dy,2))
        cv2.circle(source, center[0], int(radius), (0, 255, 0), 2)
        
cv2.namedWindow("Window")
cv2.setMouseCallback("Window", drawCircle)

key = 0
while key != 27 :
    cv2.imshow("Window", source)
    cv2.putText(source, 'Choose center, and drag. ESC to exit',
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    key = cv2.waitKey(20)

cv2.destroyAllWindows()
        
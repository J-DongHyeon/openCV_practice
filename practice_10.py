# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 20:51:54 2022

@author: jdh38
"""

import numpy as np
import cv2

freezeFlag = False
font = cv2.FONT_HERSHEY_SIMPLEX

def onMouseEvent(event, x, y, flags, userdata) :
    global freezeFlag
    
    if event == cv2.EVENT_LBUTTONDOWN :
        freezeFlag = False
    elif event == cv2.EVENT_RBUTTONDOWN :
        freezeFlag = True

cv2.namedWindow('videoWindow')
cv2.setMouseCallback('videoWindow', onMouseEvent)
cap = cv2.VideoCapture('aespa_opencv.mp4')

while(cap.isOpened()) :
    if not freezeFlag :
        ret, frame = cap.read()
        frameCopy = frame.copy()
        cv2.putText(frame, 'Playing', (10, 50), font, 1, (0, 0, 255), 3)
        cv2.imshow('videoWindow', frame)
    
    else : 
        cv2.putText(frameCopy, 'Stopped', (10, 50), font, 1, (0,255,0), 3)
        cv2.imshow('videoWindow', frameCopy)
        
    key = cv2.waitKey(10)
    print('freezeFlag ', freezeFlag)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
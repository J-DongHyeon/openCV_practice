# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:01:53 2022

@author: jdh38
"""

import numpy as np

a = np.arange(20).reshape(4, 5)
print(a)


a[a%2 != 0] += 100

print(a)

a[0], a[2] = a[2], a[0].copy()

print(a)

maxVal = a.max()
maxIdx = a.argmax()

print(maxVal, maxIdx)
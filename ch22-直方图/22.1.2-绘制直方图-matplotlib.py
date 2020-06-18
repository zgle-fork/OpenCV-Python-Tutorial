# -*- coding: utf-8 -*-
__author__ = 'play4fun'
"""
create time:15-10-24 下午5:17
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/home.jpg', 0)
# img.ravel() # np n-d array to 1-d: flatten(): returns a copy; ravel(): returns the modified array 

print('img.shape',img.shape)
ravel=img.ravel()

print('ravel.shape',ravel.shape)
plt.hist(ravel, 256, [0, 256])
plt.show()

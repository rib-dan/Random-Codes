# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:35:54 2022

@author: dan_r
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image


#class display_squares():
    
#    def __init__(self, n_squares)


x_lim = 1004
y_lim = 1004


fig, ax = plt.subplots()
ax.set_facecolor((1.0, 0.47, 0.42))
ax.set(xlim=(0, x_lim), ylim=(0, y_lim))
rect = []
for i in range(0,10):
    rect=Rectangle((2+50*i, 2), 50, 50, linewidth=1, edgecolor='r', facecolor='r')
    ax.add_patch(rect)
ax.set_axis_off()
plt.show()
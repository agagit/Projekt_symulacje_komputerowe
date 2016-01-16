# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 19:35:03 2016

@author: aga
"""

from skimage import data, io, filters

image = imread('godhier.jpg')
edges = filters.sobel(image)
io.imshow(edges)
io.show()


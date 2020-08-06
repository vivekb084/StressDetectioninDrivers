#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 12:21:50 2019

@author: Vivek Bindal
"""

import numpy as np
from peaks_func import peaks

def maxmin(arr):
    size = np.shape(arr)
    row = int(size[0])
    maxarr = []
    minarr = []
    for i in range(1, row - 1):
        if (arr[i - 1][0] < arr[i][0] and arr[i + 1][0] <= arr[i][0]):
            if (arr[i + 1][0] == arr[i][0]):
                j = i + 1
                while (j + 1 < row - 2 and arr[j + 1][0] == arr[i][0]):
                    j = j + 1
                if (j + 1 < row - 2 and arr[j + 1][0] < arr[i][0]):
                    maxarr.append(i)
            else:
                maxarr.append(i)
        if (arr[i - 1][0] >= arr[i][0] and arr[i + 1][0] > arr[i][0]):
            if (arr[i - 1][0] == arr[i][0]):
                j = i - 1
                while (arr[j - 1][0] == arr[i][0] and j - 1 > 0):
                    j = j - 1
                if (arr[j - 1][0] > arr[i][0]):
                    minarr.append(i)
            else:
                minarr.append(i)
    size = np.shape(minarr)
    sizemin = int(size[0])
    size = np.shape(maxarr)
    sizemax = int(size[0])
    farr = []
    if (minarr[0] < maxarr[0] and sizemin > sizemax):
        for i in range(0, sizemin - 1):
            farr.append(minarr[i])
            farr.append(maxarr[i])
    elif (minarr[0] < maxarr[0] and sizemin == sizemax):
        for i in range(0, sizemin):
            farr.append(minarr[i])
            farr.append(maxarr[i])
    elif (minarr[0] > maxarr[0] and sizemin == sizemax):
        for i in range(0, sizemax - 1):
            farr.append(minarr[i])
            farr.append(maxarr[i + 1])
    elif (minarr[0] > maxarr[0] and sizemin < sizemax):
        for i in range(0, sizemax - 1):
            farr.append(minarr[i])
            farr.append(maxarr[i + 1])
    return farr


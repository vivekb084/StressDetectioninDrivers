#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 20:44:34 2019

@author: Vivek Bindal
"""

import numpy as np


def normalise(arr):
    mean = 0;
    size = np.shape(arr)
    for i in range(0, size[0]):
        mean += arr[i]
    mean = mean / size[0]

    sqerror = 0
    for i in range(0, size[0]):
        sqerror += np.square((arr[i] - mean))
    dev = sqerror / size[0]
    dev = np.sqrt(dev)
    # print(dev)

    narr = np.zeros(shape=(size[0], 1))
    for i in range(0, size[0]):
        narr[i] = (arr[i] - mean) / dev
    return narr
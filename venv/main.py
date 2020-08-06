#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 13:44:34 2020

@author: Vivek Bindal
"""

import numpy as np
from features_func import features

with open('./newfoot.txt') as file:
    footm = [[float(digit) for digit in line.split()] for line in file]

foot=np.array(footm)

size=np.shape(foot)

row=int(size[0])
col=int(size[1])

feat_mat=np.zeros(shape=(row,16))

for i in range(0,row):
    feat1=np.zeros(shape=(row,8))
    feat1=features(foot[i])
    feat_mat[i,:8]=feat1[:]

with open('./newhand.txt') as file:
    handm = [[float(digit) for digit in line.split()] for line in file]

hand = np.array(handm)

size = np.shape(hand)
row = int(size[0])
col = int(size[1])

for i in range(0, row):
    feat1 = np.zeros(shape=(row, 8))
    feat1 = features(hand[i])
    feat_mat[i, 8:16] = feat1[:]

with open('feat_mat_peaks111.txt','wb') as file1:
    np.savetxt(file1,feat_mat, delimiter=',', fmt='%.5f')
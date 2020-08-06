#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 18:33:43 2019

@author: Vivek Bindal
"""

import numpy as np

mat = np.zeros(shape=(48, 4651))
n = 1;
for i in range(1, 10):
    with open("./arranged_dataset/drive0" + i + "/drive0"+i+"m.mat") as file:
        valm = [[float(digit) for digit in line.split()] for line in file]

    val = np.array(valm)
    if (i != 2 and i != 3 and i != 4 and i != 1):
        col = 6;
        mat[n, 0:4650] = val[col, 7440:12090]
        n = n + 1;
        if (i == 1):
            mat[n, 0:4650] = val[col, 16740:21390];
            n = n + 1;
            mat[n, 0:4650] = val[col, 27900:32550];
            n = n + 1;
        elif (i == 2 or i == 4 or i == 6 or i == 5 or i == 8 or i == 9):
            mat[n, 0:4650] = val[col, 18600:23250];
            n = n + 1;
            if (i == 9):
                mat[n, 0:4650] = val[col, 32550:37200];
                n = n + 1;
            else:
                mat[n, 0:4650] = val[col, 37200:41850];
                n = n + 1;
        elif (i == 3 or i == 7):
            mat[n, 0:4650] = val[col, 23250:27900];
            n = n + 1;
            mat[n, 0:4650] = val[col, 41850:46500];
            n = n + 1;
    elif (i == 2):
        col = 4;
        mat[n, 0:4650] = val[col, 7440:12090];
        n = n + 1;
        if (i == 1):
            mat[n, 0:4650] = val[col, 16740:21390];
            n = n + 1;
            mat[n, 0:4650] = val[col, 27900:32550];
            n = n + 1;
        elif (i == 2 or i == 4 or i == 6 or i == 5 or i == 8 or i == 9):
            mat[n, 0:4650] = val[col, 18600:23250];
            n = n + 1;
            if (i == 9):
                mat[n, 0:4650] = val[col, 32550:37200];
                n = n + 1;
            else:
                mat[n, 0:4650] = val[col, 37200:41850];
                n = n + 1;
        elif (i == 3 or i == 7):
            mat[n, 0:4650] = val[col, 23250:27900];
            n = n + 1;
            mat[n, 0:4650] = val[col, 41850:46500];
            n = n + 1;
    elif (i == 4 or i == 1):
        col = 5;
        mat[n, 0:4650] = val[col, 7440:12090];
        n = n + 1;
        if (i == 1):
            mat[n, 0:4650] = val[col, 16740:21390];
            n = n + 1;
            mat[n, 0:4650] = val[col, 27900:32550];
            n = n + 1;
        elif (i == 2 or i == 4 or i == 6 or i == 5 or i == 8 or i == 9):
            mat[n, 0:4650] = val[col, 18600:23250];
            n = n + 1;
            if (i == 9):
                mat[n, 0:4650] = val[col, 32550:37200];
                n = n + 1;
            else:
                mat[n, 0:4650] = val[col, 37200:41850];
                n = n + 1;
        elif (i == 3 or i == 7):
            mat[n, 0:4650] = val[col, 23250:27900];
            n = n + 1;
            mat[n, 0:4650] = val[col, 41850:46500];
            n = n + 1;
    elif (i == 3):
        col = 3;
        mat[n, 0:4650] = val[col, 7440:12090];
        n = n + 1;
        if (i == 1):
            mat[n, 0:4650] = val[col, 16740:21390];
            n = n + 1;
            mat[n, 0:4650] = val[col, 27900:32550];
            n = n + 1;
        elif (i == 2 or i == 4 or i == 6 or i == 5 or i == 8 or i == 9):
            mat[n, 0:4650] = val[col, 18600:23250];
            n = n + 1;
            if (i == 9):
                mat[n, 0:4650] = val[col, 32550:37200];
                n = n + 1;
            else:
                mat[n, 0:4650] = val[col, 37200:41850];
                n = n + 1;
        elif (i == 3 or i == 7):
            mat[n, 0:4650] = val[col, 23250:27900];
            n = n + 1;
            mat[n, 0:4650] = val[col, 41850:46500];
            n = n + 1;

for i in range(10, 17):
    with open("./arranged_dataset/drive0" + i + "m.mat") as file:
        valm = [[float(digit) for digit in line.split()] for line in file]

    val = np.array(valm)
    if (i != 13 and i != 14):
        col = 6;
        mat[n, 0:4650] = val[col, 7440:12090];
        n = n + 1;
        if (i == 15 or i == 16):
            mat[n, 0:4650] = val[col, 16740:21390];
            n = n + 1;
            mat[n, 0:4650] = val[col, 27900:32550];
            n = n + 1;
        elif (i >= 10 and i <= 14):
            mat[n, 0:4650] = val[col, 18600:23250];
            n = n + 1;
            if (i == 9):
                mat[n, 0:4650] = val[col, 32550:37200];
                n = n + 1;
            else:
                mat[n, 0:4650] = val[col, 37200:41850];
                n = n + 1;
    elif (i == 13 or i == 14):
        col = 5;
        mat[n, 0:4650] = val[col, 7440:12090];
        n = n + 1;
        if (i == 15 or i == 16):
            mat[n, 0:4650] = val[col, 16740:21390];
            n = n + 1;
            mat[n, 0:4650] = val[col, 27900:32550];
            n = n + 1;
        elif (i >= 10 and i <= 14):
            mat[n, 0:4650] = val[col, 18600:23250];
            n = n + 1;
            if (i == 9):
                mat[n, 0:4650] = val[col, 32550:37200];
                n = n + 1;
            else:
                mat[n, 0:4650] = val[col, 37200:41850];
                n = n + 1;
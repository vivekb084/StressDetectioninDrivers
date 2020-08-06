#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 21:08:02 2019

@author: Vivek Bindal
"""

import numpy as np
from normalise_func import normalise
from maxmin import maxmin
from scipy import signal
from scipy.stats import mode

def features(arr):
    feat=np.zeros(shape=(1,8))
    f, Pxx_den=signal.periodogram(arr)
    variance = (np.var(arr))/2600000
    arr=normalise(arr)
    mean =  np.mean(arr[0])
    totalPower=np.sum(Pxx_den)
    mymode,FrequencySpikes=mode(arr)
    standardDeviationPSD=np.std(Pxx_den)
    arr=arr.reshape((-1,1))
    farr=maxmin(arr)
    size=np.shape(farr)
    num=size[0]/2
    feat[0][0]=num
    sum_min=0
    sumd=0
    for j in range(0,int(size[0]/2)):
        sum_min+=arr[farr[j*2]]
        sumd+=farr[j*2+1]-farr[j*2]
    feat[0][0]=mean
    feat[0][1]=variance
    feat[0][2]=FrequencySpikes[0][0]
    feat[0][3]=sum_min
    feat[0][4]=sumd
    feat[0][5]=sumd*sum_min/2
    feat[0][6]=standardDeviationPSD
    feat[0][7]=totalPower

    return feat
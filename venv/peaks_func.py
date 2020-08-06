#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 11:06:15 2017

@author: riyamaan
"""
import numpy as np
import math 


def peaks(farr,iarr):
    size=np.shape(iarr)
    peaksarr=[]
    parr=[]
    maxs=90
    val=85
    
    for i in range(0,size[0]-1,2):
        slope=(farr[iarr[i+1]]-farr[iarr[i]])/(iarr[i+1]-iarr[i])
        slope=math.degrees(math.atan(slope))
        if(slope<val):
            parr.append(iarr[i])
            parr.append(iarr[i+1])
            
    i=0
    maxs=(farr[parr[i+1]]-farr[parr[i]])/(parr[i+1]-parr[i])
    maxs=math.degrees(math.atan(maxs))
    size=np.shape(parr)
    
    for i in range(2,size[0]-1,2):
        slope=(farr[parr[i+1]]-farr[parr[i]])/(parr[i+1]-parr[i])
        slope=math.degrees(math.atan(slope))
        if(slope>maxs):
            maxs=slope
            
    
    maxs=0.75*maxs
    
    for i in range(0,size[0]-1,2):
        slope=(farr[parr[i+1]]-farr[parr[i]])/(parr[i+1]-parr[i])
        slope=math.degrees(math.atan(slope))
        if(slope>maxs):
            peaksarr.append(parr[i])
            peaksarr.append(parr[i+1])
            
    return peaksarr
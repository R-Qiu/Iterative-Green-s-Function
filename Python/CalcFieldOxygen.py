# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 23:30:22 2018

@author: Richard
"""

def CalcOxygenOut(HistogramArray):
    OxygenOut = 0
    for i in xrange(HistogramArray.shape[0]):
        OxygenOut += HistogramArray[i,0]*HistogramArray[i,1]
        
    return OxygenOut
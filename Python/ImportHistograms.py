# -*- coding: utf-8 -*-
"""
Created on Wed Jan 03 09:14:23 2018

@author: Richard
"""

import numpy as np

def ImportHist(HistogramFileName):
    HistOut = np.empty([0,3])
    i = j = 0
    with open(HistogramFileName, "r") as Hist:
        for line in Hist:
            if i > 1 and line[0].isdigit() == False:
                j = 1
            if i > 1 and j == 0: 
                HistOut = np.vstack((HistOut,line.split()))
            i += 1
                
    return HistOut
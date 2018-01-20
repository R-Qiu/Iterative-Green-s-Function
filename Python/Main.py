# -*- coding: utf-8 -*-
"""
Created on Wed Jan 03 09:14:11 2018

@author: Richard
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from ImportHistograms import ImportHist
from CalcOxygenOut import CalcOxygenOut
from ChangeSoluteParams import ChangeSoluteParams

HistogramFileName = "D:/12th/Biotech/Model/Green's Function (VS 2010)/Green's Function (VS 2010)/Histogram.out"
#SoluteParamsFileName = "D:/12th/Biotech/Model/Green's Function (VS 2010)/Green's Function (VS 2010)/SoluteParams.dat"
SoluteParamsFileName = "D:/12th/Biotech/Model/Green's Function (VS 2010)/SoluteParams.dat"

HistOut = ImportHist(HistogramFileName)
HistOut = HistOut.astype(float)[:,:2]
HistBins = np.linspace(0,HistOut.shape[0]+1, num = HistOut.shape[0]+1)

plt.figure("1.5aMesent")
plt.hist(HistOut[:,0], HistBins, weights=HistOut[:,1])

OxygenOut = CalcOxygenOut(HistOut)

ChangeSoluteParams(SoluteParamsFileName, OxygenOut)



# -*- coding: utf-8 -*-
"""
Created on Wed Jan 03 09:14:11 2018

@author: Richard
"""

import numpy as np
import matplotlib.pyplot as plt

from ImportHistograms import ImportHist
#from FindOxygenOut import FindOxygenOut
from ChangeSoluteParams import ChangeSoluteParams
from ReadBoundaryNodes import ReadBoundaryNodes, FindOxygenIn, FindOxygenOut

HistogramFileName = "D:/12th/Biotech/Model/Green's Function (VS 2010)/Green's Function (VS 2010)/Histogram.out"
SoluteParamsFileName = "D:/12th/Biotech/Model/Green's Function (VS 2010)/Green's Function (VS 2010)/SoluteParams.dat"
IVRFileName= "D:/12th/Biotech/Model/Green's Function (VS 2010)/Green's Function (VS 2010)/IntravascRes.dat"
NetworkFileName = "D:/12th/Biotech/Model/Green's Function (VS 2010)/Green's Function (VS 2010)/Network.dat"
TissueLevelsFileName = "D:/12th/Biotech/Model/Green's Function (VS 2010)/Green's Function (VS 2010)/TissueLevels.out"
TissueSourcesFileName = "D:/12th/Biotech/Model/Green's Function (VS 2010)/Green's Function (VS 2010)/TissueSources.out"
GreensResFileName = "D:/12th/Biotech/Model/Green's Function (VS 2010)/Green's Function (VS 2010)/GreensRes.out"
VesselLevelsFileName = "D:/12th/Biotech/Model/Green's Function (VS 2010)/Green's Function (VS 2010)/VesselLevels.out"


#HistogramFileName = "D:/12th/Biotech/Model/Green's Function (VS 2010)/Histogram.out"
#SoluteParamsFileName = "D:/12th/Biotech/Model/Green's Function (VS 2010)/SoluteParams.dat"
#IVRFileName= "D:/12th/Biotech/Model/Green's Function (VS 2010)/IntravascRes.dat"
#NetworkFileName = "D:/12th/Biotech/Model/Green's Function (VS 2010)/Network.dat"
#TissueLevelsFileName = "D:/12th/Biotech/Model/Green's Function (VS 2010)/TissueLevels.out"
#TissueSourcesFileName = "D:/12th/Biotech/Model/Green's Function (VS 2010)/TissueSources.out"
#GreensResFileName = "D:/12th/Biotech/Model/Green's Function (VS 2010)/GreensRes.out"
#VesselLevelsFileName = "D:/12th/Biotech/Model/Green's Function (VS 2010)/VesselLevels.out"

#HistOut = ImportHist(HistogramFileName)
#HistOut = HistOut.astype(float)[:,:2]
#HistBins = np.linspace(0,HistOut.shape[0]+1, num = HistOut.shape[0]+1)

BoundaryNodes = ReadBoundaryNodes(NetworkFileName, VesselLevelsFileName)
InNodes = FindOxygenIn(BoundaryNodes)
OutNodes = FindOxygenOut(BoundaryNodes)

print BoundaryNodes
print InNodes
print OutNodes
#ChangeSoluteParams(SoluteParamsFileName, OxygenOut)



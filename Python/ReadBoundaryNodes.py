# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 23:56:14 2018

@author: Richard
"""
import numpy as np

def ReadBoundaryNodes(NetworkFileName, VesselLevelsFileName):
    with open(NetworkFileName) as Network:
        with open(VesselLevelsFileName) as VesselLevels:
            read = False
            BoundaryNodes = np.empty([0,7])
            for line in Network: 
                if read == True and (line[0].isdigit() == True or line[3].isdigit() == True):
                        BoundaryNodes = np.vstack((BoundaryNodes,line.split()))
                if "bctyp" in line:
                    read = True
    BoundaryNodes = BoundaryNodes.astype(np.float)
    return BoundaryNodes

def FindOxygenIn(BoundaryNodes):
    InNodes = np.empty([0,2])
    for row in BoundaryNodes:
        if row[1] == 0:
            InNodes = np.vstack((InNodes,[row[0], row[4]]))
    return InNodes

def FindOxygenOut(BoundaryNodes, ):
    OutNodes = np.empty([0,1])
    for row in BoundaryNodes:
        if row[1] == 2:
            OutNodes = np.vstack((OutNodes,[row[0]]))
    OutNodes = OutNodes.astype(np.int)
    return OutNodes

    
    
    
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 03 09:00:08 2018

@author: Richard
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#FileName = "D:/12th/Biotech/Model/Green's Function (VS 2010)/Green's Function (VS 2010)/Histogram.out"
#FileName = "D:/12th/Biotech/Model/Green's Function (VS 2010)/Green's Function (VS 2010)/SoluteParams.dat"
FileName = "D:/12th/Biotech/Model/Green's Function (VS 2010)/SoluteParams.dat"
#FileName = "D:/12th/Biotech/Model/Green's Function (VS 2010)/verp.txt"



#with open(FileName, "w") as Derp:
#    Derp.write("Seeya, world!") 
#
#with open(FileName, "r") as Herp:
#    FileContents = Herp.read()
#
#with open(FileName, "w") as HerpDerp:
#    HerpDerp.write(FileContents.replace("Seeya", "Buhbbbye b"))
#
#with open(FileName, "r") as Terp:
#    for line in Terp:
#        print line[5]
#        StringEnd = line.find("b", 6)
#        print StringEnd


with open(FileName, "r") as SoluteRead:
        SoluteParamsContents = SoluteRead.read()
        print SoluteParamsContents   

for line in SoluteParamsContents:
    if "Total inflow" in line:
        StringStart = 2
        StringEnd = line.find("	", 3)
        print line[StringStart:StringEnd]


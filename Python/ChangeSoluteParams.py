# -*- coding: utf-8 -*-
"""
Created on Sat Jan 06 17:21:01 2018

@author: Richard
"""

def ChangeSoluteParams(SoluteParamsFileName, OxygenChange):
    with open(SoluteParamsFileName, "r") as SoluteRead:
        for line in SoluteRead:
            if "Total inflow" in line:
                StringStart = 2
                StringEnd = line.find("	", 3)
                print line[StringStart:StringEnd]
        SoluteRead.seek(0)
        SoluteParamsContents = SoluteRead.read() 

#    with open(SoluteParamsFileName, "w") as SoluteWrite:
        
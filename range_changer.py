# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 15:31:50 2018
This code converts a value of one range to another range.
@author: Sourav
"""
oldMin,oldMax,newMin,newMax=10.0,-10.0,0,180
oldRange=(oldMax-oldMin)
newRange=(newMax-newMin)
def range_change(oldVal):
#    oldVal=float(input('Enter the old value:'))
    newVal=int((oldVal-oldMin)*newRange/oldRange+newMin)
    return(newVal)
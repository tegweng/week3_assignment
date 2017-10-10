# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:34:53 2017

@author: fj803263
"""

#Question one of Numerical Differentiation assignment

from __future__ import division
import numpy as np

def genarray(y0,yN,N):
    #function to generate an array of y's
    n=int(N)
    dy=( float(yN) - float(y0) ) / float(n + 1)
    yarray=np.zeros(n)
    for i in xrange(n):
        yarray[i] = y0 + i * dy
    return yarray

print genarray(0,1e6,10)

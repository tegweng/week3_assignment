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
    #here ymin is y0 and ymax is yN
    n=int(N)
    dy=( float(yN) - float(y0) ) / float(n)
    yarray=np.zeros(n+1)
    for i in xrange(n+1):
        yarray[i] = y0 + i * dy
    return yarray

#seeing if genarray works:
print genarray(0,10,10)

def pres(y):
    #function to calculate the pressure
    pa=1e5
    pb=200
    L=2.4 * 1e6
    p= pa + pb * np.cos( y * np.pi / L)
    return p
    
def gradpres(y0,yN,N):
    #using difference formulas to calcute dp/dy
    n=int(N)
    p=pres(genarray(y0,yN,N))
    dp= np.zeros(n+1)
    dy = ( float(yN) - float(y0) ) / float(n)
    dp[0] = ( p[1] - p[0] ) / dy
    dp[n] = ( p[n] - p[n-1] ) / dy
    for i in xrange(1,n):
        dp[i] = ( p[i + 1] - p[i - 1] ) / ( 2 * dy )
    return dp

def anagradpres(y0, yN, N):
    #using analytical solution to calculate dp/dy
    pb = 200
    L = 2.4 * 1e6
    y = genarray(y0,yN, N)
    dp = - pb * np.pi * np.sin( y * np.pi / L) / L
    return dp

def speed(dp):
    #fuction for calulating u
    u = - 1e4 * dp
    return u

#printing speed calculated numerically
print speed(gradpres(0,1e6,10))
#printing speed calculated analytically
print speed(anagradpres(0,1e6,10))




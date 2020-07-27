#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:53:04 2020

@author: shaloo
"""
import numpy as np
import sys
import time

L1 = float(input("Enter the length of 1st link: "))
L2 = float(input("Enter the length of the 2nd link: "))

x1 = float(input("x complement of initial position: "))
y1 = float(input("y complement of initial position: "))

x2 = float(input("x complement of final position: "))
y2 = float(input("y complement of final position: "))

if ((x1**2+y1**2)**0.5) > (L1+L2) or ((x2**2+y2**2)**0.5) > (L1+L2) or L1<L2:
    sys.exit("invalid entry")
    
p = np.pi
L= ((x1-x2)**2 + (y1-y2)**2)**0.5
z=0.1

x = np.array([x1])
y = np.array([y1])

while z<L:

    x3 = ((L-z)*x1 + z*x2)/L
    y3 = ((L-z)*y1 + z*y2)/L
    x = np.append(x, x3)
    y = np.append(y, y3)
    z = z+0.1
    
if z!=L:
    x = np.append(x,x2)
    y = np.append(y,y2)

for i,j in zip(x,y):
    c = np.arctan2(i,j)
    k = i**2+j**2

    b1 = (L1**2+L2**2-(k))/(2*L1*L2)
    a1 = (k+L1**2-L2**2)/(2*L1*(k**0.5))

    b = np.arccos(b1)
    a = np.arccos(a1)
    t1r = 180*(c-a)/p
    t2r = 180*(p-b)/p

    t1l = 180*(c+a)/p
    t2l = 180*(b-p)/p

    print('coordinates = ',i,j)
    print('The righty angles of the link are = ',t1r,t2r )
    print('The lefty angles of the link are = ',t1l,t2l ,'\n')
    time.sleep(0.5)
    


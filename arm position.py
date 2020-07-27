#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 16:42:49 2020

@author: shaloo
"""

import numpy as np

L1 = float(input("Enter the length of 1st link: "))
L2 = float(input("Enter the length of the 2nd link: "))

x = float(input("Enter the x component of the required position: "))
y = float(input("Enter the y component of the required position: "))

if ((x**2+y**2)**0.5) > (L1+L2):
    print("invalid entry")
    exit()

c = np.arctan2(x,y)
print(c)

b1 = (L1**2+L2**2-x**2-y**2)/(2*L1*L2)
a1 = (x**2+y**2+L1**2-L2**2)/(2*L1*((x**2+y**2)**0.5))

b = np.arccos(b1)
a = np.arccos(a1)

t1r = 180*(c-a)/np.pi
t2r = 180*(np.pi - b)/np.pi

t1l = 180*(c+a)/np.pi
t2l = 180*(b - np.pi)/np.pi

print('for the given input the righty angles of the link are = ',t1r,t2r )
print('for the given input the lefty angles of the link are = ',t1l,t2l )


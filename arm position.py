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

point1 = [0,0]
point2 = [L1*np.cos(c-a), L1*np.sin(c-a)]
point3 = [L1*np.cos(c+a), L1*np.sin(c+a)]
point4 = [x,y]
 
xval1 = [0,L1*np.sin(c-a)]
yval1 = [0,L1*np.cos(c-a)]
xval2 = [L1*np.sin(c-a),x]
yval2 = [L1*np.cos(c-a),y]
xval3 = [0,L1*np.sin(c+a)]
yval3 = [0,L1*np.cos(c+a)]
xval4 = [L1*np.sin(c+a),x]
yval4 = [L1*np.cos(c+a),y]

f,ax = plt.subplots(1)

ax.plot(xval1, yval1, 'r', label = 'link1')
ax.plot(xval2, yval2, 'b', label = 'link2')
ax.plot(xval3, yval3, 'r')
ax.plot(xval4, yval4, 'b')

plt.axis('square')
plt. title('Position of the arm in 2D space')

plt.grid()
plt.legend()
plt.show()

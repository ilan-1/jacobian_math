#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:45:35 2020

@author: shaloo
"""

from sympy import symbols, diff
from sympy.matrices import Matrix, zeros
from sympy.parsing.sympy_parser import parse_expr
#import numpy as np

x, y = symbols('x y', real=True)

f1 = x**2+x*y
f2 = x**y+2*x+y

print(f1)
print(type(f1))

v = Matrix([x,y])
#v=np.array(v)
print(type(v))
f= Matrix([f1,f2])

j_mat = zeros(2,2)
print(j_mat)

for i in range(0,2):
    for j in range(0,2):
        j_mat[i,j] = diff(f[i], v[j])
        print(j_mat[i,j])
        
print(j_mat)

j_mat_inv = j_mat.inv()
print(j_mat_inv)

        
        

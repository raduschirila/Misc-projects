# -*- coding: utf-8 -*-
"""
Created on Sat May 25 21:44:09 2019

A comparison of numerical integration methods (Trapezium, Simpson, Gaussian Quad)

@author: Radu Chirila
"""

import numpy as np;
import time
import math
from scipy.integrate import quad

def trapezoid(x,y,a,step):#where i>0
    return ((x[a+step]-x[a])*(y[a]+y[a+step])/2);#iterative implementation (for in main)

def simpson(x,y,a):
    return (((x[a+2]-x[a])/6)*(y[a]+4*y[a+1]+y[a+2]))

step=0.001;
x=np.arange(-1,1,step)
f=lambda t: math.exp(-2*t);
y=[f(x[i]) for i in range(len(x))]
actual_value=3.626860407847019;
print("Function tested: e^(-2x) -> integral [-1,1] of function")
print("Actual value of function",'%.15f'%actual_value);
print()

s=0;
start=float(time.time()*1000.0);
for i in range(len(x)-1):
    s+=trapezoid(x,y,i,1);

print("Trapezoid rule result: ",s);
print("Execution time:",'%.3f' %(float(time.time()*1000.0)-start),"ms");
print("Absolute Error: ", abs(actual_value-s));
print("Relative error: ", abs((actual_value-s))/s)
print()

s=0;
start=float(time.time()*1000.0);
for i in range(0,len(x)-2,2):
    s+=simpson(x,y,i);
 
print("Simpson's rule result", s);
print("Execution time:",'%.3f' %(float(time.time()*1000.0)-start),"ms");
print("Absolute Error: ", abs(actual_value-s));
print("Relative error: ", abs((actual_value-s))/s)
print() 

start = float(time.time()*1000.0);
s = quad(f,-1,1)

print("Gaussian Quadrature result", s[0]);
print("Execution time:",'%.3f' %(float(time.time()*1000.0)-start),"ms");
print("Absolute Error: ", abs(actual_value-s[0]));
print("Relative error: ", abs((actual_value-s[0]))/s[0])
print()
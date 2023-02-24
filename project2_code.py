# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 05:09:11 2023

@author: mishrai
"""
import random as rd
from mpl_toolkits import mplot3d


import numpy as np
import matplotlib.pyplot as plt

N = 500
pi = 22/7

dt = 1e-16
e = 1.602e-19
epsilon0=8.854e-14
mu0 = 4*pi * 10**(-17)

class electron:
    x = [0,0,0]
    v = [20,20,0]
    a = [0,0,0]
    q = -1*e
    m = 9.109e-31
    
a = electron()
b = electron()
b.x = [0,0.005,0]
a.x = [0,-0.005,0]



#particles = [a,b]
particles = [a]

B=[0,0.01,0]


xl=[]
yl=[]
zl=[]
nl=[]
vl = []



for i in range(N):
    for j in range(len(particles)):
        v = particles[j].v
        m = particles[j].m
        q = particles[j].q
        
        particles[j].a = [q/m*(v[1]*B[2] - v[2]*B[1]), q/m*(B[0]*v[2] - v[0]*B[2]), q/m*(v[0]*B[1] - B[0]*v[1])]
        
        for k in range(3):
            particles[j].v[k] = particles[j].v[k] + dt*particles[j].a[k]
            particles[j].x[k] = particles[j].x[k] + dt*particles[j].v[k]
        print(particles[j].v)
        xl.append(particles[j].x[0])
        yl.append(particles[j].x[1])
        zl.append(particles[j].x[2])
        vl.append((v[0]**2 + v[1]**2 + v[2]**3)**(1/2))
        nl.append(i)
        #print(vl[i])

fig = plt.figure()
#ax = plt.axes(projection='3d')

#ax.plot3D(xl, yl, zl, 'gray')

plt.plot(nl,vl)

print(a.x)
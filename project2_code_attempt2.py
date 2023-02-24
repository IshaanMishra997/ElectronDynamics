# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 19:06:16 2023

@author: mishrai
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the constants and initial conditions
q = -1.602e-19  # charge of electron in coulombs
m = 9.109e-31  # mass of electron in kg
B = np.array([0, 0, 1])  # magnetic field in tesla
v0 = np.array([1e6, 0, 0])  # initial velocity in m/s
r0 = np.array([0, 0, 0])  # initial position in m
t0 = 0  # initial time in seconds
tf = 1e-6  # final time in seconds
N = 1000  # number of time steps

# Define the differential equations describing the motion of the electron
def f(t, y):
    x, y, z, vx, vy, vz = y
    r = np.array([x, y, z])
    v = np.array([vx, vy, vz])
    a = q/m * np.cross(v, B)
    return [vx, vy, vz, a[0], a[1], a[2]]

# Use the Runge-Kutta method to solve the differential equations
t = np.linspace(t0, tf, N)
h = t[1] - t[0]
y = np.array([r0[0], r0[1], r0[2], v0[0], v0[1], v0[2]])

def mult(L, s):
    n = len(L)
    for i in range(n):
        L[i] = L[i]*s
    
    return L


for i in range(N-1):
    k1 = mult(f(t[i], y),h)
    k2 = mult(f(t[i] + h/2, y + mult(k1,1/2)),h)
    k3 = mult(f(t[i] + h/2, y + mult(k2,1/2)),h)
    k4 = mult(f(t[i] + h, y + k3),h)
    y = y + mult((k1 + mult(k2,2) + mult(k3,2) + k4),1/6)
    
    
    
    
# Plot the trajectory of the electron
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(y[:,0], y[:,1], y[:,2])
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_zlabel('z (m)')
plt.show()
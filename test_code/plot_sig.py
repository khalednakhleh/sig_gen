#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 23:26:00 2018

@author: Khaled Nakhleh
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

samples = 250
sine1_var = 300
sine2_var = 120
cosine1_var = 25

T = 1 / samples
x_range = 2*np.pi*T*samples

x = np.linspace(0, x_range, samples)
xf = np.linspace(0, 1/(2*T), samples/2)
y = np.sin(sine1_var*x)
z = np.cos(cosine1_var*x)
w = np.sin(sine2_var*x)

q = y + z + w
qf = fft(q)
qf_plot = (2/samples)*np.abs(qf[0:samples/2])

plt.figure(1)
plt.plot(x, y, label="sin("+str(sine1_var)+"x)")
plt.plot(x, z, label="cos("+str(cosine1_var)+"x)")
plt.plot(x, w, label="sin("+str(sine2_var)+"x)")
plt.plot(x, q, label="combined signal")
plt.title("sine and cosine functions from 0 to 2*pi")
plt.xlabel("entry values from 0 to 2*pi")
plt.ylabel("sinusoid values from -1 to 1")
plt.legend(loc="upper right")
plt.savefig("signals_graph.png")
plt.show()

plt.figure(2)
plt.plot(xf, qf_plot, label="FFT of combined signal (w)")
plt.title("Fast Fourier Transform of combined signal")
plt.xlabel("Frequency range")
plt.ylabel("Magnitude")
plt.legend(loc="upper right")
plt.savefig("FFT.png")
plt.show()



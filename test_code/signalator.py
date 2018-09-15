#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 09:49:48 2018

@author: Khaled Nakhleh
"""
import numpy as np
import matplotlib.pyplot as plt
import wave
import struct

# writes a .wave file for each generated sinusoid
def wav_it(y, amplitude, samples):
    nframes = samples
    comptype = "NONE"
    compname = "not compressed"
    nchannels = 1
    sampwidth = 2
    wav_file = wave.open("results/generated_signal.wav", "w")
    wav_file.setparams((nchannels, sampwidth,
    int(samples), nframes, comptype, compname))
    for s in y:
        wav_file.writeframes(struct.pack("h", int(s*amplitude)))

# plot with all info at once   
def plot_it(x, y):
    plt.plot(x, y,'b', label="Function")
    plt.xlabel("samples")
    plt.ylabel("Amplitude (a)")
    plt.legend(loc="upper right")
    plt.savefig("results/generated_sig.png")
    plt.show()

# generates a sine function
def sine_func(f, a, num_sam, t):
    x = np.linspace(0, num_sam, num_sam) 
    return x, (a * np.sin(2*np.pi*f*(x/t)))

# generates a cosine function
def cos_func(f, a, num_sam, t):
    x = np.linspace(0, num_sam, num_sam) 
    return x, (a * np.cos(2*np.pi*f*(x/t)))

def main():
    print("\n")
    freq = input("\tFrequency[def=8000 Hz]:  ")  or 8000             # Frequency
    amp = input("\tAmplitude[def=15]: ")         or 15               # Amplitude
    samples = input("\tNumber of samples[def=24000]: ") or 24000     # number of samples
    T = input("\tSampling rate[def=48000]: ")  or 48000              # sampling rate
    
    x, func = sine_func(freq, amp, samples, T)
    e = (input("""\n\tSignal succesfully generated.
               Do you wish to plot and save it?([y]/n): """) or 'y').lower()
    
    if (e =='yes' or e=='y'):
        wav_it(func, amp, samples)
        plot_it(x, func)
    else:
        exit

if __name__=='__main__':
    main()


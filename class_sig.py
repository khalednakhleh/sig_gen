#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 12:23:25 2018

@author: Khaled Nakhleh
"""
import numpy as np
import matplotlib.pyplot as plt
import wave
import struct

class Sig_Gen:

# Initializing the class with instances
    def __init__(self, freq, amp, samples, T, typ):
        """initializes the class by saving parameters """
        self.freq = freq
        self.amp = amp
        self.samples = samples
        self.T = T
        self.type = typ
        self.range = np.linspace(0, self.samples, self.samples)
        
# same range for all signals. necessary if no. of samples is different
    def samp_reg(lis):
        """ creates the same for all signals while preserving no. of samples"""
        max_len = 0
        for x in range(0, len(lis)):
            if (max_len > lis[x].samples):
                pass
            else:
                max_len = lis[x].samples

        for y in range(0, len(lis)):
            
            diff = max_len - lis[y].samples
            w =  np.zeros(diff)
            lis[y].range = np.append(lis[y].range,w)   
            
# generates a sine function
    def sine_func(self):
        """ Generates the sine function with all needed parameters"""
        return self.amp * np.sin(2*np.pi*self.freq*(self.range/self.T))

# generates a cosine function
    def cos_func(self):
        """ Generates the cosine function with all needed parameters"""
        return self.amp * np.cos(2*np.pi*self.freq*(self.range/self.T))
    
# generates a sinc function
    def sinc_func(self):
        """ Generates the sinc function with all needed parameters"""
        return self.amp * np.sinc(2*np.pi*self.freq*(self.range/self.T))
    
# writes a .wav file for the generated sinusoid
    def wav_it(self, y):
        """ Makes and saves a .wav file for the required signal"""
        nframes = self.samples
        comptype = "NONE"
        compname = "not compressed"
        nchannels = 1
        sampwidth = 2
        wav_file = wave.open("results/generated_signal.wav", "w")
        wav_file.setparams((nchannels, sampwidth,
        self.samples, nframes, comptype, compname))
        for s in y:
            wav_file.writeframes(struct.pack("h", int(s*self.amp)))
   
# plot with all info at once   
    def plot_it(self, y):
        """ Plots and saves the required signal with all information """
        plt.plot(self.range, y, label="Function")
        plt.xlabel("time (t)")
        plt.ylabel("Amplitude (a)")
        plt.legend(loc="upper right")
        plt.savefig("results/generated_sig.png")
        plt.show()

# plots the fast Fourier transform of a signal
    def fft_it(y):
        """ Plots the fast Fourier transform of a sinusoid y """
        freq = np.fft.fft(y)
        print("\n\t--------------------------------------")
        print("\tCurrent frequency range to plot: 0 to 40'000 Hz")
        limit = int(input("\n\tFrequency range to display [def: 1500]: ") or 1500)
        freq = (2/48000) * np.abs(freq[:80000//2])
        plt.plot(freq)
        plt.xlim(0, limit)
        plt.xlabel("Frequencies (Hz)")
        plt.ylabel("Amplitude (a)")
        plt.savefig("results/generated_fft.png")
        plt.show()
    
def main():    
        
    print("\t\tPlease enter the parameters for each signal below:")
    active = True
    count = 0
    comp = []
    
    while active:
        print("\n\tSignal " + str(count + 1) +": \n\t----------------------")
        
        freq    = float(input("\tFrequency [def: 100 Hz]:  ") or 100)         # Frequency
        amp     = float(input("\tAmplitude [def: 1]: ") or 1)                 # Amplitude
        samples = int(input("\tNumber of samples [def: 48000]: ") or 48000)   # number of samples
        T       = int(input("\tSampling rate [def: 48000]: ") or 48000)       # sampling rate
        typ     = (str(input("\tSignal type: [def:sin], cos, sinc: ") or "sin")).lower()
        
        inst = Sig_Gen(freq, amp, samples, T, typ)
        comp.append(inst)
        count += 1
        
        repeat = (input("""\n\tInput another signal's parameters? ([yes]/no) """)).lower()
        
        if repeat == "no" or repeat == "n":
            active = False
        else:
            pass       
    
    if len(comp) > 1:
        Sig_Gen.samp_reg(comp)
    else:
        pass
                
    return comp

if __name__ == "__main__": 
    main()




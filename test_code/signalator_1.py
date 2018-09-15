#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 12:14:15 2018

@author: Khaled Nakhleh
"""
active = True

while active:
    print("\n--------------------------")
    freq = input("\tFrequency[def=8000 Hz]:  ")  or 8000             # Frequency
    amp = input("\tAmplitude[def=15]: ")         or 15               # Amplitude
    samples = input("\tNumber of samples[def=24000]: ") or 24000     # number of samples
    T = input("\tSampling rate[def=48000]: ")  or 48000              # sampling rate
    name = (input("\nPlease Provide your name: ")).lower()
    mountain = (input("\n What mountain would you want to climb? ")).lower()

    mountains[name] = mountain

    repeat = (input("\nWould someone else want to enter their info? [yes/no] ")).lower()
    
    if repeat == "no" or repeat == "n":
    
        active = False
    
print("\n\t\t---- POLLING RESULTS ----\n")
    
for name, mountain in mountains.items():
    print("\t\t" + name.title() + " would like to climb " + mountain.title())

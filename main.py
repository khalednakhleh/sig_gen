#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 13:26:09 2018

@author: Khaled Nakhleh
"""

import class_sig as sig

def combine(lis):
    x = 0
    res = 0
    while x < (len(lis)):
        if lis[x].type == "sin":
            w = sig.Sig_Gen.sine_func(lis[x])
        elif lis[x].type == "cos":
            w = sig.Sig_Gen.cos_func(lis[x])
        elif lis[x].type == "sinc":
            w = sig.Sig_Gen.sinc_func(lis[x])
        res += w
        x = x + 1
    return res


def main():
    
    print("\n\t\t\t----Signal Combinator Software----\n")
    comp = sig.main()
    y = combine(comp)
    
    fft_rep = input("\n\tDo you wish to plot and save the FFT of the final signal? ([y]/n) ").lower()
    
    if fft_rep == "no" or fft_rep == "n":
        sig.Sig_Gen.wav_it(comp[0], y)
        sig.Sig_Gen.plot_it(comp[0], y)
    else:
        sig.Sig_Gen.wav_it(comp[0], y)
        sig.Sig_Gen.plot_it(comp[0], y)
        sig.Sig_Gen.fft_it(y)

    
    print("\n\tProcess completed. Signal graph and .wav file can be found in the results file.\n\n")
        
if __name__ == "__main__":
    main()

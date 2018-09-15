SignalSlice is a repository for viewing different signals, and to perform Fourier Fast Transform (FFT) on their combined form.

Repository uses Python 3.6, and all of its requirements can be found in the requirements file.

The code generates sinusoidal functions based on 4 parameters:

1) Frequency (F in Hz).
2) Amplitude (a in V or dB).
3) number of samples (N in samples).
4) sampling rate (in Hz or samples/second).

The code asks for a user's input on N number of signals. All of which get stored using class instances, along with its parameters. The file class_sig.py contains the class with most of the functions used. 

The file main.py uses the class file class_sig.py for inputs, then combines the signals and performs any requested options (plotting, FFT, generating .wav file). 

All the results are stored in the "results" folder. Make sure to take the file before running again, since the program will overwrite the ones existing.


author: Khaled Nakhleh
Repository url: https://github.com/KhaledNakhleh/SignalSlice

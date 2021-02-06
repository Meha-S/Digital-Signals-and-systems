#!/usr/bin/python

import sys
import time
import math

import base64
import random as random

import datetime
import time

from cpe367_wav import cpe367_wav


############################################


# define data type WAV
class Wave:
    """
    this is the waveform for each note
    A (int): Amplitude
    w1 (int) : w for frequency f at 16k sample rate
    bn (int): how many beats will the note will play
    Tn (int): time duration of the note
    bo (int): The beat at which the note starts
    to (int) : start time of the note
    n (int) : number of samples
    """
    def __init__(self, A, f, bn, bo, ph):
        self.A = int(A)
        self.w1 = f * 2 * math.pi / 16000
        self.Tn = int((bn+bo) * 0.285*16000)
        self.ph = ph
        self.to = int(bo * 0.285*16000)


# variables for note freq

G4_f = 391.995
A4_f = 440
B4_f = 493.883
C5_f = 523.251
E5_f = 659.255
D5_f = 587.330
G2_f = 97.999
G3_f = 195.998
E3_f = 164.814

#  create Waves

G4 = Wave(5000, G4_f, 1, 1, 0)
A4 = Wave(5000, A4_f, 1, 2, 0)
B4 = Wave(5000, B4_f, 1, 3, 0)
D5a = Wave(5000, D5_f, 1, 4, 0)
C5a = Wave(5000, C5_f, 1, 5, 0)
C5 = Wave(5000, C5_f, 1, 6, 0)
E5 = Wave(5000, E5_f, 1, 7, 0)
D5 = Wave(5000, D5_f, 1, 8, 0)

G2 = Wave(1000, G2_f, 3, 0, 0)
G3 = Wave(1000, G3_f, 3, 3, 0)
E3 = Wave(1000, E3_f, 3, 6, 0)

# create a list of Waves
music = [G2, G4, A4, B4, G3, D5, C5a, C5, E3, E5, D5a]
# define routine for implementing a digital filter
def process_wav(fpath_wav_out):
    """
    : this example implements a very useful system:  y[n] = x[n]
    : input and output is accomplished via WAV files
    : return: True or False
    """

    # construct objects for reading/writing WAV files
    #  assign each object a name, to facilitate status and error reporting
    wav_out = cpe367_wav('wav_out', fpath_wav_out)

    # setup configuration for output WAV
    num_channels = 1
    sample_width_8_16_bits = 16
    sample_rate_hz = 16000
    wav_out.set_wav_out_configuration(num_channels, sample_width_8_16_bits, sample_rate_hz)

    # open WAV output file
    ostat = wav_out.open_wav_out()
    if ostat == False:
        print('Cant open wav file for writing')
        return False

    ##############################################
    # writing to WAV file
    for note in music:
        # process entire input for each note
        for n in range(note.Tn):
            if n >= note.to:
                # generate a signal
                yout = note.A * math.exp(n*-0.0005)*(math.cos(note.w1 * n + note.ph)+math.sin(note.w1 * n + note.ph))

                # convert to signed int
                yout = int(round(yout))

                # output current sample
                ostat = wav_out.write_wav(yout)
                if ostat == False: break

    # close input and output files
    wav_out.close_wav()

    return True


############################################
############################################
# define main program
def main():
    # i feel better after doing this
    random.seed()

    # grab file names
    fpath_wav_out = 'lab2_1.wav'

    # let's do it!
    return process_wav(fpath_wav_out)


############################################
############################################
# call main function
if __name__ == '__main__':
    main()
    quit()

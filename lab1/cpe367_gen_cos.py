#!/usr/bin/python

import sys
import time
import math

import base64
import random as random

import datetime
import time

from cpe367_wav1 import cpe367_wav




############################################
############################################
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
	wav_out.set_wav_out_configuration(num_channels,sample_width_8_16_bits,sample_rate_hz)

	# open WAV output file
	ostat = wav_out.open_wav_out()
	if ostat == False:
		print('Cant open wav file for writing')
		return False

	##############################################
	# students - you'll need to set these parameters
	# part 1 lab 1
	# some_amp = 32768*0.75
	# some_length = 4000
	# some_w1 = 2*math.pi*500/16000
	# maybe_some_ph = math.pi / 4
	# lab 1 part 5
	some_ampA = 32768
	some_ampB = 2
	some_length = 4000
	some_w1A = 2*math.pi*2000
	some_w1B = 2 * math.pi * 500
	maybe_some_phA = math.pi / 4
	maybe_some_phB = -math.pi / 4
	some_amp = some_ampA*some_ampB/2

	# process entire input
	for n in range(0,some_length):

		# generate a signal
		# yout = some_amp * math.cos(some_w1 * n + maybe_some_ph)
		# yout = some_amp * math.cos(some_w1A * n + maybe_some_phA)*math.cos(some_w1B * n + maybe_some_phB)
		yout = some_amp * (math.cos((some_w1A + some_w1B) * n + maybe_some_phA + maybe_some_phB) + math.cos((some_w1A -
																											 some_w1B) * n + maybe_some_phA - maybe_some_phB))
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

	# check args
	if len(sys.argv) != 2:
		print('usage: include quoted name of WAV files for output')
		return False

	# grab file names
	fpath_wav_out = sys.argv[1]

	# let's do it!
	return process_wav(fpath_wav_out)




############################################
############################################
# call main function
if __name__ == '__main__':

	main()
	quit()

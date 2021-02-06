#!/usr/bin/python

import sys
import time

import base64
import random as random

import datetime
import time

from cpe367_wav1 import cpe367_wav



	
############################################
############################################
# define routine for implementing a digital filter
def process_wav(fpath_wav_in,fpath_wav_out):
	"""
	: this example implements a very useful system:  y[n] = x[n]
	: input and output is accomplished via WAV files
	: return: True or False 
	"""
	
	# construct objects for reading/writing WAV files
	#  assign each object a name, to facilitate status and error reporting
	wav_in = cpe367_wav('wav_in',fpath_wav_in)
	wav_out = cpe367_wav('wav_out',fpath_wav_out)
	
	# open wave input file
	ostat = wav_in.open_wav_in()
	if ostat == False:
		print('Cant open wav file for reading')
		return False
	
	# setup configuration for output WAV
	# num_channels = 2
	# sample_width_8_16_bits = 16
	# sample_rate_hz = 16000
	# wav_out.set_wav_out_configuration(num_channels,sample_width_8_16_bits,sample_rate_hz)
	
	# configure wave output file, mimicking parameters of input wave (sample rate...)
	wav_out.copy_wav_out_configuration(wav_in)
	
	# open WAV output file
	ostat = wav_out.open_wav_out()
	if ostat == False:
		print('Cant open wav file for writing')
		return False
		
		
	###############################################################
	###############################################################
	# students - perhaps some initialization here in future efforts...
	
		
	# process entire input
	xin = 0
	while xin != None:
	
		# read next sample (assumes mono WAV file)
		#  returns None when file is exhausted
		xin = wav_in.read_wav()
		if xin == None: break
		

		###############################################################
		###############################################################
		# students - go to work!
		
		# evaluate the difference equation
		yout = xin
		
		# students - well done!
		###############################################################
		###############################################################


		# convert to signed int
		yout = int(round(yout))
		
		# output current sample
		ostat = wav_out.write_wav(yout)
		if ostat == False: break
	
	# close input and output files
	#  important to close output - header is updated on close (with proper file size)
	wav_in.close_wav()
	wav_out.close_wav()
		
	return True





############################################
############################################
# define main program
def main():

	# i feel better after doing this
	random.seed()
	
	# check args
	if len(sys.argv) != 3:
		print('usage: include quoted names of WAV files for arguments. input first, output second')
		return False
	
	# grab file names
	fpath_wav_in = sys.argv[1]
	fpath_wav_out = sys.argv[2]

	# let's do it!
	return process_wav(fpath_wav_in,fpath_wav_out)
	
			
	
	
############################################
############################################
# call main function
if __name__ == '__main__':
	
	main()
	quit()

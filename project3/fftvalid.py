import os
import numpy as np
from scipy.io import wavfile
from scipy import fft

path = []

for fn in os.listdir('./validationwav/'):								#iterating through each file
	path.append('./validationwav/%s'%fn)								#adding file name to path list

path.sort()																#sorting file names

file = open('./fftvalidoutput.csv','ab')								#open validation output file

for i in range(100):													#iterating through 100 files
	sample_rate, X = wavfile.read(path[i])								#reading each wav file
	fft_features = abs(fft(X)[:1000])									#extracting fft features of each file
	np.savetxt(file,fft_features[None, :],fmt='%.f',delimiter=',')		#saving features to output file

file.close()															#close validation output file
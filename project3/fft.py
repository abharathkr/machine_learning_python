import numpy as np
from scipy.io import wavfile
from scipy import fft

genres = ['blues','classical','country','disco','hiphop','jazz','metal','pop','reggae','rock']

#open output file
file = open('./fftoutput.csv','ab')

for i in range(10):
	gen = genres[i]
	for j in range(10):														#reading first 10 files 0 to 9
		sample_rate, X = wavfile.read('./wav/%s.0000%d.wav'%(gen,j)) 		#reads wav file
		fft_features = abs(fft(X)[:1000]) 									#taking absolute values of first 1000 fft features
		np.savetxt(file,fft_features[None, :],fmt='%.5f',delimiter=',')		#saving the features into output file
	for k in range(10,90):													#reading files from 10 to 89
		sample_rate, X = wavfile.read('./wav/%s.000%d.wav'%(gen,k))			#reads wav file
		fft_features = abs(fft(X)[:1000])									#taking absolute values of first 1000 fft features
		np.savetxt(file,fft_features[None, :],fmt='%.5f',delimiter=',')		#saving the features into output file

#close output file
file.close()
import librosa
import os
import numpy as np

genres = ['blues','classical','country','disco','hiphop','jazz','metal','pop','reggae','rock']

#open output file
file = open('./mfcclibrosa.csv','ab')

for i in range(10):
	gen = genres[i]
	for j in range(10):											#reading first 10 files 0 to 9
		y,sr = librosa.load('./wav/%s.0000%d.wav'%(gen,j))		#load wav file using librosa
		x = librosa.feature.mfcc(y=y, sr=sr)					#extract mfcc features
		z = np.mean(x,axis=1)									#taking mean of the frames per coefficient
		np.savetxt(file,z[None, :],fmt='%f',delimiter=',')		#saving the features to the ouput file
	for k in range(10,90):										#reading files from 10 to 89
		y,sr = librosa.load('./wav/%s.000%d.wav'%(gen,k))		#load wav file using librosa
		x = librosa.feature.mfcc(y=y, sr=sr)					#extract mfcc features
		z = np.mean(x,axis=1)									#taking mean of the frames per coefficient
		np.savetxt(file,z[None, :],fmt='%f',delimiter=',')		#saving the features to the ouput file

#close output file
file.close()
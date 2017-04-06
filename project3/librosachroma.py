import librosa
import os
import numpy as np

genres = ['blues','classical','country','disco','hiphop','jazz','metal','pop','reggae','rock']

#open output file
file = open('./chromaoutput.csv','ab')

for i in range(10):
	gen = genres[i]
	for j in range(10):												#reading first 10 files 0 to 9
		y,sr = librosa.load('./wav/%s.0000%d.wav'%(gen,j))			#reading wav file by librosa
		x = librosa.feature.chroma_stft(y=y, sr=sr)					#extract chroma features
		z = np.mean(x,axis=0)										#taking mean of each frames of 12 semitones
		np.savetxt(file,z[None, :1201],fmt='%f',delimiter=',')		#saving features to output file
	for k in range(10,90):											#reading files from 10 to 89
		y,sr = librosa.load('./wav/%s.000%d.wav'%(gen,k))			#reading wav file by librosa
		x = librosa.feature.chroma_stft(y=y, sr=sr)					#extract chroma features
		z = np.mean(x,axis=0)										#taking mean of each frames of 12 semitones
		np.savetxt(file,z[None, :1201],fmt='%f',delimiter=',')		#saving features to output file

#close output file
file.close()
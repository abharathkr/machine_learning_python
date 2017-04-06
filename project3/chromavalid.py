import librosa
import os
import numpy as np

path = []

for fn in os.listdir('./validationwav/'):							#iterating through each file
	path.append('./validationwav/%s'%fn)							#adding file name to path list

path.sort()															#sorting file names

file = open('./chromavalidoutput.csv','ab')							#open validation output file

for i in range(100):												#iterating through 100 files
	y,sr = librosa.load(path[i])									#reading wav file by librosa
	x = librosa.feature.chroma_stft(y=y, sr=sr)						#extract chroma features
	z = np.mean(x,axis=0)											#taking mean of each frames of 12 semitones
	np.savetxt(file,z[None, :1201],fmt='%f',delimiter=',')			#saving features to output file

file.close()														#closing the output file

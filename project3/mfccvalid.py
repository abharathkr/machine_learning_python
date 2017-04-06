import librosa
import os
import numpy as np

path = []

for fn in os.listdir('./validationwav/'):						#iterating through each file
	path.append('./validationwav/%s'%fn)						#adding file name to path list

path.sort()														#sorting file names

file = open('./mfccvalidoutput.csv','ab')						#open validation output file

for i in range(100):											#iterating through 100 files
	y,sr = librosa.load(path[i])								#reading each wav file
	x = librosa.feature.mfcc(y=y, sr=sr)						#extracting mfcc features from the audio file
	z = np.mean(x,axis=1)										#taking mean of the frames per coefficient
	np.savetxt(file,z[None, :],fmt='%f',delimiter=',')			#saving the features to the ouput file

file.close()													#closing output file

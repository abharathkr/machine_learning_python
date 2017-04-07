#************** Project 2 *************
import math
from nltk.corpus import stopwords
import numpy as np

#stopwords
sw = stopwords.words('english')

#read files into matrices using numpy
train_labels_data = np.loadtxt('./train.label',dtype=int) # reads train.label into train_labels_data matrix
train_data = np.loadtxt('./train.data',dtype=int,delimiter=" ")
vocabulary = np.loadtxt('./vocabulary.txt',dtype=str)

lenght_of_vocabulary = len(vocabulary)
labels = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
docs_in_train_labels = [0] * 20 

j = 0
count = 0
#calculate number of documents in each newsgroup
for i in range(len(train_labels_data)):
	if train_labels_data[i] == labels[j]:
		count = count + 1
	else:
		docs_in_train_labels[j] = count
		count = 1
		j = j + 1
docs_in_train_labels[j] = count

# MLE for labels

probs_train_labels = [0] * 20
logs_of_probs_of_train_labels = []
for i in range(len(labels)):
	probs_train_labels[i] = docs_in_train_labels[i]/float(len(train_labels_data)) #p(y) - probability of a label
	logs_of_probs_of_train_labels.append(math.log(probs_train_labels[i],2))

mle = max(probs_train_labels)
# mle = 0.0531546721093

indx = probs_train_labels.index(mle)
# newsgroup is soc.religion.christian

k = 1
dictionary = {1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{},9:{},10:{},11:{},12:{},13:{},14:{},15:{},16:{},17:{},18:{},19:{},20:{}}
words_in_train_labels = [0] * 20

#counts of each word in each group calculation
number_of_docs = docs_in_train_labels[0]
for i in range(len(train_data)):
#	print docs_in_train_labels[k-1]
	if train_data[i][0] <= number_of_docs:
		if train_data[i][1] not in dictionary[k]:
			dictionary[k][train_data[i][1]] = train_data[i][2]
		else:
			dictionary[k][train_data[i][1]] = dictionary[k][train_data[i][1]] + train_data[i][2]
	else:
		number_of_docs = number_of_docs + docs_in_train_labels[k]
		k = k + 1
		dictionary[j][train_data[i][1]] = train_data[i][2]

#make count of stopwords as 1
sws = []
for i in range(len(vocabulary)):
	if vocabulary[i] in sw:
		sws.append(i+1)

for i in range(len(dictionary)):
	for j in range(len(sws)):
		if sws[j] in dictionary[i+1]:
			dictionary[i+1][sws[j]] = 1


#number of words in each group
counts = []
for i in range(len(dictionary)):
	counts.append(len(dictionary[i+1]))


beta = 0.01

test_data = np.loadtxt('./test.data',dtype=int,delimiter=" ")

def map(wordid,groupnumber):
	global beta,dictionary,vocabulary
	return (( dictionary[groupnumber][wordid] + beta ) / float(len(dictionary[groupnumber]) + (beta*len(vocabulary))))


#classifier method which prints predicted newsgroup label for each document
def classifier():
	x = 1
	summation = [0.0] * 20
	groups = [0.0] * 20
	global test_data,dictionary,lenght_of_vocabulary,logs_of_probs_of_train_labels,beta
	for m in range(len(test_data)):
		if test_data[m][0] == x:
			for n in range(20):
				if test_data[m][1] not in dictionary[n+1]:
					summation[n] = summation[n] + (test_data[m][2])*(math.log( beta / float(len(dictionary[n+1]) + (beta*lenght_of_vocabulary)),2))
				else:
					summation[n] = summation[n] + (test_data[m][2])*(math.log(map(test_data[m][1],n+1),2))
		else:
			for n in range(20):
				groups[n] = logs_of_probs_of_train_labels[n] + summation[n]
				summation[n] = 0.0
			group = max(groups)
			print groups.index(group) + 1
			x = x + 1
			for n in range(20):
				if test_data[m][1] not in dictionary[n+1]:
					summation[n] = summation[n] + (test_data[m][2])*(math.log( beta / float(len(dictionary[n+1]) + (beta*lenght_of_vocabulary)),2))
				else:
					summation[n] = summation[n] + (test_data[m][2])*(math.log(map(test_data[m][1],n+1),2))

	for n in range(20):
		groups[n] = logs_of_probs_of_train_labels[n] + summation[n]
		summation[n] = 0.0
	group = max(groups)
	print groups.index(group) + 1

classifier()
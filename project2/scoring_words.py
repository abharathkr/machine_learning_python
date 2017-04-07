#************** Project 2 *************
import math
import operator
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

beta = 0.01

#total count of words in all documents
total_count = 0
for i in range(len(dictionary)):
	for key,value in dictionary[i+1].iteritems():
		total_count = total_count + value

#calculate map - p(x|y)
def mapg(wordid,groupnumber):
	global beta,dictionary,vocabulary
	if wordid in dictionary[groupnumber]:
		return (( dictionary[groupnumber][wordid] + beta ) / float(len(dictionary[groupnumber]) + (beta*len(vocabulary))))
	else:
		return 0

#calculate probability of the word - p(x)
def prob_of_word(wordid):
	global dictionary,total_count
	word_count = 0
	for i in range(len(dictionary)):
		if wordid in dictionary[i+1]:
			word_count = word_count + dictionary[i+1].get(wordid)
	return word_count/float(total_count)

#calculate conditional entropy
def conditional_entropy(wordid):
	global probs_train_labels
	summation = 0
	for i in range(20):
		mapg_value = mapg(wordid,i+1)
		if mapg_value != 0:
			summation = summation + (probs_train_labels[i] * mapg(wordid,i+1))*(math.log( prob_of_word(wordid) / float(probs_train_labels[i] * mapg(wordid,i+1)),2))
	return summation


entropies = {}

#entropy of each word in the vocabulary
for i in range(lenght_of_vocabulary):
	entropies[i+1] = conditional_entropy(i+1)

#sorting the entropies
sorted_entropies = sorted(entropies.items(), key=operator.itemgetter(1))
#top 100 words with less entropies
top100 = sorted_entropies[:100]

#print words
for tup in top100:
	print vocabulary[tup[0] - 1]

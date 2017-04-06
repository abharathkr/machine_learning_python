import numpy as np
from sklearn import svm
from sklearn.decomposition import PCA
from time import gmtime, strftime

print strftime("%Y-%m-%d %H:%M:%S", gmtime())
training = np.loadtxt('./train.csv',delimiter=',',dtype=int)
validation = np.loadtxt('./test.csv',delimiter=',',dtype=int)
print strftime("%Y-%m-%d %H:%M:%S", gmtime())
print "files loaded"

labels = training[:,0]
traindata = np.delete(training,0,1)

pca = PCA(n_components=700)

pca.fit(traindata,labels)
pcafittrain = pca.transform(traindata)
pcafittest = pca.transform(validation)
print strftime("%Y-%m-%d %H:%M:%S", gmtime())
print "pca done"

print len(pcafittrain[0])
print len(pcafittest[0])

classifier = svm.SVC(kernel='poly')

print "starting svm fit"
print strftime("%Y-%m-%d %H:%M:%S", gmtime())
classifier.fit(pcafittrain,labels)
print strftime("%Y-%m-%d %H:%M:%S", gmtime())
print "svm fit done"

result = classifier.predict(pcafittest)
print "prediction done"
print strftime("%Y-%m-%d %H:%M:%S", gmtime())
print "ImageID,Label"
for i in range(28000):
	print '%d,%d' % ((i+1),result[i])
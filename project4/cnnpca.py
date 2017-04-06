import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages')
import numpy as np
#from sklearn import svm
from sklearn.decomposition import PCA
import pandas as pd
from sknn.mlp import Classifier,Layer
from sknn.mlp import Convolution

training = np.loadtxt('./train.csv',delimiter=',',dtype=int)
validation = np.loadtxt('./test.csv',delimiter=',',dtype=int)
labels = training[:,0]
traindata = np.delete(training,0,1)
pca = PCA()
pca.fit(traindata,labels)
pcafittrain = pca.transform(traindata)
pcafittest = pca.transform(validation)
print "pca done"

c = Classifier(layers=[Convolution("Rectifier", channels=18, pool_shape=(2,2),kernel_shape=(5,5), 
	border_mode='valid'),Layer('Rectifier', units=200),Layer('Softmax')],learning_rate=0.00001,learning_rule='nesterov',
	learning_momentum=0.9, batch_size=300, valid_size=0.0, 
	normalize='L1',n_stable=10, n_iter=10, verbose=True)

c.fit(pcafittrain,labels)
print "fitting done"
result = c.predict(pcafittest).ravel()
print "result"
print result
x = list(range(1,28001))
df = pd.DataFrame({"ImageID" : x, "Label" : result})
df.to_csv('outo.csv',index=False)
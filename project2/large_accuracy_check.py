#accuracy percentage values for different values of beta
#generates only one file containing predicted newsgroup labels for all values of beta

import numpy as np

test_labels = np.loadtxt('./test.label',dtype=int)
output_labels = np.loadtxt('./large_output.txt',dtype=int)

j = 0
for k in range(15):
	count = 0
	for i in range(len(test_labels)):
		if test_labels[i] == output_labels[j]:
			count = count + 1
		j = j + 1
	print count * 100/ float(len(test_labels))
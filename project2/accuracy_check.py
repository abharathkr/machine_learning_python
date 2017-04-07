#code to check the accuracy percentage with beta = 0.01 

import numpy as np

test_labels = np.loadtxt('./test.label',dtype=int)
output_labels = np.loadtxt('./output.txt',dtype=int)

count = 0

for i in range(len(test_labels)):
	if test_labels[i] == output_labels[i]:
		count = count + 1

#prints the accuracy percentage
print count * 100/ float(len(test_labels))
#prints confusion matrix

import numpy as np

test_labels = np.loadtxt('./test.label',dtype=int)
output_labels = np.loadtxt('./output.txt',dtype=int)

x=1

confusion_matrix = [[0]*20 for i in range(20)]

for i in range(len(test_labels)):
	if test_labels[i] == x:
		confusion_matrix[x-1][output_labels[i]-1] = confusion_matrix[x-1][output_labels[i]-1] + 1
	else:
		confusion_matrix[x-2][output_labels[i]-1] = confusion_matrix[x-2][output_labels[i]-1] + 1
		x = x + 1

for i in range(len(confusion_matrix)):
	print confusion_matrix[i]
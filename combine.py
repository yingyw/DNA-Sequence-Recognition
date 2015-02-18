#!/usr/env/bin/python

import numpy as np
from collections import Counter
import math
import scipy
import scipy.stats as st
import heapq, random
lineNumber = 0
data = np.zeros((4, 150))
l = []
for line in open('output1.dat'):
	line = line.split()
	if line:
		line = [int(i) for i in line]
		l.append(line)
		data[lineNumber] = line
	lineNumber += 1
def col(matrix, i):
	return [row[i] for row in matrix]
result = []
# print data
for i in range(150):
	column = col(data, i)
	# counts = np.bincount(column)
	# result.append(np.argmax(counts))
	#print column.count(0), column.count(1), column.count(2)
	#result.append(max(column.count(0), column.count(1), column.count(2)))
	if (max(column.count(0), column.count(1), column.count(2)) == column.count(0)):
		result.append(0)
	if (max(column.count(0), column.count(1), column.count(2)) == column.count(1)):
		result.append(1)
	if (max(column.count(0), column.count(1), column.count(2)) == column.count(2)):
		result.append(2)

# print len(result)
# print result
same = 0
testY = []
testyFile = "ytest34.txt"
for c in open(testyFile):
	lineNumber += 1;
	testY.append(int(c))
# for i in range(150):
# 	if (result[i] == testY[i]):
# 		same += 1
# percentage = same * 1.0/ 150
# print percentage

same = 0
s0 = 0
s1 = 0
s2 = 0
for i in range(150):
	if (result[i] == testY[i]):
		same += 1
		if (result[i] == 0):
			s0 += 1
		if (result[i] == 1):
			s1 += 1
		if (result[i] == 2):
			s2 += 1
percentage = same * 1.0/ 150
p0 = s0 * 1.0 / same
p1 = s1  * 1.0/ same
p2 = s2 * 1.0/ same
print s0, s1, s2
print p0, p1, p2
print percentage
print same
print result.count(0)
print result.count(1)
print result.count(2)
print testY.count(0)
print testY.count(1)
print testY.count(2)
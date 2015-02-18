#!/usr/env/bin/python

import numpy as np
import math
import scipy
import scipy.stats as st

#read Y-train data
lineNumber = 0
originalY = []
for c in open('splice-Ytrain.dat'):
	lineNumber += 1;
	originalY.append(int(c))

#read X-train data
def Datatype(line):
	dataLine = []
	for i in range(60):
		if (line[i] == 'A'):
			dataLine.append(1)
		if (line[i] == 'C'):
			dataLine.append(2)
		if (line[i] == 'G'):
			dataLine.append(3)
		if (line[i] == 'T'):
			dataLine.append(4)
		if (line[i] == 'D'):
			dataLine.append(0)
		if (line[i] == 'N'):
			dataLine.append(0)
		if (line[i] == 'S'):
			dataLine.append(0)
		if (line[i] == 'R'):
			dataLine.append(0)
	return dataLine;

result = []
originalX = np.zeros((3000, 60))
remain = 0;
count = 0;
for line in open ('splice-Xtrain.dat'):
	result = Datatype(line)
	if (result.count(0) == 0):
		originalX[remain] = result;
		remain += 1
	else :
		originalY[count] = 3
	count += 1


dataX = np.zeros((remain, 60));
for i in range(remain):
	dataX[i] = originalX[i]
#print dataY

dataY = []
for y in originalY:
	if (y != 3):
		dataY.append(y)

Pc = [0.0, 0.0, 0.0]

for i in range(3):
	Pc[i] = dataY.count(i) * 1.0 /len(dataY)


print Pc
print dataY.count(0)
print dataY.count(1)
print dataY.count(2)

# categroies
count0 = 0
count1 = 0
count2 = 0
count = 0
c0 = np.zeros((1519, 60))
c1 = np.zeros((704, 60))
c2 = np.zeros((720, 60))
for y in dataY:
	if (y == 0):
		c0[count0] = dataX[count]
		count0 += 1
	if (y == 1):
		c1[count1] = dataX[count]
		count1 += 1
	if (y == 2):
		c2[count2] = dataX[count]
		count2 += 1
	count += 1
c = [c0, c1, c2]

def col(matrix, i):
    return [row[i] for row in matrix]

PxcList = []
for j in range(60):
	Pxc = np.zeros((3, 4))
	for i in range(3):
		column = col(c[i], j)
		for k in range(4):
			Pxc[i][k] = (column.count(k + 1) * 1.0)/len(column)
		# Pxc[i][0] = column.count(1) * 1.0/len(column)
		# Pxc[i][1] = column.count(2) * 1.0/len(column)
		# Pxc[i][2] = column.count(3) * 1.0/len(column)
		# Pxc[i][3] = column.count(4) * 1.0/len(column)
	PxcList.append(Pxc)

testxFile = 'test34.txt'
testyFile = 'ytest34.txt'

result = []
testX = np.zeros((150, 60))
remain = 0;
for line in open (testxFile):
	result = Datatype(line)
	if (result.count(0) == 0):
		testX[remain] = result;
		remain += 1

lineNumber = 0
testY = []
for c in open(testyFile):
	lineNumber += 1;
	testY.append(int(c))

testResult = []
estimate = []
for row in range(150):
	for c in range(3):
		result = Pc[c]
		for column in range(60):
			for i in range(4):
				if (testX[row][column] == (i+1)):
					number = PxcList[column][c][i]
					result *= number
		estimate.append(result)
	testResult.append(estimate.index(max(estimate)))
	estimate = []
print testResult

# same = 0
# for i in range(150):
# 	if (testResult[i] == testY[i]):
# 		same += 1
# percentage = same * 1.0/ 150

# print percentage
# print same
# print PxcList[0]
# print PxcList[0]

same = 0
s0 = 0
s1 = 0
s2 = 0
for i in range(150):
	if (testResult[i] == testY[i]):
		same += 1
		if (testResult[i] == 0):
			s0 += 1
		if (testResult[i] == 1):
			s1 += 1
		if (testResult[i] == 2):
			s2 += 1
percentage = same * 1.0/ 150
p0 = s0 * 1.0 / same
p1 = s1  * 1.0/ same
p2 = s2 * 1.0/ same
print s0, s1, s2
print p0, p1, p2
print percentage
print same
print testResult.count(0)
print testResult.count(1)
print testResult.count(2)
print testY.count(0)
print testY.count(1)
print testY.count(2)












	


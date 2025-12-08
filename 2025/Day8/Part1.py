import math
import requests

url = 'https://adventofcode.com/2025/day/8/input'
session = '53616c7465645f5f7ae7e21264f5ae862c9dbcce56a09049f1bb7dde3b67ec13c4116eb85355d0e96aa6497511c5c7e65cbdbd93bd13629425228fae49a2b4a3'
input = requests.get(url, cookies={'session': session}).text.strip()

input = input.split('\n')
tempInput = input[:]
for i in range(len(tempInput)):
	input[i] = tuple(int(x) for x in tempInput[i].split(','))

distDict = {}
for y in range(len(input)):
	for x in range(len(input)):
		if input[y]==input[x] or (input[x], input[y]) in distDict:
			continue
		distDict[(input[y],input[x])] =  math.sqrt(pow(input[y][0]-input[x][0],2)+pow(input[y][1]-input[x][1],2) + pow(input[y][2]-input[x][2],2))

sortedKV = sorted(distDict.items(),key=lambda x: x[1])

circuits = []
i=0
while i<len(sortedKV):
	boxes = sortedKV[i][0]
	c1=None
	c2=None
	for c in circuits:
		if boxes[0] in c:
			c1 = c
		if boxes[1] in c:
			c2 = c
	if c1==None and c2==None:
		circuits.append(set([boxes[0], boxes[1]]))
		retVal = boxes[0][0]*boxes[1][0]
	elif c1==None:
		c2.add(boxes[0])
		retVal = boxes[0][0]*boxes[1][0]
	elif c2==None:
		c1.add(boxes[1])
		retVal = boxes[0][0]*boxes[1][0]
	elif not c1==c2:
		circuits.append(c1.union(c2))
		circuits.remove(c1)
		circuits.remove(c2)
		retVal = boxes[0][0]*boxes[1][0]
	i+=1

total = 1
print(retVal)

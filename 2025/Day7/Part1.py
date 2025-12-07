import requests

url = 'https://adventofcode.com/2025/day/7/input'
session = '53616c7465645f5f7ae7e21264f5ae862c9dbcce56a09049f1bb7dde3b67ec13c4116eb85355d0e96aa6497511c5c7e65cbdbd93bd13629425228fae49a2b4a3'
input = requests.get(url, cookies={'session': session}).text.strip()

input = input.split('\n')

startX=0
startY=0
found = False
for y in range(len(input)):
	if not found:
		for x in range(len(input[0])):
			if input[y][x]=='S':
				startX = x
				startY = y
	input[y] = list(input[y])

split = 0
stk = [[startX, startY]]
while len(stk)>0:
	coords = stk.pop()
	x = coords[0]
	y = coords[1]
	while y<len(input):
		if input[y][x]=='^':
			if x-1>=0 and input[y][x-1]!='|':
				stk.append([x-1, y])
			if x+1<len(input[0]) and input[y][x+1]!='|':
				stk.append([x+1, y])
			split+=1
			break
		elif input[y][x]=='|':
			break
		input[y][x]='|'
		y+=1
print(split)

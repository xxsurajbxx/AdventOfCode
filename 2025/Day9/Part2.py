'''
import requests

url = 'https://adventofcode.com/2025/day/9/input'
session = '53616c7465645f5f7ae7e21264f5ae862c9dbcce56a09049f1bb7dde3b67ec13c4116eb85355d0e96aa6497511c5c7e65cbdbd93bd13629425228fae49a2b4a3'
input = requests.get(url, cookies={'session': session}).text.strip()
'''
input='''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''

input = input.split('\n')
for i in range(len(input)):
	input[i] = input[i].split(',')
	input[i][0] = int(input[i][0])
	input[i][1] = int(input[i][1])

biggestArea = 0
for x in range(len(input)-1):
	prev = input[x-1]
	if prev[1]<input[x][1]:
		prevDirection = 'above'
	elif prev[1]>input[x][1]:
		prevDirection = 'below'
	elif prev[0]<input[x][0]:
		prevDirection = 'left'
	elif prev[0]>input[x][1]:
		prevDirection = 'right'

	next = input[x+1 if x+1<len(input) else 0]
	if next[1]<input[x][1]:
                nextDirection = 'above'
	elif next[1]>input[x][1]:
                nextDirection = 'below'
	elif next[0]<input[x][0]:
                nextDirection = 'left'
	elif next[0]>input[x][1]:
		nextDirection = 'right'

	y=x+1
	while y!=x:
		next = input[y+1 if y+1<len(input) else 0]
		if next[1]<input[y][1]:
			nextYDir = 'above'
		elif next[1]>input[y][1]:
			nextYDir = 'below'
		elif next[0]<input[x][0]:
			nextYDir = 'left'
		elif next[0]>input[x][0]:
			nextYDir = 'right'

		if prevDirection=='below' and nextDirection=='right' and (input[x][0]<input[y][0] and input[x][1]<input[y][1] and not nextYDir=='above'):
			print(f'potential candidate: {input[x]} to {input[y]}')
		elif prevDirection=='left' and nextDirection=='below' and (input[x][0]>input[y][0] and input[x][1]<input[y][1] and not nextYDir=='above'):
			print(f'potential candidate: {input[x]} to {input[y]}')
		area = (abs(input[x][0]-input[y][0])+1)*(abs(input[x][1]-input[y][1])+1)
		if area>biggestArea:
			biggestArea = area
		y+=1
		if y==len(input):
			y=0

print(biggestArea)

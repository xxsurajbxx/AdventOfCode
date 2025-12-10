import requests

url = 'https://adventofcode.com/2025/day/9/input'
session = '53616c7465645f5f7ae7e21264f5ae862c9dbcce56a09049f1bb7dde3b67ec13c4116eb85355d0e96aa6497511c5c7e65cbdbd93bd13629425228fae49a2b4a3'
input = requests.get(url, cookies={'session': session}).text.strip()

input = input.split('\n')
for i in range(len(input)):
	input[i] = input[i].split(',')
	input[i][0] = int(input[i][0])
	input[i][1] = int(input[i][1])

biggestArea = 0
for x in range(len(input)-1):
	for y in range(x+1, len(input)):
		area = (abs(input[x][0]-input[y][0])+1)*(abs(input[x][1]-input[y][1])+1)
		if area>biggestArea:
			biggestArea = area

print(biggestArea)

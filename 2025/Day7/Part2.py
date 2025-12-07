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

dp = [[0 for a in range(len(input[0]))] for b in range(len(input))]
dp[startY][startX] = 1
for y in range(1, len(input)):
	for x in range(len(input[0])):
		if input[y][x]=='^':
			if x-1>=0:
				dp[y][x-1]+=dp[y-1][x]
			if x+1<len(input[0]):
				dp[y][x+1]+=dp[y-1][x]
		else:
			dp[y][x]+=dp[y-1][x]

paths=0
for x in range(len(input[0])):
	paths+=dp[-1][x]
print(paths)

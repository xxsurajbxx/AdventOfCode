import requests

url = 'https://adventofcode.com/2025/day/6/input'
session = '53616c7465645f5f36fc66b8ff0a10c145a8c64d8d3913818417fd3a435ee92da7384d615fd84694938c798ae97a1b30f66be2097bc2ac62a39c0d24ced84f79'
input = requests.get(url, cookies={'session': session}).text.strip()

input = input.split('\n')
for x in range(len(input)):
	input[x] = input[x].split()

total = 0
for x in range(len(input[0])):
	add = input[-1][x]=='+'
	if add:
		t=0
	else:
		t=1
	for y in range(len(input)-1):
		if add:
			t+=int(input[y][x])
		else:
			t*=int(input[y][x])
	total += t
print(total)

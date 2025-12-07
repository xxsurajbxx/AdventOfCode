import requests

url = 'https://adventofcode.com/2025/day/6/input'
session = '53616c7465645f5f36fc66b8ff0a10c145a8c64d8d3913818417fd3a435ee92da7384d615fd84694938c798ae97a1b30f66be2097bc2ac62a39c0d24ced84f79'
input = requests.get(url, cookies={'session': session}).text.strip()

input = input.split('\n')

total=0
numbers = []

for x in range(len(input[0])-1, -1, -1):
	digits = []
	for y in range(0, len(input)-1):
		if input[y][x]!=' ':
			digits.append(int(input[y][x]))
	num = 0
	for d in range(len(digits)):
		num += pow(10,len(digits)-(d+1))*digits[d]

	if len(digits)!=0:
		numbers.append(num)
	else:
		numbers=[]

	if x<len(input[-1]):
		if input[-1][x]=='+':
			t=0
			for i in numbers:
				t+=i
			total+=t

		elif input[-1][x]=='*':
			t=1
			for i in numbers:
				t*=i
			total+=t
print(total)

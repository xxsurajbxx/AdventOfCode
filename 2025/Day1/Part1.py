import requests

url = 'https://adventofcode.com/2025/day/1/input'
input = requests.get(url, cookies={'session': '53616c7465645f5f36fc66b8ff0a10c145a8c64d8d3913818417fd3a435ee92da7384d615fd84694938c798ae97a1b30f66be2097bc2ac62a39c0d24ced84f79'}).text
input = input.split()
dial = 50
counter = 0
for i in input:
	if i[0]=='L':
		mult=-1
	else:
		mult=1
	dial = (dial+mult*int(i[1:]))%100
	if dial==0:
		counter+=1
print(counter)

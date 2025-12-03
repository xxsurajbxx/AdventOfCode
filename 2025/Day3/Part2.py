import requests

url = 'https://adventofcode.com/2025/day/3/input'
session = '53616c7465645f5f36fc66b8ff0a10c145a8c64d8d3913818417fd3a435ee92da7384d615fd84694938c798ae97a1b30f66be2097bc2ac62a39c0d24ced84f79'
input = requests.get(url, cookies={'session': session}).text.strip()
input = input.split()

#input = ['987654321111111','811111111111119','234234234234278','818181911112111']

total = 0
for bank in input:
	numbersToFind = 12
	batteries = []
	largestInd=-1
	n=0
	for i in range(numbersToFind):
		largest = -1
		for j in range(largestInd+1, len(bank)-(numbersToFind-1)):
			if int(bank[j])>largest:
				largest = int(bank[j])
				largestInd = j
		numbersToFind-=1
		n += largest*pow(10,numbersToFind)
	total += n
print(total)

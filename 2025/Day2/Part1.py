import requests

url = 'https://adventofcode.com/2025/day/2/input'
input = requests.get(url, cookies={'session': '53616c7465645f5f36fc66b8ff0a10c145a8c64d8d3913818417fd3a435ee92da7384d615fd84694938c798ae97a1b30f66be2097bc2ac62a39c0d24ced84f79'}).text.strip()
input = input.split(',')

#input = ['11-22', '95-115', '998-1012', '1188511880-1188511890', '222220-222224', '1698522-1698528', '446443-446449', '38593856-38593862', '565653-565659', '824824821-824824827', '2121212118-2121212124']

invalidIDs = []
total = 0
for i in input:
	interval = i.split('-')
	for x in range(int(interval[0]), int(interval[1])+1):
		xstr = str(x)
		if len(xstr)%2==0:
			if xstr[:int(len(xstr)/2)]==xstr[int(len(xstr)/2):]:
				invalidIDs.append(x)
				total+=x
#print(invalidIDs)
print(total)

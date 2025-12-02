import requests

url = 'https://adventofcode.com/2025/day/1/input'
input = requests.get(url, cookies={'session': '53616c7465645f5f36fc66b8ff0a10c145a8c64d8d3913818417fd3a435ee92da7384d615fd84694938c798ae97a1b30f66be2097bc2ac62a39c0d24ced84f79'}).text
input = input.split()

#input = ['L50', 'L500']

#input = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']

dial = 50
counter1 = 0
counter2 = 0
for i in input:
	if i[0]=='L':
		mult=-1
	else:
		mult=1
	turn = dial+mult*int(i[1:])
	if turn%100==0:
		counter1+=1
	if turn<0 or turn>100:
		counter2+=abs(int((turn+(1 if turn<0 else -1))/100))
		if turn<0 and dial!=0:
			counter2+=1
	dial = turn%100
print(f'C1: {counter1}')
print(f'C2: {counter2}')
print(counter1+counter2)

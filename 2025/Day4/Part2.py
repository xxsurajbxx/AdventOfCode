import requests

url = 'https://adventofcode.com/2025/day/4/input'
session = '53616c7465645f5f7ae7e21264f5ae862c9dbcce56a09049f1bb7dde3b67ec13c4116eb85355d0e96aa6497511c5c7e65cbdbd93bd13629425228fae49a2b4a3'
input = requests.get(url, cookies={'session': session}).text.strip()
input = input.split()

#input = '''..@@.@@@@.\n@@@.@.@.@@\n@@@@@.@.@@\n@.@@@@..@.\n@@.@@@@.@@\n.@@@@@@@.@\n.@.@.@.@@@\n@.@@@.@@@@\n.@@@@@@@@.\n@.@.@@@.@.'''
#input = input.split()

input = [list(s) for s in input]
output = [list(s) for s in input]
total = 0
removedARoll = True
while removedARoll:
	removedARoll = False
	for row in range(len(input)):
		rowAbove=True if row+1 <len(input) else False
		rowBelow=True if row-1 >=0 else False
		for col in range(len(input[0])):
			if input[row][col]=='@':
				adjRolls = 0
				colBelow = True if col-1 >=0 else False
				colAbove = True if col+1 <len(input[0]) else False
				if colBelow:
					if input[row][col-1]=='@':
						adjRolls+=1
					if rowAbove and input[row+1][col-1]=='@':
						adjRolls+=1
					if rowBelow and input[row-1][col-1]=='@':
						adjRolls+=1
				if colAbove:
					if input[row][col+1]=='@':
						adjRolls+=1
					if rowAbove and input[row+1][col+1]=='@':
						adjRolls+=1
					if rowBelow and input[row-1][col+1]=='@':
						adjRolls+=1
				if rowAbove and input[row+1][col]=='@':
					adjRolls+=1
				if rowBelow and input[row-1][col]=='@':
					adjRolls+=1
				if adjRolls<4:
					total+=1
					output[row][col] = '.'
					removedARoll = True
	input = output
#for x in output:
#	print(x[:])
print(total)

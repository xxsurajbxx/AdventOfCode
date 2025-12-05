import requests

url = 'https://adventofcode.com/2025/day/5/input'
session = '53616c7465645f5f36fc66b8ff0a10c145a8c64d8d3913818417fd3a435ee92da7384d615fd84694938c798ae97a1b30f66be2097bc2ac62a39c0d24ced84f79'
input = requests.get(url, cookies={'session': session}).text

input = input.split('\n\n')
input[0] = input[0].split()
input[1] = input[1].split()

i = []
for inpt in input[0]:
	x = inpt.find('-')
	i.append([int(inpt[:x]), int(inpt[x+1:])])
input[0] = i
input[0].sort(key=lambda x: x[1])

def mergeIntervals(intervals):
	i=1
	while i<len(intervals):
		if i-1>=0 and intervals[i-1][1] >= intervals[i][0]:
			intervals[i] = [min(intervals[i-1][0], intervals[i][0]), intervals[i][1]]
			intervals.pop(i-1)
			i-=1
		else:
			i+=1

def intervalBinarySearch(ID, sortedIntervals):
	start = 0
	end = len(sortedIntervals)-1
	while start<=end:
		mid = int((start+end)/2)
		if ID>=sortedIntervals[mid][0] and ID<=sortedIntervals[mid][1]:
			return True
		elif ID>sortedIntervals[mid][1]:
			start = mid+1
		elif ID<sortedIntervals[mid][1]:
			end = mid-1
	return False

mergeIntervals(input[0])

freshCount = 0
for interval in input[0]:
	freshCount+=(interval[1]-interval[0])+1
print(freshCount)


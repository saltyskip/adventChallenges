from itertools import chain, combinations
from operator import mul

weights = []
with open('input') as fp:
	for line in fp.readlines():
		weights.append(int(line.strip()))
print len(weights)
setWeight = sum(weights) / 4
partitions = []


def findSubsets(weights,stored,setWeight):
	global partitions
	if sum(stored) == setWeight:
		if sum(weights) == 2*setWeight:
			print 'done'
			partitions.append(stored)
			return
		else: return
	if sum(stored) > setWeight or len(weights) == 0:
		print 'done'
		return
	findSubsets(weights[1:], stored + [weights[0]], setWeight)
	findSubsets(weights[1:], stored, setWeight)

def findSubsets2(weights):
	for x in range(len(weights)):
		toCheck = [reduce(mul, c) for c in combinations(weights,x) if sum(c) == setWeight]
		if (toCheck): return min(toCheck)

print findSubsets2(weights)

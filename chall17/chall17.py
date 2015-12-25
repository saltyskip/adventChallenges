from sets import Set
MAX_WEIGHT = 150
weights = []
permutations  = {}
lengths = []
NUM_WEIGHTS = 20

def knapsack(curr_weight,weights):
	if curr_weight==MAX_WEIGHT:
		return 1
	if curr_weight > MAX_WEIGHT or len(weights) == 0:
		return 0
	first = weights[0]
	rest = weights[1:]
	return knapsack(curr_weight + first, rest) + knapsack(curr_weight, rest)

def knapsack2(curr_weight,weights, count = 4):
	if curr_weight==MAX_WEIGHT and count == 0:
		return 1
	if curr_weight > MAX_WEIGHT or len(weights) == 0:
		return 0
	first = weights[0]
	rest = weights[1:]
	return knapsack2(curr_weight + first, rest, count - 1) + knapsack2(curr_weight, rest, count)

with open('input') as fp:
	for line in fp.readlines():
		weights.append(int(line.strip()))

print knapsack2(0,weights)

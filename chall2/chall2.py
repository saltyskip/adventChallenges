from numpy import prod

def data_read():
	dimensions = []
	with open('input') as fp:
	    for line in fp:
	    	dims = line.rstrip('\n').split('x')
	    	dimensions.append([int(x) for x in dims])
	    	dimensions[-1].sort()
	return dimensions

def calc_wrapping(dimensions):
	total_paper = 0
	for box in dimensions:
		total_paper += 2*(box[0]*box[1] + box[1]*box[2] + box[0]*box[2]) \
					+ min(box[0]*box[1], box[1]*box[2], box[0]*box[2])
	return total_paper

def calc_ribbon(dimensions):
	total_ribbon = 0
	for box in dimensions:
		total_ribbon += 2*(box[0] + box[1]) + prod(box)
	return total_ribbon

dimensions= data_read()
print calc_ribbon(dimensions)
print calc_wrapping(dimensions)        
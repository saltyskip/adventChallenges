difference = 0
with open('input') as fp:
	for line in fp:
		difference+= len(line[:-1]) - len(eval(line))
print difference

difference = 0
with open('input') as fp:
	for line in fp:
		difference += 2 + line.count('\\') + line.count('"')
print difference
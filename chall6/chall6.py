instructions = []
#instruction_type: 
#	0-turnOff
#	1-turnOn
#	2-toglle
#data structures (instruction_type, (left corner), (right_corner))

#converts string '111,222' to (111,222) example
def stringPairToTuple(pair):
	individuals = pair.split(',')
	return (int(individuals[0]), int(individuals[1]))

def setLights(instructions):
	grid = [[0 for x in range(1000)] for y in range(1000)]
	for instruction in instructions:
		for row in range(instruction[1][0], instruction[2][0]+1):
			for col in range(instruction[1][1], instruction[2][1]+1):
				if instruction[0] == 2:
					grid[row][col] = 1 - grid[row][col]
				else:
					grid[row][col] = instruction[0]
	return grid

def setLightsBrightness(instructions):
	grid = [[0 for x in range(1000)] for y in range(1000)]
	for instruction in instructions:
		for row in range(instruction[1][0], instruction[2][0]+1):
			for col in range(instruction[1][1], instruction[2][1]+1):
				if instruction[0] == 2:
					grid[row][col] += 2
				elif instruction[0] == 1:
					grid[row][col] += 1
				else:
					grid[row][col] = 0 if grid[row][col] == 0 else grid[row][col]-1
	return grid

def countLights(grid):
	lightsOn = 0
	for row in range(1000):
		for col in range(1000):
			lightsOn+=grid[row][col]
	return lightsOn


instructions = []
with open('input') as fp:
	for line in fp:
		unsanitized = line.rstrip('\n').split()
		data = ()
		if unsanitized[0] == 'toggle':
			data = (2,stringPairToTuple(unsanitized[1]),stringPairToTuple(unsanitized[3]))
		else:
			if unsanitized[1] == 'off':
				data = (0,stringPairToTuple(unsanitized[2]),stringPairToTuple(unsanitized[4]))		
			else:
				data = (1,stringPairToTuple(unsanitized[2]),stringPairToTuple(unsanitized[4]))
		instructions.append(data)

grid = setLightsBrightness(instructions)
print countLights(grid)
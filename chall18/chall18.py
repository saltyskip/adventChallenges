grid = []
NUM_STEPS = 100
with open('input') as fp:
	for line in fp.readlines():
		grid.append(list(line.strip()))

def get_same_neighbors(row, col, grid):
	num_neighbors = 0
	for r in range(row-1, row+2):
		for c in range(col-1, col+2):
			if (r == row and c == col) or (c == -1) or (r == -1):
				continue
			try:
				if grid[r][c] == '#':
					num_neighbors+=1
			except:
				continue
	return num_neighbors


def game_of_lights(grid):
	for x in range(NUM_STEPS):
		new_grid = []
		for row in range(len(grid)):
			new_row = []
			for col in range(len(grid[0])):
				if grid[row][col] == '#':
					if get_same_neighbors(row,col,grid) == 2 or get_same_neighbors(row,col,grid) == 3:
						new_row.append('#')
					else:
						new_row.append('.')
				else:
					if get_same_neighbors(row,col,grid) == 3:
						new_row.append('#')
					else:
						new_row.append('.')
			new_grid.append(new_row)
		grid = new_grid
	return grid

def game_of_lights2(grid):
	grid[0][0] = "#"
	grid[0][99] = "#"
	grid[99][0] = "#"
	grid[99][99] = "#"
	for elem in grid:
		print elem
	print
	for x in range(NUM_STEPS):
		new_grid = []
		for row in range(len(grid)):
			new_row = []
			for col in range(len(grid[0])):
				if (row,col) == (0,0) or (row,col) == (0,99) or (row,col) == (99,99) or (row,col) == (99,0):
					new_row.append('#')
					continue 
				if grid[row][col] == '#':
					if get_same_neighbors(row,col,grid) == 2 or get_same_neighbors(row,col,grid) == 3:
						new_row.append('#')
					else:
						new_row.append('.')
				else:
					if get_same_neighbors(row,col,grid) == 3:
						new_row.append('#')
					else:
						new_row.append('.')
			new_grid.append(new_row)
		grid = new_grid
	return grid	

def count_lights(grid):
	lights_on = 0
	for row in range(len(grid)):
		for col in range(len(grid[0])):
			if grid[row][col] == '#': lights_on += 1
	print lights_on
grid = game_of_lights2(grid)
count_lights(grid)

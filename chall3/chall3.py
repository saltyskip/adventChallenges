def updateLocation(loc, move):
	if move == '>':return (loc[0]+1,loc[1])
	if move == '<':return (loc[0]-1,loc[1])
	if move == '^':return (loc[0],loc[1]+1)
	if move == 'v':return (loc[0],loc[1]-1)

def deliverPresents(directions):
	
	#form is tuple to number of times visited
	locations = {}
	sL =(0,0) #startLocation
	for move in directions:
		locations[sL] = locations.get(sL, 0) + 1
		sL=updateLocation(sL,move)
	locations[sL] = locations.get(sL, 0) + 1
	return len(locations)

def deliverPresentsRoboSanta(directions):
	locations = {}
	sLS =(0,0) #startLocationSanta
	sLR =(0,0) #startLocationRobot
	santaTurn = True
	for move in directions:
		if santaTurn:
			locations[sLS] = locations.get(sLS, 0) + 1
			sLS = updateLocation(sLS,move)
		else:
			locations[sLR] = locations.get(sLR, 0) + 1
			sLR = updateLocation(sLR,move)
		santaTurn = not santaTurn

	locations[sLR] = locations.get(sLR, 0) + 1
	locations[sLS] = locations.get(sLS, 0) + 1
	return len(locations)

f = open('input', 'r')
directions = f.read().strip('\n')
print deliverPresents(directions)
print deliverPresentsRoboSanta(directions)
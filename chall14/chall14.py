#data format {name: [speed,travelTime,restTime, currDist, state, restCounter, travelCounter)]
reindeer = []
NAME, SPEED, TRAVEL_T = 0,1,2 
REST_T, CURR_D, FLYING = 3,4,5 
REST_C, TRAVEL_C, POINTS = 6,7,8


def simulateRace(reindeer):
	winningDist = 0
	winnerName = None
	flying = True
	for t in range(2503):
		for deer in reindeer:
			if deer[FLYING]:
				deer[CURR_D] += deer[SPEED]
				deer[TRAVEL_C] += 1
				if deer[TRAVEL_C] == deer[TRAVEL_T]:
					deer[FLYING] = False 
					deer[TRAVEL_C] = 0
			else:
				deer[REST_C] += 1
				if deer[REST_C] == deer[REST_T]:
					deer[FLYING] = True 
					deer[REST_C] = 0
	return reindeer

def simulateRace2(reindeer):
	winningDist = 0
	winnerName = None
	flying = True
	for t in range(2503):
		for deer in reindeer:
			if deer[FLYING]:
				deer[CURR_D] += deer[SPEED]
				deer[TRAVEL_C] += 1
				if deer[TRAVEL_C] == deer[TRAVEL_T]:
					deer[FLYING] = False 
					deer[TRAVEL_C] = 0
			else:
				deer[REST_C] += 1
				if deer[REST_C] == deer[REST_T]:
					deer[FLYING] = True 
					deer[REST_C] = 0
		leadDistance = max(reindeer, key = lambda x:x[CURR_D])[CURR_D]
		for deer in reindeer:
			if deer[CURR_D] == leadDistance: deer[POINTS] += 1			
	return reindeer



with open('input') as fp:
	for line in fp.readlines():
		toParse = line.split()
		reindeer.append([toParse[0],int(toParse[3]), int(toParse[6]), int(toParse[13]), 0, True, 0, 0,0])
#for x in simulateRace(reindeer):
#	print x[CURR_D]

for x in simulateRace2(reindeer):
	print x[POINTS]


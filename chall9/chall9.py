cities = {}
allPaths = []

def findAllPaths(cities, currLoc, path, dist):
	
	path.append(currLoc)
	#add the distance to the new link we made
	if len(path) > 1:
		dist+= cities[currLoc][path[-2]]
	#make sure we can complete the last loop of our path
	if (len(path) == len(cities)) and cities[path[0]].has_key(path[-1]):
		global allPaths
		allPaths.append((path, dist))
		return

	#fork off
	for city in cities:
		if (city not in path) and cities[city].has_key(currLoc):
			findAllPaths(dict(cities), city, list(path), dist)



with open('input') as fp:
	for line in fp.readlines():
		toParse = line.split()
		if toParse[0] in cities:
			cities[toParse[0]].update({toParse[2]:int(toParse[4])})
		else:
			cities[toParse[0]] = {toParse[2]:int(toParse[4])}
		if toParse[2] in cities:
			cities[toParse[2]].update({toParse[0]:int(toParse[4])})
		else:
			cities[toParse[2]] = {toParse[0]:int(toParse[4])}

for key in cities.keys():
	findAllPaths(cities, key, [], 0)
#print allPaths
print min(allPaths, key = lambda x:x[1])
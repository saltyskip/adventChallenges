table = {}
allPaths = []

def findAllPaths(cities, currLoc, path, dist):
	
	path.append(currLoc)
	#add the distance to the new link we made
	if len(path) > 1:
		dist+= table[currLoc][path[-2]]
	#make sure we can complete the last loop of our path
	if (len(path) == len(table)) and table[path[0]].has_key(path[-1]):
		global allPaths
		dist += table[path[-1]][path[0]]
		allPaths.append((path, dist))
		return

	#fork off
	for person in table:
		if (person not in path) and table[person].has_key(currLoc):
			findAllPaths(dict(table), person, list(path), dist)




with open('input2') as fp:
	for line in fp.readlines():
		toParse = line.split()
		person1 = toParse[0]
		person2 = toParse[-1][0:-1]
		happiness = int(toParse[3]) if toParse[2] == 'gain' else -int(toParse[3])
		if person1 not in table: 
			table[person1] = {person2: happiness}
		elif person2 in table[person1]:
			table[person1][person2] += happiness
		else:
			table[person1].update({person2:happiness})

		if person2 not in table: 
			table[person2] = {person1: happiness}
		elif person1 in table[person2]:
			table[person2][person1] += happiness
		else:
			table[person2].update({person1:happiness})			
print table

for key in table.keys():
	findAllPaths(table, key, [], 0)
#print allPaths
print max(allPaths, key = lambda x:x[1])


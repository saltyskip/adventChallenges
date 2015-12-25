from sets import Set

def read(f):
    return [x.strip().split() for x in open(f, 'r')]

def findMappings(mol, mappings):
	newMols = Set()
	print mol
	for mapping in mappings:
		for x in range(0, len(mol)):
			print 'comparing: ' + mol[x:x+len(mapping[0])] + ' to ' + mapping[0]
			if mol[x:x+len(mapping[0])] == mapping[0]:
				newMols.add(mol[:x] + mapping[1] + mol[x+len(mapping[0]):])
	return newMols

lines = read('input')
mappings = []
for i in lines[:-2]:
    mappings.append((i[0], i[-1]))
mol = lines[-1][0]
newMols = findMappings(mol, mappings)
print len(newMols)
my_sue ={'children':3, 'cats':7, 'samoyeds':2,'pomeranians':3,'akitas':0,
		'vizslas':0, 'goldfish':5, 'trees':3, 'cars':2, 'perfumes':1 }
def part1():
	with open('input') as fp:
		for line in fp.readlines():
			toParse = line.split()
			attr1 = (toParse[2][0:-1], int(toParse[3][0:-1]))
			attr2 = (toParse[4][0:-1], int(toParse[5][0:-1]))
			attr3 = (toParse[6][0:-1], int(toParse[7]))
			if (my_sue[attr1[0]] == attr1[1] and my_sue[attr2[0]] == attr2[1] 
					and my_sue[attr3[0]] == attr3[1]):
				print line
				break
def part2():
	with open('input') as fp:
		for line in fp.readlines():
			toParse = line.split()
			attrs = []
			attrs.append((toParse[2][0:-1], int(toParse[3][0:-1])))
			attrs.append((toParse[4][0:-1], int(toParse[5][0:-1])))
			attrs.append((toParse[6][0:-1], int(toParse[7])))
			isValid = True
			for attr in attrs:
				if attr[0] == 'cats' or attr[0] == 'trees':
					if my_sue[attr[0]] >= attr[1]:
						isValid = False
				elif attr[0] == 'pomeranians' or attr[0] == 'goldfish':
					if my_sue[attr[0]] <= attr[1]:
						isValid = False
				else:
					if my_sue[attr[0]] != attr[1]:
						isValid = False
			if isValid: 
				print line
				break
part2()
blackSet =  ['ab', 'cd', 'pq', 'xy']
the_vowel = ["a","e","i","o","u"]
def naughtyStringCount(strings):
	numNice = 0
	for string in strings:
		vowels = 0
		consec = False
		blackSub = False
		for x in range(len(string)):
			if string[x] in the_vowel:
				vowels += 1
			if (x != len(string)-1) and (string[x] == string[x+1]):
				consec = True
			if (x != len(string)-1) and (string[x]+string[x+1] in blackSet):
				blackSub = True
		if vowels >=3 and consec and not blackSub:
			numNice+=1
	return numNice

def naughtyStringCount2(strings):
	numNice = 0
	string = strings[0]
	for string in strings:
		sandwich = False
		bigramPair = False
		for x in range(len(string)-2):
			if string[x] == string[x+2]:
				sandwich = True
				break
		for x in range(len(string)-1):
			bigram = string[x:x+2]
			for y in range(x+2, len(string)-1):
				if	bigram == string[y:y+2]:
					bigramPair = True
					break
		if sandwich and bigramPair: numNice+=1
	return numNice


strings = []
with open('input') as fp:
	for line in fp:
	  	strings.append(line.rstrip('\n'))

print naughtyStringCount2(strings)
	
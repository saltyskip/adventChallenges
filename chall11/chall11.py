from itertools import groupby

SECRET_CODE = 'cqjxjnds'
SECRET_CODE2 = 'cqjxxyzz'

def checkPass(passw):
	if 'i' in passw or 'o' in passw or 'l' in passw:
		return False
	hasConsec = False
	for x in range(len(passw) - 2):
		firstCharVal = ord(passw[x])
		if ord(passw[x+1]) == firstCharVal  + 1 and ord(passw[x+2]) == firstCharVal + 2:
			hasConsec = True
			break
	sequences = [[k,len(list(g))] for k, g in groupby(passw)]
	numPairs = 0
	for seq in sequences:
		if seq[1] > 1: numPairs+=1
	if numPairs > 1 and hasConsec: return True
	return False

def incrementPass(passw):
	mustCarry = False
	passWordValid = False
	letterToInc = -1
	while not passWordValid:
		if passw[letterToInc] == 'z':
			passw[letterToInc] = 'a'
			letterToInc -= 1
		else:
			passw[letterToInc] = chr(ord(passw[letterToInc])+1)
			letterToInc = -1
			if checkPass(passw): return passw
	

print str(incrementPass(list(SECRET_CODE2)))

calc = dict()
results = dict()
with open('input') as fp:
	for line in fp:
		(ops, res) = line.split('->')
		calc[res.strip()] = ops.strip().split(' ')

def evaluate(wire):
	#no need to recur, already have value
	try: return int(wire)
	except ValueError:pass

	if wire not in results:
		if len(calc[wire]) == 1: #inserting number straight into wire
			result =  evaluate(calc[wire][0])
		else:
			if calc[wire][1] == 'AND':
				result =  evaluate(calc[wire][0]) & evaluate(calc[wire][2]) 
			elif calc[wire][1] == 'OR':
				result =  evaluate(calc[wire][0]) | evaluate(calc[wire][2])
			elif calc[wire][1] == 'LSHIFT':
				result =  evaluate(calc[wire][0]) << evaluate(calc[wire][2])
			elif calc[wire][1] == 'RSHIFT':
				result =  evaluate(calc[wire][0]) >> evaluate(calc[wire][2])
			else:
				result = ~evaluate(calc[wire][1]) & 0xffff
		results[wire] = result
	return results[wire]	

print evaluate('a')
import json
def countNum(obj):
	if type(obj) == int:
		return obj
	if type(obj) == list:
		return sum([countNum(x) for x in obj])
	if type(obj) == dict:
		#return sum([countNum(obj[key]) for key in obj.keys()])
		if 'red' in obj.values(): return 0
		return sum([countNum(obj[key]) for key in obj.keys()])

	return 0 
data = json.loads(open('input', 'r').read())
print countNum(data)

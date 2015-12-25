instructions = []
with open('input') as fp:
	for line in fp.readlines():
		instructions.append(line.strip().split())
a,b = 1,0
def assembly(instructions,a,b):
	instructNum = 0
	while instructNum < len(instructions):
		if instructions[instructNum][0] == 'inc':
			exec(instructions[instructNum][1] + '+=1')
			instructNum += 1
		elif instructions[instructNum][0] == 'tpl':
			exec(instructions[instructNum][1] + '*=3')
			instructNum += 1	
		elif instructions[instructNum][0] == 'hlf':
			exec(instructions[instructNum][1] + '/=2')
			instructNum += 1
		elif instructions[instructNum][0] == 'jmp':
			instructNum += int(instructions[instructNum][1])
		elif instructions[instructNum][0] == 'jie':
			if eval(instructions[instructNum][1].strip(',')) % 2 == 0:
				instructNum += int(instructions[instructNum][2])
			else:
				instructNum += 1
		elif instructions[instructNum][0] == 'jio':
			if eval((instructions[instructNum][1]).strip(',')) == 1:
				instructNum += int(instructions[instructNum][2])
			else:
				instructNum += 1
	print a,b
assembly(instructions, a, b)
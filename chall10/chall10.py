import re

INPUT = '1113222113'
NUM_ROUNDS = 50

curr_string = INPUT
for x in range(NUM_ROUNDS):
	new_string = ''
	groups = [m.group(0) for m in re.finditer(r"(\d)\1*", curr_string)]
	for group in groups:
		new_string += str(len(group)) + group[0]
	curr_string = new_string
print len(curr_string)
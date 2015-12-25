input = 29000000
import math

def factors(n):
    factors = set()
    for x in range(1, int(math.sqrt(n)) + 1):
    	if n % x == 0:
          	factors.add(x)
        	factors.add(n//x)
    return factors

def factors2(n):
    factors = set()
    for x in range(1, int(math.sqrt(n)) + 1):
    	if n % x == 0:
          	if x * 50 >= n:
          		factors.add(x)
        	if (n//x) * 50 >= n:
        		factors.add(n//x)
    return factors 

def calc_presents(factors):
	sum = 0
	for f in factors:
		sum += f
	return sum

house = 1
total_presents = 0
curr_max = 0
while  total_presents < input/11:
	house += 1
	fac = factors2(house)
	total_presents = calc_presents(fac)
	curr_max = max(total_presents, curr_max)
	if curr_max == total_presents: print curr_max
print house


F = [4,-2,0,0,5]
C = [0,5,-1,0,8]
B = [-1,0,5,0,6]
S = [0,0,-2,2,1]
highScore = 0
total_score = 0
for f in range(100):
	for c in range(100-f):
		for b in range(100-f-c):
			capacity = f*F[0] + c*C[0] + b*B[0] + (100-f-c-b)*S[0]
			durability = f*F[1] + c*C[1] + b*B[1] + (100-f-c-b)*S[1]
			flavor = f*F[2] + c*C[2] + b*B[2] + (100-f-c-b)*S[2]
			texture =  f*F[3] + c*C[3] + b*B[3] + (100-f-c-b)*S[3]
			calories = f*F[4] + c*C[4] + b*B[4] + (100-f-c-b)*S[4]
			if capacity <= 0 or durability <= 0 or flavor <=0 or texture <= 0 or calories != 500:
				total_score = 0
			else: total_score = capacity * durability * flavor * texture
			if total_score > highScore:
				highScore = total_score
print highScore
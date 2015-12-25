import hashlib
import hashlib
SECRET_KEY = 'yzbqklnj'

number = 1
while True:
	code = hashlib.md5(SECRET_KEY + str(number)).hexdigest()
	if code[0:6] == '000000':
		print code
		print number
		break
	number+=1
def xo(s):

	countO = 0
	countX = 0

	for letra in s:
		if letra == "o" or letra == "O":
			countO += 1
		elif letra == 'x' or letra == 'X':
			countX += 1
		else: 
			countX += 0 
			countO += 0

	if countO == countX:
		print True
	elif countO != countX:
		print False
	else:
		print True

	return xo()



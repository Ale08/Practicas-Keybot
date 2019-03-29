

def summy(string_of_ints):	

	sum_of_ints = 0
	lista = string_of_ints.split() 

	for elemento in lista:
		numero = int(elemento)
		sum_of_ints = int(elemento) + sum_of_ints

	return sum_of_ints


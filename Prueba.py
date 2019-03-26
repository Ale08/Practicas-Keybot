lista = ["Xime", "Nube","Abi", "Emi", "Isma"]
lista_buena = []
def FRIENDS(x):
	for nombre in lista:
		if len(nombre) == 4:
			lista_buena.append(nombre)

	return lista_buena

print FRIENDS(lista)

def friend(x):
    lista = []
    for nombre in x:
        if len(nombre) == 4:
            lista.append(nombre)
    return lista


entrada = int (raw_input('Cuantas iteracciones deseas utilizar:  ')) 
valor = raw_input('Ingresa el valor a incrementar:  ')
while entrada > 0:
	entrada = entrada -1
	valor = str(int(valor)+int(valor[0]) + int(valor[len(valor)-1]))
	print valor


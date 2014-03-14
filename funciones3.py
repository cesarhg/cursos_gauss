def nombre_funcion(variable1, variable2):
	resultado = int(variable1) + int(variable2)
	return resultado
print('Ingresa los valores a sumar')
valor1 = raw_input('>>>')
valor2 = raw_input('>>>')

variable = nombre_funcion(valor1,valor2)

print variable

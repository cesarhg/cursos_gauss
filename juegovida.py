import random #importamos la funcion random 
rango = 20


def llenado_matriz(): #creacion funcion matriz para llenado de puntos
	if random.randrange(3) == 2:
		return'0'
	else:
		return' '
def vecinos(x,y,matrix):
	contador = 0
	if matrix[y-1][x-1] == '0':
		contador += 1



matrix = [[llenado_matriz() for x in xrange(rango)] for x in xrange(rango)]
for fila in matrix:
	for blanco in fila:

		print blanco, #Imprime espacio en blanco y la coma da salto de linea
	print #Imprime linea por linea
contador_filas = 1
while contador_filas < rango:
	contador_columnas = 1
	while contador_columnas = 1
		print vecinos(contador_columnas,contador_filas,matrix)
		contador_columnas += 1
	print
	contador_filas += 1

	

	


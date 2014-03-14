
matrix=[1,1] #Declaracion de matriz
iteracion=int(raw_input('Ingresa el numero de iteraciones'))#Ingresar datos

while iteracion > 0: #Mientras iteracion sea menor que cero se ejecuta el proceso 

	iteracion = iteracion - 1 # Se hara un decremento de 1 en 1

	indice = len(matrix) #Se cuentan el numero de elementos del arreglo matrix

	while indice > 1: #Si el indice es menor que 1 se ejecuta el proceso

 		indice = indice - 1 #Se realiza un decremento en el indice
 		matrix[indice] = matrix[indice] + matrix[indice -1]# Se acumula la matrix
 	matrix.append(1) #Inserta el primer elemento de la matrix

 	print matrix #impresion de matrix




variable = 0

while True:
	
	operacion = raw_input('Que operacion desea hacer (s)uma, (r)esta, (m)ultiplicacion, (d)ivision, sa(l)ir  ')

	if operacion == 'l':
		break
	
	entrada = raw_input('Ingresa un valor:  ')

	if operacion == 's':
		variable = variable + int(entrada)
		print variable
	elif operacion == 'r':
		variable = variable - int(entrada)
		print variable
	elif operacion == 'm':
		variable = variable * int(entrada)
		print variable
	elif operacion == 'd':
		variable = variable / int(entrada)
		print variable		    
		
		#operacion = raw_input('Que operacion deseas hacer')
		#operacion= raw_input('Que deseas hacer')
		#if operacion == '+':
		#variable = variable + int(entrada)
	 	#print variable


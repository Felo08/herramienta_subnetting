

################# CONVERTIDOR ########################
def convertidor(num_convertir, tipo):
	separador = "."
	numero_convertido = ""
	tup_num_conv =[]  # lista donde se almacenaran los octetos ya convertidos
	num_array = []

	num_array = num_convertir.split(".")

	for octeto in num_array:

		if tipo == "d":
			suma = 0
			exponente = 0
			for pos_bit in range(-1,(-1* (octeto.length + 1)),-1):
				suma += int(octeto[pos_bit]) * (2**exponente)
				exponente += 1
				
			tup_num_conv.append(str(suma))

#-////////////////////////////////////////////////////////////

		elif tipo == "b":
			numero = int(octeto)
			residuo = 0
			contador = 0
			convertido = ""
			binario = ""

			while numero > 1:
				residuo, numero = numero%2, numero//2
				convertido += str(residuo)
				contador += 1

			convertido += str(numero)
			contador += 1
	
			if contador < 8:
				faltante = 8-contador
				binario = "0"*faltante

			for i in range(-1,(-1 * (contador+1)),-1):
				binario += convertido[i]
                        
			

			tup_num_conv.append(binario)


		numero_convertido = separador.join(tup_num_conv)

	return numero_convertido


################# HALLAR EXPONENTE ########################
def exponente(hosts_solicitados):
	for exp in range(0, 9):
		potenciado = 2**exp
		diferencia = potenciado - int(hosts_solicitados)
		if diferencia >= 2:
			return exp
			break


################# NUEVA MASCARA ########################
def nueva_mascara_subnormal(hosts_solicitados, mascara_binaria): # Funcion para calcular la nueva mascara del subnetting normal
	mascara_vieja_array = mascara_binaria.split(".")

	bits_encender = exponente(hosts_solicitados)
	cambio = False
	mascara_nueva = mascara_vieja_array[0]
	
	for octeto in mascara_vieja_array:
		if octeto == "00000000" and cambio == False:
			encendido = 0
			while encendido < bits_encender:
				octeto[encendido] = "1"
				encendido += 1

			cambio = True
		mascara_nueva += "." + octeto
	
	return mascara_nueva

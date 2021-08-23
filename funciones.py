
import ipaddress
from tabulate import tabulate

####################### CONVERTIDOR ##############################
# Convierte las direcciones IPv4 de decimal a binario y viceversa
# tiene como parametros la dirección IPv4 (en binario o decimal) 
# y el formato al que sera convertido ("d" de binario a decimal y "b" de decimal a binario)  
# Devuelve la IPv4 en forma de lista (vector), con los octetos separados. ej: 255.255.255.0 => ["11...","11...","11...","00..."]

def convertidor(num_convertir, tipo): 

	array_num_conv =[]  # lista donde se almacenaran los octetos ya convertidos

	for octeto in num_convertir:

		if tipo == "d":
			suma = 0
			exponente = 0
			for pos_bit in range(-1,-9,-1):
				suma += int(octeto[pos_bit]) * (2**exponente)
				exponente += 1
				
			array_num_conv.append(str(suma))

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
                        
			

			array_num_conv.append(binario)


		

	return array_num_conv


################# HALLAR EXPONENTE ########################
def exponente(hosts_solicitados):
	for exp in range(0, 9):
		potenciado = 2**exp
		diferencia = potenciado - int(hosts_solicitados)
		if diferencia >= 2:
			return exp
			break


################# NUEVA MASCARA ########################
# Funcion para calcular la nueva mascara del subnetting normal
# Como parametros recive la cantidad de host solicitados y la mascara de red
# retorna la nueva mascara en forma de lista, con los octetos separados.ej: 255.255.255.128 => ["11...","11...","11...","10..."]
def nueva_mascara_subnormal(hosts_solicitados, mascara_binaria): 
	
	bits_encender = exponente(hosts_solicitados)
	cambio = False
	mascara_nueva = []
	mascara_nueva.append(mascara_binaria[0])
	
	for octeto in mascara_binaria:
		if octeto == "00000000" and cambio == False:
			encendido = 0
			nuevo_octeto = "1"*bits_encender
			nuevo_octeto += "0"* (8 - bits_encender)

			octeto = nuevo_octeto
			cambio = True
		mascara_nueva.append(octeto)
	
	return mascara_nueva


################# SALTO DE RED ########################
def salto_red(mascara_nueva_decimal):
	constante = 256
	salto = 1
	for octeto in mascara_nueva_decimal:
		if octeto != "255":
			salto = 256 - int(octeto)
			break
	
	return salto


def informacion(salto_red, hosts_solicitados, ip_ingresada):
	subredes = ["Subredes"]
	primera_ip = ["primera ip utilizable"]
	ultima_ip = ["ultima ip utilizable"]
	broadcast = ["Broadcast"]

	ip_red = ipaddress.IPv4Address(".".join(ip_ingresada))
	
	for i in range(1,(int(hosts_solicitados) + 1)):
		subredes.append(format(ip_red))
		primera_ip.append(format(ip_red + 1))
		ultima_ip.append(format(ip_red + (salto_red - 2)))
		broadcast.append(format(ip_red + (salto_red - 1)))

		ip_red += salto_red

	
	tabla = []
	tabla.append(["#", subredes[0], primera_ip[0], ultima_ip[0], broadcast[0]])

	for j in range(1, (int(hosts_solicitados) + 1) ):
		tabla.append([str(j), subredes[j], primera_ip[j], ultima_ip[j], broadcast[j]])
	
	print(tabulate(tabla, headers='firstrow'))
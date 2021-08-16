# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 22:41:54 2021

@author: felipe
"""
import funciones

def main():

    print("digite el numero y tipo a convertir separados por un ESPACIO('d' para cambiar de binario a decimal o 'b' para cambiar de decimal a binario)")
    entrada = input("->")
 
    datos_entrada = entrada.split(" ")
 
    numero = datos_entrada[0]
    tipo = datos_entrada[1]
 
    conversion = funciones.convertidor(numero, tipo)
 
    print(conversion)
#=============================================================================
# =============================================================================
# 	hosts = input("cantidad de hosts solicitados: ")
# 	print(funciones.exponente(hosts))
# =============================================================================


main()

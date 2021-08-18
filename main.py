# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 22:41:54 2021

@author: felipe
"""
import funciones

def main():


    ip = input("Dijite la ip de red: ")
    prefijo = input("Dijite el prefijo de red: ")
    hosts_solicitados = input("Dijite la cantidad de host solicitados: ")

    ip_array = ip.split(".")

    mascara = ""

    if prefijo == "8":
        mascara = "255.0.0.0"

    elif prefijo == "16":
        mascara = "255.255.0.0"

    elif prefijo == "24":
        mascara = "255.255.255.0"

    array_mascara = mascara.split(".")
 
    mascara_binaria = funciones.convertidor(array_mascara, "b")

    mascara_nueva = funciones.nueva_mascara_subnormal(hosts_solicitados, mascara_binaria)

    mascara_nueva_decimal = funciones.convertidor(mascara_nueva, "d")

    salto_de_red = funciones.salto_red(mascara_nueva_decimal)

    funciones.informacion(salto_de_red, hosts_solicitados, ip_array)


main()

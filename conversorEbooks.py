#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Script para convertir libros electrónicos a otro formato.
# Calibre debe estar instalado.

import os

def menu():
    os.system("clear")
    print("\n--- MENÚ ---\n1) Listar el contenido de la carpeta.\n2) Sustituir espacios en blanco por guiones bajos.\n3) Convertir ebook a otro formato.\n4) Salir.")

def listar():
	os.system("ls -l")
	input("\nPulsa intro para continuar...")

def renombrar():
    files = os.listdir()  # listamos el contenido del directorio

    for file in files:
        # sustituimos los posibles espacios en blanco por guiones bajos y
        # renombramos el archivo
        os.rename(file, "_".join(file.split()))

def convertir(origen, destino):
    files = os.listdir()

    for file in files:
        if os.path.isfile(file):  # si es un archivo
            if file.endswith(origen) == True:  # si la extension es 'origen'
                print(file + " se convertirá a " + destino)

                # usamos calibre para convertir a otro formato
                os.system("ebook-convert {0} {0}.{1}".format(file, destino))

def corregir(origen, destino):
    files = os.listdir()

    for file in files:
        if os.path.isfile(file):
            if file.endswith(destino) == True:
                # eliminamos la extensión antigua del nombre final
                os.rename(file, file.replace(".{0}.".format(origen), "."))

while True:
    menu()
    opcion = input("\nElige una opción: ")

    if opcion == "1":
    	listar()
    elif opcion == "2":
        renombrar()
    elif opcion == "3":
        origen = input("Formato de origen: ")
        destino = input("Formato de destino: ")
        convertir(origen, destino)
        corregir(origen, destino)
    elif opcion == "4":
        print("Aguuur")
        break
    else:
        print("Opción no válida")

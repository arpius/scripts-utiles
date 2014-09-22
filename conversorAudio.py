#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Script para convertir pistas de audio de un formato a otro.
# Los archivos de audio deben estar en el mismo directorio.
# Este script está escrito en python 3.

import os

def menu():
	os.system("clear")
	print("\n--- MENÚ ---\n1) Sustituir espacios en blanco por guiones bajos.\n2) Convertir de un formato de audio a otro.\n3) Salir.")

def renombrar():
	files = os.listdir() #listamos el contenido del directorio

	for file in files:
		os.rename(file, "_".join(file.split())) #sustituimos los posibles espacios en blanco por guiones bajos y renombramos el archivo

def convertir(origen, destino):
	files = os.listdir()

	for file in files:
		if os.path.isfile(file): #si es un archivo
			if file.endswith(origen) == True: #si la extension es 'origen'
				print(file+ " se convertirá a " +destino)
					
				os.system("ffmpeg -i {0} {0}.{1}".format(file, destino)) #usamos ffmpeg para convertir entre formatos de audio

def corregir(origen, destino):
	files = os.listdir()

	for file in files:
		if os.path.isfile(file):
			if file.endswith(destino) == True:
				os.rename(file, file.replace(".{0}.".format(origen), ".")) #eliminamos la extensión antigua del nombre final

while True:
	menu()
	opcion = input("\nElige una opción: ")
	
	if opcion == "1":
		renombrar()
	elif opcion == "2":
		origen = input("Formato de origen: ")
		destino = input("Formato de destino: ")
		convertir(origen, destino)
		corregir(origen, destino)
	elif opcion == "3":
		print("Aguuur")
		break
	else:
		print("Opción no válida")
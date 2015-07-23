#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:59:08 2015

@author: aritz
"""
# Script para transferir archivos entre 2 equipos mediante el comando scp.

import os


def menu():
    os.system('clear')

    titulo = 'scp interactivo'
    op1 = '1) Copiar archivo remoto a local.'
    op2 = '2) Copiar carpeta remota a local.'
    op3 = '3) Copiar archivo local a remoto.'
    op4 = '4) Copiar carpeta local a remoto.'
    salir = '5) Salir'

    menu = '{:-^34}\n {}\n {}\n {}\n {}\n {}'.format(titulo, op1, op2, op3,
                                                     op4, salir)
    print(menu)


def pedir_datos():
    usuario = input('Nombre de usuario: ')
    host = input('Host remoto: ')
    archivo = input('Nombre de archivo: ')
    destino = input('Ruta de destino: ')

    return usuario, host, archivo, destino


def ejecutar_scp(opcion):
    datos = {}
    datos = pedir_datos()

    if opcion == '1':
        # archivo remoto a local
        scp = 'scp -P 777 {}@{}:{} {}'.format(datos[0], datos[1], datos[2],
                                              datos[3])
    elif opcion == '2':
        # carpeta remota a local
        carpeta = input('Ruta a la carpeta remota: ')
        scp = 'scp -P 777 {}@{}:{} {}/{}'.format(datos[0], datos[1], carpeta,
                                                 datos[3], datos[2])
    elif opcion == '3':
        # archivo local a remoto
        scp = 'scp -P 777 {} {}@{}:{}'.format(datos[2], datos[0], datos[1],
                                              datos[3])
    elif opcion == '4':
        # carpeta local a remoto
        scp = 'scp -P 777 -r {} {}@{}:{}'.format(datos[2], datos[0], datos[1],
                                                 datos[3])

    print('Ejecutando {}... '.format(scp))
    os.system(scp)

while True:
    menu()
    opcion = input('\nElige una opción: ')

    if opcion == '1':
        ejecutar_scp(opcion)
    elif opcion == '2':
        ejecutar_scp(opcion)
    elif opcion == '3':
        ejecutar_scp(opcion)
    elif opcion == '4':
        ejecutar_scp(opcion)
    elif opcion == '5':
        print('Hasta otra o/')
        break

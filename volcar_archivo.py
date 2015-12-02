#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, origen, destino = argv

print("Copiando de {} a {}.".format(origen, destino))

archivo_orig = open(origen).read()

print("El archivo tiene un tamaño de {} bytes".format(len(archivo_orig)))

if exists(destino):
    print("El archivo de destino [ {} ] ya existe. ¿Desea reemplazarlo?".format_map(destino))
    print("Pulsa ENTER para continuar o CONTROL+C para cancelar...")
    input()

archivo_dest = open(destino, 'w').write(archivo_orig)

print("Proceso de volcado: OK")

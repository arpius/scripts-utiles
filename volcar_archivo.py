#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, origen, destino = argv

print "Copiando de %s a %s." % (origen, destino)

archivo_orig = open(origen).read()

print "El archivo tiene un tamaño de %d bytes" % len(archivo_orig)

if exists(destino):
	print "El archivo de destino [ %r ] ya existe. ¿Desea reemplazarlo?" % destino
	print "Pulsa ENTER para continuar o CONTROL+C para cancelar..."
	raw_input()

archivo_dest = open(destino, 'w').write(archivo_orig)

print "Proceso de volcado: OK"

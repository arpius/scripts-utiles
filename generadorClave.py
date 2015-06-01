#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 13:14:49 2014

@author: aritz
"""
# Script que genera una clave aleatoria que contiene letras mayúsculas,
# minúsculas, números y signos.
# Por defecto la longitud de la clave es de 12 caracteres.

from random import choice
import string


def generadorClave(longitud=12):
    caracteres = string.letters + string.digits + string.punctuation
    clave = ''.join(choice(caracteres) for i in xrange(longitud))
    return clave

print "Clave generada: " + generadorClave()

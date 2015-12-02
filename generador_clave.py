#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script que genera una clave aleatoria que contiene letras mayúsculas,
# minúsculas, números y signos.
# Por defecto la longitud de la clave es de 8 caracteres.

from random import choice
import string


def generadorClave(longitud=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    clave = ''.join(choice(caracteres) for i in range(longitud))
    return clave

print("Clave generada: {}".format(generadorClave(16)))

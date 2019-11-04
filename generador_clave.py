#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script que genera una clave aleatoria que contiene letras mayúsculas,
minúsculas, números y signos.
Por defecto la longitud de la clave es de 12 caracteres.
"""

from random import choice
import string
import click


@click.command()
@click.option('-l', '--longitud', default=12, help='Longitud de la clave.')
def generadorClave(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    clave = ''.join(choice(caracteres) for i in range(longitud))
    click.echo(clave)


if __name__ == "__main__":
    generadorClave()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Script para redimensionar imágenes para subirlas a la web o mandar por correo.
# Imagemagick debe estar instalado.
# mogrify -resize ANCHOxALTO [-quality CALIDAD] ruta_de_las_imagenes/*.EXTENSIÓN

import os

print("Introduce la ruta completa de la imágen que quieres redimensionar")
print("En caso de que quieras redimensionar todas las imágenes de un mismo tipo escribe: ruta_imagenes/*.extensión")
print("¡OJOCUIDAO este script SOBRESCRIBE la imagen original!")

ruta_img = input("Ruta de la imágen: ")

os.system("mogrify -resize 1024x768 -quality 94% {0}".format(ruta_img))

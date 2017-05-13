#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script para enviar correo por consola.
"""
import smtplib
import yaml
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


with open('config/config.yml', 'r') as config:
    try:
        configuracion = yaml.load(config)
    except yaml.YAMLError as error:
        print(error)


# Parámetros de configuración para el mensaje de correo
EMISOR = configuracion['correo']['emisor']
RECEPTOR = configuracion['correo']['receptor']
ASUNTO = configuracion['correo']['asunto']
MENSAJE = configuracion['correo']['mensaje']
ADJUNTO = configuracion['correo']['adjunto']

# Parámetros de configuración del servidor de correo
SMTP = configuracion['servidor']['saliente']
PUERTO = configuracion['servidor']['puerto']
CLAVE = configuracion['servidor']['clave']


correo = MIMEMultipart()
correo['From'] = EMISOR
correo['To'] = ','.join(RECEPTOR)
correo['Subject'] = ASUNTO
correo.attach(MIMEText(MENSAJE, 'plain'))


for adj in ADJUNTO:
    archivo = open(adj, "rb")

    adjunto = MIMEBase('application', 'octet-stream')
    adjunto.set_payload(archivo.read())
    encoders.encode_base64(adjunto)
    adjunto.add_header('Content-Disposition', "attachment; filename={}".format(
                        adj))

    correo.attach(adjunto)


servidor = smtplib.SMTP(SMTP, PUERTO)
servidor.starttls()
servidor.login(EMISOR, CLAVE)

texto = correo.as_string()

servidor.sendmail(EMISOR, RECEPTOR, texto)
servidor.quit()

print('{:-^42}'.format(' Correo electrónico '))
print('[Enviado por] {}'.format(EMISOR))
print('[Recibido por] {}'.format(RECEPTOR))
print('[Fecha] {:%Y-%m-%d %H:%M}'.format(datetime.now()))
print('[Adjuntos] {}'.format(ADJUNTO))

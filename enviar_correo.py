#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script para enviar correo por consola.
"""
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


desde = "tu correo"
hacia = "correo del destinatario"
correo = MIMEMultipart()
correo['From'] = desde
correo['To'] = hacia
correo['Subject'] = "asunto"

mensaje = "cuerpo del mensaje"
correo.attach(MIMEText(mensaje, 'plain'))

archivo = "nombre del archivo adjunto"
ruta = open("ruta del archivo adjunto/{}".format(archivo), "rb")

adjunto = MIMEBase('application', 'octet-stream')
adjunto.set_payload((ruta).read())
encoders.encode_base64(adjunto)
adjunto.add_header('Content-Disposition', "attachment; filename={}".format(
                archivo))

correo.attach(adjunto)

servidor = smtplib.SMTP('servidor de correo saliente', 587)
servidor.starttls()
servidor.login(desde, "contraseña")

texto = correo.as_string()

servidor.sendmail(desde, hacia, texto)
servidor.quit()

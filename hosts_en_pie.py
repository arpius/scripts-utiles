#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nmap

nm = nmap.PortScanner()
nodos = input('IP o rango de IPs a escanear: ')

while len(nodos) == 0:
    nodos = input('IP o rango de IPs a escanear: ')

nm.scan(hosts=nodos, arguments='-n -sP -PE -PA21,22,23,53,80,137,138,139,443,445,631,3389')
listado = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
archivo = open('escaneado.txt', 'w')

for nodo, estado in listado:
    print(nodo, estado)
    archivo.write(nodo+ '\n')

archivo.close()

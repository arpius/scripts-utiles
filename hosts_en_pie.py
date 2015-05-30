#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nmap

nm = nmap.PortScanner()
hosts = input('IP o rango de IPs a escanear: ')

while len(hosts) == 0:
    hosts = input('IP o rango de IPs a escanear: ')

nm.scan(hosts=hosts, arguments='-n -sP -PE -PA21,23,80,3389')
listado = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
archivo = open('escaneado.txt', 'w')

for host, estado in listado:
    print(host, estado)
    archivo.write(host+ '\n')

archivo.close()

#!/usr/bin/env bash
# Script para actualizar los repositorios de software
# y el firmware de la raspberry Pi

sudo aptitude update -y && \
sudo aptitude upgrade -y && \
sudo rpi-update
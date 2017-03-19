#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Adriano Freitas <https://adrianofreitas.me>
# Robson Marques <http://rbmarques.com.br>
#
import socket
HOST = '127.0.0.1'
PORT = 1337
print 'Trabalho para a disciplina Programação de Sistemas Distribuídos'
print 'Adriano Freitas <https://adrianofreitas.me>'
print 'Robson Marques  <http://rbmarques.com.br>'
print '\nPara sair use CTRL+X\n'

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
msg = raw_input()
while msg <> '\x18':
    tcp.send (msg)
    msg = raw_input()
tcp.close()

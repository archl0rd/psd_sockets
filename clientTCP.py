#!/usr/bin/python
#
# Adriano Freitas <https://adrianofreitas.me>
# Robson Marques <http://rbmarques.com.br>
#
import socket
HOST = '127.0.0.1'
PORT = 1337
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print '\n'
print 'Trabalho para a disciplina Programação de Sistemas Distribuídos'
print 'Para sair use CTRL+X\n'
msg = raw_input()
while msg <> '\x18':
    tcp.send (msg)
    msg = raw_input()
tcp.close()

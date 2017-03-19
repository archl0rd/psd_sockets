#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Adriano Freitas <https://adrianofreitas.me>
# Robson Marques <http://rbmarques.com.br>
#
import socket
HOST = ''
PORT = 1337

def menu():
    print '1 - Listar recursos existentes'
    print '2 - Status recurso'
    print '3 - Reservar recurso'
    print '4 - Liberar recurso'

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print 'Cliente conectado', cliente
    while True:
        msg = con.recv(1024)
        if not msg: break
        print cliente, msg
    print 'Finalizando conexao..', cliente
    con.close()

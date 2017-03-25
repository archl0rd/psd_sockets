#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Adriano Freitas <https://adrianofreitas.me>
# Robson Marques <http://rbmarques.com.br>
#
import socket
HOST = ''
PORT = 2048

menu = "\n1 - Listar recursos existentes\n2 - Status recurso\n3 - Reservar recurso\n4 - Liberar recurso"

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
        if msg == 'menu':
            #envia resposta para o cliente
            con.sendall(menu)

        print cliente, msg
    print 'Finalizando conexao..', cliente
    con.close()

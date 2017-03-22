#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Adriano Freitas <https://adrianofreitas.me>
# Robson Marques <http://rbmarques.com.br>
#
import socket
HOST = ''
PORT = 1337

menu = "\n1 - Listar salas existentes\n2 - Status sala\n3 - Reservar sala\n4 - Liberar sala"

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

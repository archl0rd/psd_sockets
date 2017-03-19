#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Adriano Freitas <https://adrianofreitas.me>
# Robson Marques <http://rbmarques.com.br>
#
import socket
import sys, getopt

def banner():
    print '#!/usr/bin/python'
    print '# Adriano Freitas <https://adrianofreitas.me>'
    print '# Robson Marques  <http://rbmarques.com.br>'
    print '\n'

def ajuda():
    print '-h\t--help\tExibir Ajuda'
    print '-m\t--menu\tExibir Menu'
    print '\n'

def solicitaRecurso(comando):
    HOST = '127.0.0.1'
    PORT = 1337
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)
    tcp.send (comando)

    reply = tcp.recv(131072)
    print "recvd: ", reply
    #msg = raw_input()
    #while msg <> '\x18':#enquanto a msg for diferente de CTRL+x
    #    tcp.send (msg)
    #    msg = raw_input()

    #encerra conexão
    tcp.close()



def main(argv):
    # exibe autores
    banner()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hm:v", ["help", "menu"])
    except getopt.GetoptError:
        print '\npython clientTCP.py --help\tPara exibir ajuda.'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-v':
            verbose = True
            sys.exit()
        elif opt in ("-h", "--help"):
            ajuda()
            sys.exit()
        elif opt in ("-m", "--menu"):
            solicitaRecurso("menu")
            sys.exit()


# chama a função principal
if __name__ == "__main__":
    main(sys.argv[1:])

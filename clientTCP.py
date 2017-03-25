
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
    PORT = 2048
    #cria socket tcp
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #info do servidor
    dest = (HOST, PORT)
    #cria conexao
    tcp.connect(dest)
    #envia oscomandos
    tcp.send (comando)

    # espera a resposta do servidor
    reply = tcp.recv(16384)
    print "Resposta Servidor:\n ", reply
    ### nao descomente...ainda
    #msg = raw_input()
    #while msg <> '\x18':#enquanto a msg for diferente de CTRL+x
    #    tcp.send (msg)
    #    msg = raw_input()


    #encerra conexao
    tcp.close()



def main(argv):
    # exibe autores
    banner()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hm:v", ["help", "menu"])
    except getopt.GetoptError:
        # erro padrao, caso a opcao seja invalida
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


# chama a funcao principal
if __name__ == "__main__":
    main(sys.argv[1:])

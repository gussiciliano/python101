'''
socket server
'''

import socket

BUFFER_SIZE = 1024

def escucharConexion():

    (clientsocket, address) = serversocket.accept() #Se cuelga acá hasta que alguien se conecte
    print('Se conecto...', address)

    with clientsocket: #Verifica que dicho cliente siga vivo, mientras escucha.
        while True:
            data = clientsocket.recv(BUFFER_SIZE)
            if data:
                clientsocket.send(data) #ECO DE MENSAJE RECIBIDO
                print(data.decode('UTF-8'))
            else:
                break

    print("se desconecto cliente", address)

if __name__ == '__main__':
    # crea un socket INET de tipo STREAM
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Esta máquina es", socket.gethostname())
    # asocia el socket a un host público
    # y a un puerto bien conocido (HTTP = 80)
    serversocket.bind((socket.gethostname(), 80))
    #Si hubiera usado s.bind(('', 80)) or s.bind(('localhost', 80)) or s.bind(('127.0.0.1', 80))
    #también tendría un socket servidor, pero solo sería accesible desde la misma máquina.
    # lo convierte en socket servidor TCP
    serversocket.listen(1)

    escucharConexion()

'''
socket server
'''
from threading import Thread
import socket


BUFFER_SIZE = 1024
connetctions = []

class ThreadSocketClient(Thread):

    def __init__(self, clientsocket, callback = None):
        super().__init__()
        self.__callback = callback
        self.__clientsocket = clientsocket

    def run(self):
        with self.__clientsocket:
            while True:
                msg = self.__clientsocket.recv(BUFFER_SIZE)
                if not msg:
                    break
                print("llego msg")
                self.__callback(self, msg)

    def getSocket(self):
        return self.__clientsocket

def broadcast_data(threadSocketClient, message):
    for threadSocketAux in connetctions:
        socket_aux = threadSocketAux.getSocket()
        #print("llego, for con", socket_aux)
        #print("clientsocket", clientsocket)
        if socket_aux != threadSocketClient.getSocket():
            try :
                socket_aux.send(message)
            except :
                socket_aux.close()
                connetctions.remove(threadSocketAux)

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
    serversocket.listen(2)

    while True:
        (clientsocket, address) = serversocket.accept()
        threadingSocketClient = ThreadSocketClient(clientsocket, broadcast_data)
        connetctions.append(threadingSocketClient)
        threadingSocketClient.start()

    print("maxima capacidad alcanzada.")

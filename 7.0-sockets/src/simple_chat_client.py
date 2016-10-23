'''
simple chat client Lucas Bais 04/10/2016
'''
import socket
from threading import Thread

def sendMessage(socket, message):
        socket.send(message.encode(encoding='utf_8'))


BUFFER_SIZE = 1024
# crea un socket INET de tipo STREAM

class ThreadSocketClient(Thread):

    def __init__(self, clientsocket, callback = None):
        super().__init__()
        self.__callback = callback
        self.__clientsocket = clientsocket

    def run(self):
        with self.__clientsocket:
            while True:
                msg = self.__clientsocket.recv(BUFFER_SIZE)
                print('<El otr@>' ,msg.decode('utf-8'))

    def getSocket(self):
        return self.__clientsocket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # ahora se conecta al servidor web en el puerto 80 (http)
    s.connect(("Lucas", 80))
    print("Escriba 'exit' para salir del chat:")
    listener = ThreadSocketClient(s)
    listener.start()

    while True:
        message = input()
        if message == 'exit':
            break
        sendMessage(s, message)
        print("\033[A                             \033[A")
        print('<Yo>', message)
    s.close()
    #data = s.recv(BUFFER_SIZE)

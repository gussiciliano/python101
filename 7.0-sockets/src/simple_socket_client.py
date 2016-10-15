'''
https://wiki.python.org/moin/HowTo/Sockets
'''
import socket

BUFFER_SIZE = 1024
# crea un socket INET de tipo STREAM
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # ahora se conecta al servidor web en el puerto 80 (http)
    s.connect(("Lucas", 80))
    s.send(b"Aguante la comic sans vieja!")
    data = s.recv(BUFFER_SIZE)
    print('Received', repr(data))
    s.close()

import socket, turtle
import time

UDP_IP = "0.0.0.0"
UDP_PORT = 5005

if __name__ == "__main__":

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        message = input()
        sock.sendto(message.encode("utf-8"), (UDP_IP, UDP_PORT))

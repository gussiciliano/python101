import socket, turtle
import time

UDP_IP = "0.0.0.0"
UDP_PORT = 5005

if __name__ == "__main__":
    turtle.setup(800, 600)
    jorge = turtle.Turtle()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        time.sleep(1)
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        dataString = data.decode("utf-8")
        print(dataString)
        if "derecha" in dataString:
            jorge.forward(10)
        elif "izquierda" in dataString:
            jorge.backward(10)

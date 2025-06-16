import random
import socket

MAX_BYTES = 1024

def udp_listen(address: tuple):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.bind(address)
        print("Listening : ", sock.getsockname())
    except:
        return False

def udp_client(host: tuple):
    pass
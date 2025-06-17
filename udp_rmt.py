import socket
from time import sleep

MAX_BYTES = 1024

def udp_listen(port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.bind(("", port))
        is_bind = True
    except:
        is_bind = False
        return False
    if is_bind:
        while is_bind:
            data, guest = sock.recvfrom(MAX_BYTES)
            print("Receive data: ", data.decode('utf-8'))
            sock.sendto("*ESP*".encode('ascii'), guest)
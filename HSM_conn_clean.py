import binascii
import functools
from locale import atoi
from functools import reduce
import struct

__author__ = 'jcakmak'

import socket
import sys

def tcp_conn():

    HOST = ''
    PORT = 1500

    message = ""

    binary = b""

    size = len(message) + len(binary)

    print (size)

    command = struct.pack("!h", size) + message.encode() + binary

    print (command)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    try:
        sock.send(command)
        sock.send(binary)
    except socket.error:
        print("Fail")

    data = sock.recv(1024)

    sock.close()
    print(str(data))

if __name__ == "__main__":
    tcp_conn()

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

    #MAC
    #message = ""


    #MAC
    #message = ""

    #Pin verification
    message = ""


"""
    binary = b""

    message = "" + "" + "" + "" + ""

    #message = ""

    size = len(message) + len(binary)

    #size = len(message)

    print (size)

    #command = struct.pack("!h", size) +  message.encode()

    command = struct.pack("!h", size) + message.encode() + binary

    #whole_command = command + binary

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

def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)

    return reduce(lambda x,y:x+y, lst)

#convert hex repr to string
def toStr(s):
    return s and chr(atoi(s[:2], base=16)) + toStr(s[2:]) or ''



if __name__ == "__main__":
    tcp_conn()
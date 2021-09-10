import socket
from sys import argv

def tcpsend(hostname, port, data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((hostname, int(port)))
        s.sendall(bytes(data, encoding='utf-8'))

tcpsend(argv[1], argv[2], argv[3])
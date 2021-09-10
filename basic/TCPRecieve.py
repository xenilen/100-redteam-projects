import socket
from sys import argv

def tcprecieve(hostname, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Opening socket on", hostname, port)
        s.bind((hostname, int(port)))
        s.listen()
        print("Success!")
        print("Waiting for connections...\n")
        connect, address = s.accept()
        with connect:
            print("[+] Connection :", str(address[0]) + ":" + str(address[1]))
            while True:
                data = connect.recv(512)
                if not data:
                    print("[-] Connection :", str(address[0]) + ":" + str(address[1]))
                    break
                print(str(data, encoding='utf-8'))
                # connect.sendall(data)

tcprecieve(argv[1], argv[2])
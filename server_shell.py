import socket

HOST = '127.0.0.1'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen()

client, address=server.accept()

while True:
    print(f"Bağlandı {address}")
    cmd_input = input("Komut gir: ")
    client.send(cmd_input.encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))
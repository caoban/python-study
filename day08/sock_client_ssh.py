import socket

Client = socket.socket()

Client.connect(('localhost',9999))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:continue
    Client.send(cmd.encode("utf-8"))
    cmd_res = Client.recv(1024)

    print(cmd_res)


Client.close()


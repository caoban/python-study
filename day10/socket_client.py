import socket

HOST = 'localhost' #远程的server端的地址
#端口是 数字
PORT = 9000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    msg = bytes(input(">>:"), encoding="utf8")
    s.sendall(msg)
    data = s.recv(1024)
    print("revc:", data)

s.close()




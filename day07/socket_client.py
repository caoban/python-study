#客户端
import socket

client = socket.socket() #声明socket类型，同时生成socket连接对象
client.connect(('localhost',6969))

client.send(b"Hello World!")
data = client.recv(1024)

print("recv:" ,data)
client.close()







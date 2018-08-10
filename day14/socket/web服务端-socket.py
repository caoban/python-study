#!/usr/bin/env python
# coding:utf-8
import socket

#本地启动一个socket 服务端，在浏览器中就能够访问到

def handle_request(client):
    buf = client.recv(1024)

    #python3 中传输的时候都是字节类型。
    # bytes()这种转换方式便于记忆。记得加上字符集
    client.send(bytes("HTTP/1.1 200 OK\r\n\r\n", encoding='utf-8'))
    #client.send(bytes("<h1 style='background-color:red;'>Hello, World<h1>", encoding='utf-8'))

    #改成从文件中读取数据，传到浏览器
    f = open('index.html', 'rb')
    data = f.read()
    f.close()
    client.send(data)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()


if __name__ == '__main__':
    main()












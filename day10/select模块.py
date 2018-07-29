import selectors
import socket

#创建一个select对象
sel = selectors.DefaultSelector()


def accept(sock, mask):

    #先建立连接
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)

    # 让select监听sock，新连接注册  read回调函数。read 里面是接收和发送数据。
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    data = conn.recv(1024)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


sock = socket.socket()
sock.bind(('localhost', 10000))
sock.listen(100)
sock.setblocking(False)


#  第一次是把 server 自己注册，select 监听server
#让select监听sock，只要来一个新连接就调用 accept函数
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    #有活动连接，说明有连接进来，就执行。
    events = sel.select() #默认阻塞，有活动连接就返回活动的连接列表
    for key, mask in events:
        callback = key.data #相当于调用accept
        callback(key.fileobj, mask)





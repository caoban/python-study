

import gevent

#要用协程自己的 socket  monkey是实现线程的
from gevent import socket,monkey

#加上这个才能知道有IO操作的时候就切换
monkey.patch_all()


#定义一个 socket的server端
def Server(port):
    s = socket.socket()
    s.bind(('0.0.0.0',port))

    #500 是指最大连接数
    s.listen(500)

    # 循环，启动协程，协程里面调用具体的方法。 类似真正socket中的handle方法
    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_request, cli)

#这个就相当于真正socket中的handle方法
def handle_request(conn):
    try:
        while True:
            data = conn.recv(1024)
            print("recv:", data)
            conn.send(data)
            if not data:
                break
    except Exception as ex:
        print("ex")
    finally:
        conn.close()

if __name__ == '__main__':
    Server(8001)


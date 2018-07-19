
from multiprocessing import Process,Pipe

#Pipe 是管道

def f(conn):
    conn.send([42, None, 'hello from child'])
    conn.send([42, None, 'hello from child2'])
    print(conn.recv())
    conn.close()

if __name__ == '__main__':
    #定义一个管道对象 管道有两头
    parent_conn, child_conn = Pipe()
    #定义一个进程对象 并启动
    p = Process(target=f,args=(child_conn,))
    p.start()
    # 这一头接收数据，另外发送接受。这头发送，另外一头接收
    print(parent_conn.recv())
    print(parent_conn.recv())
    parent_conn.send('sssss')
    #等待所有都执行完
    p.join()




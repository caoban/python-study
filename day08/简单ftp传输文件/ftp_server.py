__anthor__ = "suhan"

import socket,os,hashlib

#实例化
server = socket.socket()
#绑定端口并监听
server.bind(('0.0.0.0',9998))
server.listen()

#循环传输文件
while True:
    #这样可以多个client一起
    conn,addr = server.accept()
    print("new conn:",addr)
    #这个循环里面是真正的传输数据的操作
    while True:
        print("等待新指令")
        #1024是指一次接收的数据大小的限制
        data = conn.recv(1024)
        #判断client是否传空的，是空的话就break
        if not data:
            print("客户端已经端口")
            break

        print("data_____:",data)
        #data传过来的时候是byte类型，要decode成utf-8的string
        cmd,filename = data.decode().split()
        print("cmd____:",cmd)
        print("filename____:", filename)

        #os模块判断是否是文件
        if os.path.isfile(filename):
            f = open(filename,'rb')

            #实例化MD5对象后面比较MD5值
            m = hashlib.md5()
            #os 模块判断文件大小
            file_size = os.stat(filename).st_size
            #传文件大小。转成byte类型
            print("str(file_size).encode() ___:",str(file_size).encode() )
            conn.send = ( str(file_size).encode() )

            print("发送文件大小成功")
            #接收客户端响应，避免粘包
        #     conn.recv(1024)
        #
        #     for line in f:
        #         #对每行进行加密，因为文件大的话，不能等全部加载完再加密
        #         #分割的每行进行加密和连在一起加密是 MD5值是一样的
        #         m.update(line)
        #         #分行 传输文件
        #         conn.send(line)
        #     #打印MD5值
        #     print("file md5___:\n", m.hexdigest())
        #     f.close()
        #     #传输最后的整个文件的MD5值
        #     conn.send(m.hexdigest().encode())
        # print("send done")
server.close()






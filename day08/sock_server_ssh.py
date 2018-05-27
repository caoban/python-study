__author__ = 'suhan'
'''
date = 2018/05/24/20:56
'''
import socket ,os ,time

Server = socket.socket()
Server.bind(('localhost',9999))

Server.listen()

while True:
    conn, addr = Server.accept()
    print("new conn:",addr)
    while True:
        print("等待新指令")
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        print("执行指令" ,data)
        #接受字符串，输出的结果也是字符串
        cmd_res = os.popen(data.decode()).read() #接受字符串，执行结果也是字符串
        print("before send", len(cmd_res.encode()))
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output...."


        # 这个是为了发送，指令输出的结果的大小给client。先传文件大小，再传文件数据
        # 整数是不能直接encode的，先转出str，再encode。
        conn.send( str(len(cmd_res.encode())).encode("utf-8") )
        client_ack = conn.recv(1024) #等待客户端响应，这样上一条就会全部发送完成，不会粘包
        conn.send(cmd_res.encode("utf-8"))
        print("send done")
        # os.path.isfile()
        # os.stat("sock")

Server.close()



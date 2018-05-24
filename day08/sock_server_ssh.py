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
        cmd_res = os.popen(data.decode()).read()
        # print("before send", len(cmd_res))
        # if len(cmd_res) == 0:
        #     cmd_res = "cmd has no output...."
        # conn.send( str(len(cmd_res.encode())).encode("utf-8") )
        # time.sleep(0.5)
        conn.send(cmd_res.encode("utf-8"))
        # print("send done")
        # os.path.isfile()
        # os.stat("sock")

Server.close()



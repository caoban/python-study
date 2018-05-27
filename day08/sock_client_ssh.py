import socket

Client = socket.socket()

Client.connect(('localhost',9999))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:continue
    Client.send(cmd.encode("utf-8"))
    cmd_res_size = Client.recv(1024) #接受命令结果的长度
    print("命令结果大小:",cmd_res_size)

    receive_size = 0
    receive_data = b''
    #cmd_res_size 是 byte类型
    while receive_size < int(cmd_res_size.decode()) :
        data = Client.recv(1024)
        receive_size += len(data) #判断每次收到的数据大小，并累加最后判断是否跟server端的大小一致。
        receive_data += data

    else:
        print("cmd res receivce done...", receive_size)
        print(receive_data.decode())

    #server端传过来的时候 encode，这边需要decode
Client.close()


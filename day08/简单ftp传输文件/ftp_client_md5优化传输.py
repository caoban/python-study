
import socket,hashlib
client = socket.socket()

client.connect(('localhost',9998))
while True:
    cmd = input(">>:").strip()
    #判断cmd是否为空
    if len(cmd) == 0:continue
    #如果命令是get开始字符
    if cmd.startswith("get"):
        #发送命令到server端
        client.send(cmd.encode())
        print("发送命令到server成功")
        server_response = client.recv(10240)
        print("server_response:",server_response)

        client.send(b"ready to recv file")
        #接收server端传过来的文件大小
        file_total_size  = int(server_response.decode())

        received_size = 0
        #获取client端执行时的文件名
        filename = cmd.split()[1]
        #打开要写入的新文件
        f = open(filename + ".new",'wb')
        m = hashlib.md5()

        while received_size < file_total_size:
            if file_total_size - received_size > 1024: #收不止一次
                size = 1024
            else:#收的少于1024  这样永远都不会粘包
                size = file_total_size - received_size

            data = client.recv(1024)
            received_size += len(data)
            m.update(data)
            f.write(data)

        else:
            print("file recv done", received_size,file_total_size)
            f.close()
        client_md5 =  m.hexdigest()
        server_md5 = client.recv(1024)

        print("servermd5:%s,clientmd5:%s" %(server_md5,client_md5))


client.close()
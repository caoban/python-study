import socket

Socket socket = getSocket(type = "TCP") #定好协议类型
connect(socket,address = "1,2,3,4",port = "80") #连接远程机器
send(socket,"Hello,World") #发送消息
close(socket) #关闭连接





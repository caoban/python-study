
import socket

#检查mysql端口的方法
def CheckMysqlPort():
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)
    try:
      sk.connect(('mdb.servers.dev.ofc',3306))
      print('mdb port 3306 OK!')
    except Exception:
      print('mdb port 3306 not connect!')
    sk.close()

def CheckRedisPort():
    sk2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk2.settimeout(1)
    try:
      sk2.connect(('redis.servers.dev.ofc',6379))
      print('redis port 6379 OK!')
    except Exception:
      print('redis port 6379 not connect!')
    sk2.close()

def CheckZkPort():
    sk3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk3.settimeout(1)
    try:
      sk3.connect(('10.101.9.207',2182))
      print('zk port 2182 OK!')
    except Exception:
      print('zk port 2182 not connect!')
    sk3.close()

def CheckShidcWsPort():
    sk4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk4.settimeout(1)
    try:
      sk4.connect(('10.101.11.102',80))
      print('ShidcWs port 80 OK!')
    except Exception:
      print('ShidcWs port 80 not connect!')
    sk4.close()

#上海redis 10.130.1.1:6379

#上海idc的mq



#main函数程序入口
if __name__ == "__main__":
    CheckMysqlPort()
    CheckRedisPort()
    CheckZkPort()
    CheckShidcWsPort()


import socket

def CheckMysqlPort():
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)
    try:
      sk.connect(('mdb.servers.product.sh',3306))
      print('mdb.servers.product.sh port 3306 OK!')
    except Exception:
      print('mdb.servers.product.sh port 3306 not connect!')
    sk.close()

def CheckRedisPort():
    sk2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk2.settimeout(1)
    try:
      sk2.connect(('10.130.1.1',6379))
      print('redis 10.130.1.1 port 6379 OK!')
    except Exception:
      print('redis 10.130.1.1 port 6379 not connect!')
    sk2.close()


def CheckZkPort():
    sk3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk3.settimeout(1)
    try:
      sk3.connect(('10.130.1.11',2181))
      print('zk 10.130.1.11 port 2181 OK!')
    except Exception:
      print('zk 10.130.1.11 port 2181 not connect!')
    sk3.close()

def CheckShidcWs80Port():
    sk4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk4.settimeout(1)
    try:
      sk4.connect(('10.129.5.18',80))
      print('ShidcWs 10.129.5.18 port 80 OK!')
    except Exception:
      print('ShidcWs 10.129.5.18 port 80 not connect!')
    sk4.close()

def CheckShidcWs443Port():
    sk4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk4.settimeout(1)
    try:
      sk4.connect(('10.129.5.18',443))
      print('ShidcWs 10.129.5.18 port 443 OK!')
    except Exception:
      print('ShidcWs 10.129.5.18 port 443 not connect!')
    sk4.close()

def CheckMqPort():
    sk4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk4.settimeout(1)
    try:
      sk4.connect(('mq.servers.product.sh',5672))
      print('mq.servers.product.sh 5672 OK!')
    except Exception:
      print('mq.servers.product.sh port 5672 not connect!')
    sk4.close()

#上海idc 的可以直接使用

if __name__ == "__main__":
    CheckMysqlPort()
    CheckRedisPort()
    CheckZkPort()
    CheckShidcWs80Port()
    CheckShidcWs443Port()
    CheckMqPort()


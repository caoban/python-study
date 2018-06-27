
import socket

def CheckMysqlPort():
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)
    try:
      sk.connect(('mdb.servers.product.ali',3306))
      print('mdb.servers.product.ali port 3306 OK!')
    except Exception:
      print('mdb.servers.product.ali port 3306 not connect!')
    sk.close()

def CheckRedisPort():
    sk2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk2.settimeout(1)
    try:
      sk2.connect(('192.168.96.4',6379))
      print('redis 192.168.96.4 port 6379 OK!')
    except Exception:
      print('redis 192.168.96.4 port 6379 not connect!')
    sk2.close()


def CheckZkPort():
    sk3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk3.settimeout(1)
    try:
      sk3.connect(('192.168.96.1',2181))
      print('zk 192.168.96.1 port 2181 OK!')
    except Exception:
      print('zk 192.168.96.1 port 2181 not connect!')
    sk3.close()

def CheckSLB80Port():
    sk4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk4.settimeout(1)
    try:
      sk4.connect(('192.168.64.4',80))
      print('alislb 192.168.64.4 port 80 OK!')
    except Exception:
      print('alislb 192.168.64.4 port 80 not connect!')
    sk4.close()

def CheckSLB443Port():
    sk4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk4.settimeout(1)
    try:
      sk4.connect(('192.168.64.4',443))
      print('alislb 192.168.64.4 port 443 OK!')
    except Exception:
      print('alislb 192.168.64.4 port 443 not connect!')
    sk4.close()




if __name__ == "__main__":
    CheckMysqlPort()
    CheckRedisPort()
    CheckZkPort()
    CheckSLB80Port()
    CheckSLB443Port()
    



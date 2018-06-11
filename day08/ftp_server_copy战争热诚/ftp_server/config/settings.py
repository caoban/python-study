# _*_ coding: utf-8 _*_
'''
这个里面就是一些配置的信息
'''

import os,sys,socket

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

#拼接出来accounts.ini的绝对路径
ACCOUNTS_FILE = os.path.join(BASE_DIR,'config','accounts.ini')

address_family = socket.AF_INET
socket_type = socket.SOCK_STREAM
print(address_family)
print(socket_type)

BIND_HOST = '127.0.0.1'
BIND_PORT = 9999
ip_port = (BIND_HOST,BIND_PORT)
print(ip_port)
coding = 'utf-8'
listen_count = 5
max_recv_bytes = 8192
allow_user_address = False











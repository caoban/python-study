# _*_ coding: utf-8 _*_

import os,sys,socket

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

#拼接出来accounts.ini的绝对路径
ACCOUNTS_FILE = os.path.join(BASE_DIR,'config','accounts.ini')

print(ACCOUNTS_FILE)




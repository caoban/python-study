# _*_ coding: utf-8 _*_
import os,sys

BASE_DIP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIP)

from core import ftp_server
from core import main
from config import settings

#主函数，程序入口，以后找也是从这里操作
if __name__ == '__main__':
    #是创建一个对象。 main.py中的Manager函数，所以我才百度搜不到啊。
    a = main.Manager()
    #调用对象的里面定义的方法
    a.interactive()











# _*_ coding: utf-8 _*_
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import ftp_server
from core import main
from config import settings


#主函数，程序的入口，以后找也是从这里进去操作。
if __name__ == '__main__':
    a = main.Manager()
    a.interactive()
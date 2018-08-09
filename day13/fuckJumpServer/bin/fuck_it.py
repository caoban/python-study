#_*_coding:utf-8_*_
__author__ = 'Alex Li'
import os,sys

#可以打印下看看是什么
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


print(BASE_DIR)
#添加到系统的PATH中
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    from modules.actions import excute_from_command_line
    excute_from_command_line(sys.argv)









# _*_ coding: utf-8 _*_
from core.user_handle import UserHandle
from core.ftp_server import FTPServer
from config import settings

class Manager():
    '''
    主程序，包括启动server创建用户，退出
    '''
    def start_ftp(self):
        '''
        启动server端
        :return: 
        '''
        #FTPserver是自定义的一个类
        #from core.ftp_server import FTPServer 所以可以直接使用，前面什么都不用加
        server = FTPServer(settings.ip_port)
        server.server_link()
        server.close()







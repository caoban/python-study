# _*_ coding: utf-8 _*_
import socket
import hashlib
import os
import struct
import pickle

from config import settings

#server的一些方式，自己封装了下
class FTPServer():
    def __init__(self,server_address,bind_and_listen = True):
        self.server_address = server_address
        self.socket = socket.socket(settings.address_family,settings.socket_type)
        if bind_and_listen:
            try:
                self.server_bind()
                self.server_listen()
            except Exception:
                self.server_close()

    #setsockopt设置socket的一些属性比如关闭了立即释放和重启socket的时候会用到
    def server_bind(self):
        allow_reuse_address = False
        if allow_reuse_address:
            self.socket.setsockopt(socket.SOL_IP,socket.SO_REUSEADDR,1)
        self.socket.bind(self.server_address)

    def server_listen(self):
        self.socket.listen(settings.listen_count)

    def server_close(self):
        self.socket.close()

    def server_accept(self):
        return self.socket.accept()


    def conn_close(self,conn):
        conn.close()

    def getfile_md5(self):
        '''获取文件的MD5'''
        return hashlib.md5(self.readfile()).hexdigest()

    def readfile(self):
        '''读取文件，获取文件内容的byte类型'''
        #read 是全部读取完，这样文件大不行啊。还是要一行行读，用md5的update来加密呀
        with open(self.file_path,'rb') as f:
            filedata = f.read()
        return filedata

    def sed_filedata(self,exist_file_size=0):
        """下载时将文件打开send(data)"""
        with open(self.file_path,'rb') as f:
            f.seek(exist_file_size)
            while True:
                data = f.read(1024)
                if data :
                    self.conn.send(data)
                else:
                    break

    def get(self,cmds):
        '''
        下载时先检查文件是否存在，然后上传文件的报头大小，上传文件，以读的方式发送文件
        找到下载的文件
        发送 header_size
        发送 header_bytes file_size
        读文件 rb 发送send(line)
        若文件不存在，发送0 client提示文件不存在
        '''


        if len(cmds) > 1:
            filename = cmds[1]
            self.file_path = os.path.join(os.getcwd(),filename)
            if os.path.isfile(self.file_path):
                file_size = os.path.getsize(self.file_path)
                obj = self.conn.recv(4)
                exit_file_size = struct.unpack('i',obj)[0]
                header = {
                    'filename' : filename,
                    'filemd5': self.getfile_md5(),
                    'file_size' : file_size
                }
                header_bytes = pickle.dumps(header)
                self.conn.send(struct.pack('i',len(header_bytes)))
                self.conn.send(header_bytes)

                if exit_file_size : #表示之前被下载过一部分
                    if exit_file_size != file_size:
                        self.send_filedata(exit_file_size)
                    else:
                        print('\033[31;1mbreakpoint and file size are the same\033[0m')

                else:#第一次下载
                    self.send_filedata()
            else:
                print('\033[31;1merror\033[0m')
                self.conn.send(struct.pack('i',0))
        else:
            print("\033[31;1muser does not enter file name\033[0m")


    def recursion_file(self,dir):
        """递归查出用户目录下的所有文件，算出文件的大小。函数里面再自己调用自己"""

        #列出来对应路径下面的文件和文件夹 不包括.和..
        res = os.listdir(dir)
        for i in res:
            path = os.path.join(dir,i)
            if os.path.isdir(path):
                self.recursion_file(path)
            elif os.path.isfile(path):
                self.home_bytes_size += os.path.getsize(path)


    def current_home_size(self):
        """得到当前用户的目录的大小，字节/M"""
        self.home_bytes_size = 0
        self.recursion_file(self.homedir_path)
        home_m_size = round(self.home_bytes_size / 1024 /1024,1)

    def put(self,cmds):
        """从client上传文件到server当前工作目录下"""
        if len(cmds) > 1:
            obj = self.conn.recv(4)
            #这个 0 是什么意思没有明白
            state_size = struct.unpack('i',obj)[0]
            if state_size == 0:
                print("\033[31;1mfile does not exist!\033[0m")

            else:
                #算出了home下已被占用的大小self.home_bytes_size
                self.current_home_size()
                header_bytes = self.conn.recv(struct.unpack('i',self.conn.recv(4))[0])
                header_dic = pickle.loads(header_bytes)
                filename = header_dic.get('filename')
                file_size = header_dic.get('file_size')
                file_md5 = header_dic.get()











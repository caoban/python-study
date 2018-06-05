# _*_ coding: utf-8 _*_
import socket
import hashlib
import os
import struct
import pickle
import subprocess

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
                self.file_path = os.path.join(os.getcwd(),filename)

                if os.path.exists(self.file_path):
                    self.conn.send(struct.pack('i',1))
                    has_size = os.path.getsize(self.file_path)
                    if has_size == file_size:
                        print("\033[31;1mfile already does exist!\033[0m")
                        self.conn.send(struct.pack('i',0))
                    else:
                        print('\033[31;1mLast file not finished,this time continue\033[0m')
                        self.conn.send(struct.pack('i',1))
                        if self.home_bytes_size + int(file_size - has_size) > self.quota_bytes:
                            print('\033[31;1mSorry exceeding user quotas\033[0m')
                            self.conn.send(struct.pack('i',0))
                        else:
                            self.conn.send(struct.pack('i',1))
                            self.conn.send(struct.pack('i',has_size))
                            with open(self.file_path,'ab') as f:
                                f.seek(has_size)
                                self.write_file(f,has_size,file_size)
                            #用自己写的算MD5的方法
                            self.verification_filemd5(file_md5)


                else:
                    self.conn.send(struct.pack('i',0))
                    print('\033[31;1mSorry file does not exist now first put\033[0m')
                    if self.home_bytes_size + int(file_size) > self.quota_bytes:
                        print('\033[31;1mSorry exceeding user quotas\033[0m')
                        #struct.pack 格式化字符的 i 表示int。0要么表示数据的0什么的，要么就是真的0
                        self.conn.send(struct.pack('i',0))
                    else:
                        self.conn.send(struct.pack('i',1))
                        with open(self.file_path,'wb') as f:
                            #写入文件
                            recv_size = 0
                            self.write_file(f,recv_size,file_size)
                        self.verification_filemd5(file_md5)


        else:
            print("\033[31;1muser does not enter file name\033[0m")


    def write_file(self,f,recv_size,file_size):
        """上传文件时，将文件内容写入文件中"""
        while recv_size < file_size:
            #每次接收的数据，循环写入文件中
            res = self.conn.recv(settings.max_recv_bytes)
            f.write(res)
            recv_size += len(res)
            #为了进度条显示
            self.conn.send(struct.pack('i',recv_size))

    #只是对比下MD5值，传完文件前后
    def verification_filemd5(self,filemd5):
        #判断文件内容的MD5
        if self.getfile_md5() == filemd5:
            print('\033[31;1mCongratulations download success\033[0m')
            #传个int型的1过去
            self.conn.send(struct.pack('i',1))
        else:
            print('\033[31;1mSorry download failed\033[0m')
            self.conn.send(struct.pack('i',0))


    def ls(self):
        """查看当前工作目录下，先返回文件列表的大小，再返回查询的结果"""
        print("\033[34;1mview current working directory\033[0m")
        subpro_obj = subprocess.Popen('dir',shell=True,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
        stdout = subpro_obj.stdout.read()
        stderr = subpro_obj.stderr.read()
        self.conn.send(struct.pack('i',len(stdout + stderr)))
        self.conn.send(stdout)
        self.conn.send(stderr)

    def mkdir(self,cmds):
        """增加目录
        在当前目录下，增加目录
        1、查看目录名是否已经存在
        2、增加目录成功返回1 
        3、增加目录失败返回0
        """
        print("\033[34;1madd working directory\033[0m")
        if len(cmds) > 1:
            mkdir_path = os.path.join(os.getcwd(),cmds[1])
            if not os.path.exists(mkdir_path):
                os.mkdir(mkdir_path)
                print('\033[31;1mCongratulations add directory success\033[0m')
                self.conn.send(struct.pack('i',1))
            else:
                print("\033[31;1muser directory already does exist\033[0m")
                self.conn.send(struct.pack('i',0))
        else:
            print("\033[31;1muser does not enter file name\033[0m")

    def cd(self,cmds):
        """
        切换目录
        1、查看是否是目录名
        2、拿到当前目录，拿到目标目录
        3、判断homedir是否在目标目录内，防止用户越过自己的home目录
        4、切换成功，返回1
        5、切换失败返回0
        """
        print("\033[34;1mSwitch working directory\033[0m")
        if len(cmds) > 1:
            dir_path = os.path.join(os.getcwd(),cmds[1])
            if os.path.isdir(dir_path):
                #os.getcwd,获取当前目录
                previous_path = os.getcwd()
                #os.chdir改变当前脚本目录
                os.chdir(dir_path)
                target_dir = os.getcwd()
                if self.homedir_path in target_dir:
                    print('\033[31;1mCongratulations switch directory success\033[0m')
                    self.conn.send(struct.pack('i',1))
                else:
                    print('\033[31;1mSorry switch directory failed\033[0m')
                    #切换失败后，返回到之前的目录下
                    os.chdir(previous_path)
                    self.conn.send(struct.pack('i',0))
            else:
                print('\033[31;1mSorry switch directory failed,the directory is not current directory\033[0m')
                self.conn.send(struct.pack('i', 0))

        else:
            print("\033[31;1muser does not enter file name\033[0m")


    def remove(self,cmds):
        """删除指定的文件或者空的文件夹
        1.删除成功，返回1
        2、删除失败，返回0
        """
        print("\033[34;1mRemove working directory\033[0m")
        if len(cmds) > 1:
            file_name = cmds[1]
            file_path = os.path.join(os.getcwd(),file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
                self.conn.send(struct.pack('i', 1))
            #删除目录
            elif os.path.isdir(file_path):
                if not len(os.listdir(file_path)):
                    os.removedirs(file_path)
                    print('\033[31;1mCongratulations remove success\033[0m')
                    self.conn.send(struct.pack('i', 1))
                else:
                    print('\033[31;1mSorry remove directory failed\033[0m')
                    self.conn.send(struct.pack('i', 0))

            else:
                print('\033[31;1mSorry remove directory failed\033[0m')
                self.conn.send(struct.pack('i', 0))
        else:
            print("\033[31;1muser does not enter file name\033[0m")


    def get_recv(self):
        """从client端接收发出来的数据"""
        user_dic = self.get_recv()
        username = user_dic['username']
        password = user_dic['password']
        md5_obj = hashlib.md5()
        md5_obj.update(password)
        check_password = md5_obj.hexdigest()

    def auth(self):
        """
        处理用户的认证请求
        1、根据username读取account.ini文件，然后查看用户是否存在
        2、将程序运行的目录从bin.user_auth修改到用户home/username方便之后查询
        3、把客户端返回用户的详细信息
        """
        while True:
            user_dic = self.get_recv()
            username = user_dic['username']
            password = user_dic['password']
            md5_obj = hashlib.md5(password.encode('utf-8'))
            check_password = md5_obj.hexdigest()
            user_handle = UserHandle(username)
            #判断用户是否存在，返回列表
            user_data = user_handle.judge_user()
            if  user_data:
                pass











































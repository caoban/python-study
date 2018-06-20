# _*_ coding: utf-8 _*_
import socket
import struct
import json
import os
import pickle
import subprocess
import hashlib

from config import settings
from core.user_handle import UserHandle


#就一个class，里面定义个各种server端的方法。
class FTPServer():
    #判断写在__init__里面，调用下面定义的方法。
    def __init__(self, server_address, bind_and_listen=True):
        self.server_address = server_address
        self.socket = socket.socket(settings.address_family, settings.socket_type)
        if bind_and_listen:
            try:
                self.server_bind()
                self.server_listen()
            except Exception:
                self.server_close()

    #绑定server
    def server_bind(self):
        allow_reuse_address = False
        if allow_reuse_address:
            #SOL_SOCKET 当用closesocket时马上关闭socket
            #SO_REUSEADDR 关闭以后的可以立刻使用  1 应该表示是时间
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)

    #监听 封装成一个方法。 里面的参数用的是import进来的配置文件中的。
    def server_listen(self):
        self.socket.listen(settings.listen_count)

    def server_close(self):
        self.socket.close()

    def server_accept(self):
        return self.socket.accept()

    def conn_close(self, conn):
        conn.close()

    def getfile_md5(self):
        '''获取文件的md5'''
        return hashlib.md5(self.readfile()).hexdigest()

    def readfile(self):
        '''读取文件，得到文件内容的bytes类型'''
        with open(self.file_path, 'rb') as f:
            filedata = f.read()
        return filedata

    def send_filedata(self, exist_file_size=0):
        """下载时，将文件打开，send(data)"""
        with open(self.file_path, 'rb') as f:
            f.seek(exist_file_size)
            while True:
                data = f.read(1024)
                if data:
                    self.conn.send(data)
                else:
                    break

    def get(self, cmds):
        '''
       下载，首先查看文件是否存在，然后上传文件的报头大小，上传文件，以读的方式发开文件
       找到下载的文件
    发送 header_size
    发送 header_bytes file_size
    读文件 rb 发送 send(line)
    若文件不存在，发送0 client提示：文件不存在
       :param cmds:
       :return:
               '''
        if len(cmds) > 1:
            filename = cmds[1]
            self.file_path = os.path.join(os.getcwd(), filename)
            if os.path.isfile(self.file_path):
                file_size = os.path.getsize(self.file_path)
                obj = self.conn.recv(4)
                exist_file_size = struct.unpack('i', obj)[0]
                header = {
                    'filename': filename,
                    'filemd5': self.getfile_md5(),
                    'file_size': file_size
                }
                header_bytes = pickle.dumps(header)
                self.conn.send(struct.pack('i', len(header_bytes)))
                self.conn.send(header_bytes)
                if exist_file_size:  # 表示之前被下载过 一部分
                    if exist_file_size != file_size:
                        self.send_filedata(exist_file_size)
                    else:
                        print('\033[31;1mbreakpoint and file size are the same\033[0m')
                else:  # 文件第一次下载
                    self.send_filedata()
            else:
                print('\033[31;1merror\033[0m')
                self.conn.send(struct.pack('i', 0))

        else:
            print("\033[31;1muser does not enter file name\033[0m")

    def recursion_file(self, dir):
        """递归查询用户目录下的所有文件，算出文件的大小"""
        res = os.listdir(dir)
        for i in res:
            path = os.path.join(dir, i)
            if os.path.isdir(path):
                self.recursion_file(path)
            elif os.path.isfile(path):
                self.home_bytes_size += os.path.getsize(path)

    def current_home_size(self):
        """得到当前用户目录的大小，字节/M"""
        self.home_bytes_size = 0
        self.recursion_file(self.homedir_path)
        home_m_size = round(self.home_bytes_size / 1024 / 1024, 1)

    def put(self, cmds):
        """从client上传文件到server当前工作目录下
        """
        if len(cmds) > 1:
            obj = self.conn.recv(4)
            state_size = struct.unpack('i', obj)[0]
            if state_size == 0:
                print("\033[31;1mfile does not exist!\033[0m")
            else:
                # 算出了home下已被占用的大小self.home_bytes_size
                self.current_home_size()
                header_bytes = self.conn.recv(struct.unpack('i', self.conn.recv(4))[0])
                header_dic = pickle.loads(header_bytes)
                filename = header_dic.get('filename')
                file_size = header_dic.get('file_size')
                file_md5 = header_dic.get('file_md5')
                self.file_path = os.path.join(os.getcwd(), filename)
                if os.path.exists(self.file_path):
                    self.conn.send(struct.pack('i', 1))
                    has_size = os.path.getsize(self.file_path)
                    if has_size == file_size:
                        print("\033[31;1mfile already does exist!\033[0m")
                        self.conn.send(struct.pack('i', 0))
                    else:
                        print('\033[31;1mLast file not finished,this time continue\033[0m')
                        self.conn.send(struct.pack('i', 1))
                        if self.home_bytes_size + int(file_size - has_size) > self.quota_bytes:
                            print('\033[31;1mSorry exceeding user quotas\033[0m')
                            self.conn.send(struct.pack('i', 0))
                        else:
                            self.conn.send(struct.pack('i', 1))
                            self.conn.send(struct.pack('i', has_size))
                            with open(self.file_path, 'ab') as f:
                                f.seek(has_size)
                                self.write_file(f, has_size, file_size)
                            self.verification_filemd5(file_md5)
                else:
                    self.conn.send(struct.pack('i', 0))
                    print('\033[31;1mSorry file does not exist now first put\033[0m')
                    if self.home_bytes_size + int(file_size) > self.quota_bytes:
                        print('\033[31;1mSorry exceeding user quotas\033[0m')
                        self.conn.send(struct.pack('i', 0))
                    else:
                        self.conn.send(struct.pack('i', 1))
                        with open(self.file_path, 'wb') as f:
                            recv_size = 0
                            self.write_file(f, recv_size, file_size)
                        self.verification_filemd5(file_md5)

        else:
            print("\033[31;1muser does not enter file name\033[0m")

    def write_file(self, f, recv_size, file_size):
        '''上传文件时，将文件内容写入到文件中'''
        while recv_size < file_size:
            res = self.conn.recv(settings.max_recv_bytes)
            f.write(res)
            recv_size += len(res)
            self.conn.send(struct.pack('i', recv_size))  # 为了进度条的显示

    def verification_filemd5(self, filemd5):
        # 判断文件内容的md5
        if self.getfile_md5() == filemd5:
            print('\033[31;1mCongratulations download success\033[0m')
            self.conn.send(struct.pack('i', 1))
        else:
            print('\033[31;1mSorry download failed\033[0m')
            self.conn.send(struct.pack('i', 0))

    def ls(self, cmds):
        '''查看当前工作目录下，先返回文件列表的大小，在返回查询的结果'''
        print("\033[34;1mview current working directory\033[0m")
        subpro_obj = subprocess.Popen('dir', shell=True,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
        stdout = subpro_obj.stdout.read()
        stderr = subpro_obj.stderr.read()
        self.conn.send(struct.pack('i', len(stdout + stderr)))
        self.conn.send(stdout)
        self.conn.send(stderr)

    def mkdir(self, cmds):
        '''增加目录
        在当前目录下,增加目录
        1.查看目录名是否已经存在
        2.增加目录成功,返回 1
        2.增加目录失败,返回 0'''
        print("\033[34;1madd working directory\033[0m")
        if len(cmds) > 1:
            mkdir_path = os.path.join(os.getcwd(), cmds[1])
            if not os.path.exists(mkdir_path):
                os.mkdir(mkdir_path)
                print('\033[31;1mCongratulations add directory success\033[0m')
                self.conn.send(struct.pack('i', 1))
            else:
                print("\033[31;1muser directory already does exist\033[0m")
                self.conn.send(struct.pack('i', 0))
        else:
            print("\033[31;1muser does not enter file name\033[0m")

    def cd(self, cmds):
        '''切换目录
        1.查看是否是目录名
        2.拿到当前目录,拿到目标目录,
        3.判断homedir是否在目标目录内,防止用户越过自己的home目录 eg: ../../....
        4.切换成功,返回 1
        5.切换失败,返回 0'''
        print("\033[34;1mSwitch working directory\033[0m")
        if len(cmds) > 1:
            dir_path = os.path.join(os.getcwd(), cmds[1])
            if os.path.isdir(dir_path):
                # os.getcwd 获取当前工作目录
                previous_path = os.getcwd()
                # os.chdir改变当前脚本目录
                os.chdir(dir_path)
                target_dir = os.getcwd()
                if self.homedir_path in target_dir:
                    print('\033[31;1mCongratulations switch directory success\033[0m')
                    self.conn.send(struct.pack('i', 1))
                else:
                    print('\033[31;1mSorry switch directory failed\033[0m')
                    # 切换失败后,返回到之前的目录下
                    os.chdir(previous_path)
                    self.conn.send(struct.pack('i', 0))
            else:
                print('\033[31;1mSorry switch directory failed,the directory is not current directory\033[0m')
                self.conn.send(struct.pack('i', 0))
        else:
            print("\033[31;1muser does not enter file name\033[0m")

    def remove(self, cmds):
        """删除指定的文件,或者空文件夹
               1.删除成功,返回 1
               2.删除失败,返回 0
               """
        print("\033[34;1mRemove working directory\033[0m")
        if len(cmds) > 1:
            file_name = cmds[1]
            file_path = os.path.join(os.getcwd(), file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
                self.conn.send(struct.pack('i', 1))
            elif os.path.isdir(file_path):  # 删除空目录
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
        '''从client端接收发来的数据'''
        return pickle.loads(self.conn.recv(settings.max_recv_bytes))

    def handle_data(self):
        '''处理接收到的数据，主要是将密码转化为md5的形式'''
        user_dic = self.get_recv()
        username = user_dic['username']
        password = user_dic['password']
        md5_obj = hashlib.md5()
        md5_obj.update(password)
        check_password = md5_obj.hexdigest()

    def auth(self):
        '''
        处理用户的认证请求
        1，根据username读取accounts.ini文件，然后查看用户是否存在
        2，将程序运行的目录从bin.user_auth修改到用户home/username方便之后查询
        3，把客户端返回用户的详细信息
        :return:
        '''
        while True:
            user_dic = self.get_recv()
            username = user_dic['username']
            password = user_dic['password']
            md5_obj = hashlib.md5(password.encode('utf-8'))
            check_password = md5_obj.hexdigest()
            user_handle = UserHandle(username)
            # 判断用户是否存在 返回列表,
            user_data = user_handle.judge_user()
            if user_data:
                if user_data[0][1] == check_password:
                    self.conn.send(struct.pack('i', 1))  # 登录成功返回 1
                    self.homedir_path = os.path.join(settings.BASE_DIR, 'home', username)
                    # 将程序运行的目录名修改到 用户home目录下
                    os.chdir(self.homedir_path)
                    # 将用户配额的大小从M 改到字节
                    self.quota_bytes = int(user_data[2][1]) * 1024 * 1024
                    user_info_dic = {
                        'username': username,
                        'homedir': user_data[1][1],
                        'quota': user_data[2][1]
                    }
                    # 用户的详细信息发送到客户端
                    self.conn.send(pickle.dumps(user_info_dic))
                    return True
                else:
                    self.conn.send(struct.pack('i', 0))  # 登录失败返回 0
            else:
                self.conn.send(struct.pack('i', 0))  # 登录失败返回 0

    def server_link(self):
        print("\033[31;1mwaiting client .....\033[0m")
        while True:  # 链接循环
            self.conn, self.client_addr = self.server_accept()
            while True:  # 通信循环
                try:
                    self.server_handle()
                except Exception:
                    break
            self.conn_close(self.conn)

    def server_handle(self):
        '''处理与用户的交互指令'''
        if self.auth():
            print("\033[32;1m-------user authentication successfully-------\033[0m")
            res = self.conn.recv(settings.max_recv_bytes)
            # 解析命令，提取相应的参数
            cmds = res.decode(settings.coding).split()
            if hasattr(self, cmds[0]):
                func = getattr(self, cmds[0])
                func(cmds)
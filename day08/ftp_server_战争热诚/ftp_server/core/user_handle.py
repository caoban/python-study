# _*_ coding: utf-8 _*_
import configparser
import hashlib
import os

from config import settings


class UserHandle():
    '''
    创建用户名称，密码
    如果用户存在，则返回，如果用户不存在，则注册成功
    '''

    def __init__(self, username):
        self.username = username
        #configparser.ConfigParser 是对指定的配置文件进行增删改查操作 my.cnf那种格式的文件
        self.config = configparser.ConfigParser()
        #读入文件，accounts.ini 文件，后面估计做修改用.settings.ACCOUNTS_FILE是自己定义的
        self.config.read(settings.ACCOUNTS_FILE)

    #@property 属性方法，赋值的操作。 当做一个变量那种去赋值。 但是没有存下来。不能()的方式调用
    @property
    def password(self):
        #就是输入后，使用MD5加密操作
        '''生成用户的默认密码  '''
        password_inp = input("\033[32;1mplease input your password>>>\033[0m").strip()
        md5_obj = hashlib.md5()
        md5_obj.update(password_inp.encode())
        md5_password = md5_obj.hexdigest()
        return md5_password

    @property
    def disk_quota(self):
        '''生成每个用户的磁盘配额'''
        quota = input('\033[32;1mplease input Disk quotas>>>:\033[0m').strip()
        #isdigit() 判断字符是否只有数据组成
        if quota.isdigit():
            return quota
        else:
            exit('\033[31;1mdisk quotas must be integer\033[0m')

    def add_user(self):
        """创建用户,存到accounts.ini"""
        #config.has_section 是判断配置文件中是否有 [xxx] 这个块字段
        if not self.config.has_section(self.username):
            #如果没有，就添加用户
            print('\033[31;1mcreating username is :%s \033[0m' % self.username)
            self.config.add_section(self.username)
            self.config.set(self.username, 'password', self.password)
            self.config.set(self.username, 'homedir', 'home/' + self.username)
            self.config.set(self.username, 'quota', self.disk_quota)
            with open(settings.ACCOUNTS_FILE, 'w') as f:
                self.config.write(f)
            os.mkdir(os.path.join(settings.BASE_DIR, 'home', self.username))  # 创建用户的home文件夹
            print('\033[1;32msuccessfully create userdata\033[0m')
        else:
            print('\033[1;31musername already existing\033[0m')

    def judge_user(self):
        """判断用户是否存在"""
        #判断是否存在，在添加用户的时候也用到这个
        if self.config.has_section(self.username):
            return self.config.items(self.username)
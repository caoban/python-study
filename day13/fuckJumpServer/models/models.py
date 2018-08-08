#导入ORM 需要的模块
from sqlalchemy import Table, Column, Enum,Integer,String,DATE, ForeignKey,UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import ChoiceType

#生成ORM基类
Base = declarative_base()

#建立多对多的关系
#一个主机，对应多个堡垒机用户的账号
host_m2m_remoteuser = Table('host_m2m_remoteuser',Base.metadata,
                            Column('host_id', Integer, ForeignKey('host.id')),#ForeignKey 是这个表中的字段关联到对应的哪个表哪个字段
                            Column('remoteuser_id', Integer, ForeignKey('remote_user.id'))
                            )







class Host(Base):
    __tablename__ = 'host' #表名
    id = Column(Integer,primary_key=True) #创建id 设置成主键，是默认自增的
    hostname = Column(String(64),unique=True) #unique=True 表示必须唯一
    ip = Column(String(64),unique=True)
    port = Column(Integer,default=22)

    #建立关联关系。一个主机，对应多个堡垒机用户的账号
    # Host类中的表和RemoteUser类中的表建立关联，存在第三张host_m2m_remoteuser中。
    #反查Host类中的表的数据的时候 使用 hosts 查
    remote_users = relationship('RemoteUser', secondary=host_m2m_remoteuser, backref='hosts')

    #这个函数是为了显示的时候能显示值，不会显示函数的内存地址
    #return 是自己写的
    def __repr__(self):
        return self.hostname


class HostGroup(Base):
    __tablename__ = 'host_group'
    id = Column(Integer, primary_key=True)  # 创建id 设置成主键，是默认自增的
    name = Column(String(64),unique=True)

    def __repr__(self):
        return self.name


#服务器的用户和密码，登录类型
class RemoteUser(Base):
    __tablename__ = 'remote_user'
    #'auth_type','username','password' 联合在一起必须是唯一的。叫联合唯一。 存到 _user_passwd_uc 字段中
    __table_args__ = (UniqueConstraint('auth_type', 'username', 'password', name='_user_passwd_uc'),)
    id = Column(Integer, primary_key=True)  # 创建id 设置成主键，是默认自增的
    #登录类型。里面是两个元祖，映射关系。SSH/Password是提示相当于，也可以是中文。只是显示
    AuthTypes = [
        ('ssh-password','SSH/Password'),
        ('ssh-key','SSH/KEY'),
    ]
    auth_type = Column(ChoiceType(AuthTypes)) #选择类型
    username = Column(String(32))
    password = Column(String(128))


    def __repr__(self):
        return self.username


class UserProfile(Base):
    __tablename__ = 'user_profile'
    id = Column(Integer, primary_key=True)
    username = Column(String(32),unique=True)
    password = Column(String(128))

    def __repr__(self):
        return self.username























#导入ORM 需要的模块
from sqlalchemy import Table, Column, Enum,Integer,String,DATE, ForeignKey,UniqueConstraint, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import ChoiceType

#生成ORM基类
Base = declarative_base()

#建立多对多的关系
#一个主机，对应多个堡垒机用户的账号
user_m2m_bindhost = Table('user_m2m_bindhost',Base.metadata,
                            Column('userprofile_id', Integer, ForeignKey('user_profile.id')),#ForeignKey 是这个表中的字段关联到对应的哪个表哪个字段
                            Column('bindhost_id', Integer, ForeignKey('bind_host.id'))
                            )


bindhost_m2m_hostgroup = Table('bindhost_m2m_hostgroup',Base.metadata,
                            Column('bindhost_id', Integer, ForeignKey('bind_host.id')),#ForeignKey 是这个表中的字段关联到对应的哪个表哪个字段
                            Column('hostgroup_id', Integer, ForeignKey('host_group.id'))
                            )

user_m2m_hostgroup = Table('userprofile_m2m_hostgroup',Base.metadata,
                            Column('userprofile_id', Integer, ForeignKey('user_profile.id')),#ForeignKey 是这个表中的字段关联到对应的哪个表哪个字段
                            Column('hostgroup_id', Integer, ForeignKey('host_group.id'))
                            )




class Host(Base):
    __tablename__ = 'host' #表名
    id = Column(Integer,primary_key=True) #创建id 设置成主键，是默认自增的
    hostname = Column(String(64),unique=True) #unique=True 表示必须唯一
    ip = Column(String(64),unique=True)
    port = Column(Integer,default=22)


    #这个函数是为了显示的时候能显示值，不会显示函数的内存地址
    #return 是自己写的
    def __repr__(self):
        return self.hostname


class HostGroup(Base):
    __tablename__ = 'host_group'
    id = Column(Integer, primary_key=True)  # 创建id 设置成主键，是默认自增的
    name = Column(String(64),unique=True)

    bind_hosts = relationship("BindHost",secondary='bindhost_m2m_hostgroup', backref='host_groups')

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


class BindHost(Base):

    '''
    #存入ip 类型 所属组的关系
    192.168.1.11 web bj_group
    192.168.1.11 mysql sh_group
    '''
    __tablename__ = 'bind_host'
    #最后的一个 逗号一定要记得
    __table_args__ = (UniqueConstraint('host_id', 'remoteuser_id', name='_host_remoteuser_uc'),)

    id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey('host.id'))
    #group_id = Column(Integer, ForeignKey('group.id'))
    remoteuser_id = Column(Integer, ForeignKey('remote_user.id'))

    #做关联关系，得有外键
    host = relationship("Host",backref="bind_hosts")
    #host_group = relationship("HostGroup",backref="bind_hosts")
    remote_user = relationship("RemoteUser",backref="bind_hosts")

    #返回到时候显示的时候想要的值
    def __repr__(self):
        return "<%s--%s>" %(self.host.ip,
                                self.remote_user.username
                              )



class UserProfile(Base):
    __tablename__ = 'user_profile'
    id = Column(Integer, primary_key=True)
    username = Column(String(32),unique=True)
    password = Column(String(128))

    #secondary 是 第三张表的表名
    bind_hosts = relationship("BindHost", secondary='user_m2m_bindhost',backref="user_profiles")
    host_groups = relationship("HostGroup", secondary='userprofile_m2m_hostgroup', backref='user_profiles')

    def __repr__(self):
        return self.username























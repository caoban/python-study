#导入ORM 需要的模块
from sqlalchemy import Table, Column, Enum,Integer,String,DATE, ForeignKey,UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import ChoiceType

#生成ORM基类
Base = declarative_base()

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

    def __repr__(self):
        return self.name


class RemoteUser(Base):
    __tablename__ = 'remote_user'
    id = Column(Integer, primary_key=True)  # 创建id 设置成主键，是默认自增的
    auth_type = Column(Enum(0,1)) #枚举类型，在0,1 之间选择
    username = Column(String(32))
    password = Column(String(128))

    def __repr__(self):
        return self.username








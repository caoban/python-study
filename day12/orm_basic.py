import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

#建立数据连接  echo=True 会把所有的信息都打印出来
engine = create_engine("mysql+pymysql://root:alex3714@localhost/testdb",
                       encoding='utf-8', echo=True)



Base = declarative_base()  # 生成orm基类


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    #加这个东西，查询数据的时候，显示的信息就更清楚了。
    def __repr__(self):
        return "<%s name:%s>" % (self.id,self.name)


Base.metadata.create_all(engine)  # 创建表结构

#生成一个类。sessionmaker是上面import进来的
#创建与数据库会话的session类。这里返回的是个类，不是实例
Session_class = sessionmaker(bind=engine)
#实例化一个对象
Session = Session_class()


#
# #生成要创建的数据库对象。
# # 里面是 内容，是要插入的数据，id是自增的可以不用写
# user_obj = User(name="alex",password="alex3714")
#
# #上面的是声明，还没创建对象呢，不信打印一下id 发现是null
# print(user_obj.name, user_obj.id)
#
# #把要创建的数据对象添加到这个session里面，一会同意创建
# Session.add(user_obj)
#
# #上面还没有创建
# print(user_obj.name, user_obj.id)
#
# #现在提交了 才创建
# Session.commit()

#查询数据。filter_by中可以加上name="alex" 过滤条件
#all是所有 first是第一个
#filter(User.id>2)  这样才能写大于，filter_by不可以
#filter_by(id==2)  filter_by是这样写的

data = Session.query(User).filter_by().all()
print(data)

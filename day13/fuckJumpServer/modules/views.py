#引用models 目录下面的models.py
from models import models
from conf import settings
from modules.utils import print_err,yaml_parser
from modules.db_conn import engine,session

def syncdb(argvs):
    print("Syncing DB....")
    #create_engine 在models 目录下面的models.py中已经引用了
    engine = models.create_engine(settings.ConnParams,
        echo=True
    )
    models.Base.metadata.create_all(engine) #创建所有表结构

def create_hosts(argvs):
    '''
    create hosts
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        hosts_file  = argvs[argvs.index("-f") +1 ]
    else:
        print_err("invalid usage, should be:\ncreate_hosts -f <the new hosts file>",quit=True)
    source = yaml_parser(hosts_file)
    if source:
        for key,val in source.items():
            print(key,val)

            #models.Host 是导入进来的。是from models import models
            #把参数给models.py中的Host类中的形参
            obj = models.Host(hostname=key,ip=val.get('ip'), port=val.get('port') or 22)
            session.add(obj)
        #一定要提交才能真的插入进去
        session.commit()


#具体的插入表数据的函数


def create_remoteusers(argvs):
    '''
    create remoteusers
    :param argvs:
    :return:
    '''
    # 里面加了判断是否是文件
    if '-f' in argvs:
        remoteusers_file  = argvs[argvs.index("-f") +1 ]
    else:
        print_err("invalid usage, should be:\ncreate_remoteusers -f <the new remoteusers file>",quit=True)

    #从yaml中 load 出来
    source = yaml_parser(remoteusers_file)
    if source:
        for key,val in source.items():
            print(key,val)
    #把 yaml中load出来的值获取到，赋值给对应的 sql中表的字段
            obj = models.RemoteUser(username=val.get('username'),auth_type=val.get('auth_type'),password=val.get('password'))
            session.add(obj)
    #再提交，真正的插入数据到表中
        session.commit()

#创建堡垒机用户
def create_users(argvs):
    '''
    create little_finger access user
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        user_file  = argvs[argvs.index("-f") +1 ]
    else:
        print_err("invalid usage, should be:\ncreateusers -f <the new users file>",quit=True)

    source = yaml_parser(user_file)
    if source:
        for key,val in source.items():
            print(key,val)
            #创建用户
            obj = models.UserProfile(username=key,password=val.get('password'))

            #判断是否有groups数据，有的话做如下的操作
            # if val.get('groups'):
            #     groups = session.query(models.Group).filter(models.Group.name.in_(val.get('groups'))).all()
            #     if not groups:
            #         print_err("none of [%s] exist in group table." % val.get('groups'),quit=True)
            #     obj.groups = groups
            # if val.get('bind_hosts'):
            #     bind_hosts = common_filters.bind_hosts_filter(val)
            #     obj.bind_hosts = bind_hosts
            # #print(obj)
            session.add(obj)
        session.commit()

def create_groups(argvs):
    '''
    create groups
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        group_file  = argvs[argvs.index("-f") +1 ]
    else:
        print_err("invalid usage, should be:\ncreategroups -f <the new groups file>",quit=True)
    source = yaml_parser(group_file)
    if source:
        for key,val in source.items():
            print(key,val)
            obj = models.HostGroup(name=key)

            # if val.get('bind_hosts'):
            #     bind_hosts = common_filters.bind_hosts_filter(val)
            #     obj.bind_hosts = bind_hosts
            #
            # if val.get('user_profiles'):
            #     user_profiles = common_filters.user_profiles_filter(val)
            #     obj.user_profiles = user_profiles

            session.add(obj)
        session.commit()

def create_bindhosts(argvs):
    '''
    create bind hosts
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        bindhosts_file  = argvs[argvs.index("-f") +1 ]
    else:
        print_err("invalid usage, should be:\ncreate_hosts -f <the new bindhosts file>",quit=True)
    source = yaml_parser(bindhosts_file)
    if source:
        for key,val in source.items():
            #print(key,val)  查出主机名
            host_obj = session.query(models.Host).filter(models.Host.hostname==val.get('hostname')).first()

            #assert 断言，host_obj存在才能往下走
            assert host_obj
            for item in val['remote_users']:
                print(item )
                assert item.get('auth_type')
                if item.get('auth_type') == 'ssh-password':
                    remoteuser_obj = session.query(models.RemoteUser).filter(
                                                        models.RemoteUser.username==item.get('username'),
                                                        models.RemoteUser.password==item.get('password')
                                                    ).first()
                else:
                    remoteuser_obj = session.query(models.RemoteUser).filter(
                                                        models.RemoteUser.username==item.get('username'),
                                                        models.RemoteUser.auth_type==item.get('auth_type'),
                                                    ).first()
                if not remoteuser_obj:
                    print_err("RemoteUser obj %s does not exist." % item,quit=True )
                bindhost_obj = models.BindHost(host_id=host_obj.id,remoteuser_id=remoteuser_obj.id)
                session.add(bindhost_obj)


                #for groups this host binds to
                #获取所有的组去关联组
                if source[key].get('groups'):
                    group_objs = session.query(models.HostGroup).filter(models.HostGroup.name.in_(source[key].get('groups') )).all()
                    assert group_objs
                    print('groups:', group_objs)
                    bindhost_obj.groups = group_objs
                #for user_profiles this host binds to
                if source[key].get('user_profiles'):
                    userprofile_objs = session.query(models.UserProfile).filter(models.UserProfile.username.in_(
                        source[key].get('user_profiles')
                    )).all()
                    assert userprofile_objs
                    print("userprofiles:",userprofile_objs)
                    bindhost_obj.user_profiles = userprofile_objs
                #print(bindhost_obj)
        session.commit()


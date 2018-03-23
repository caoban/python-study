# _*_ coding:utf-8 _*_
import sys

retry_limit = 3
retry_count = 0
account_file = 'account.txt'
lock_file = 'lock.txt'

while retry_count < retry_limit:  # 不超过三次就循环
    username = raw_input('请输入用户名')
    # 输入用户名以后，打开lockfile，检查是否被lock
    lock_check = file(lock_file)
    for line in lock_check.readlines():
        if username in line:
            sys.exit('user is lock' % username)

    password = raw_input('输入密码')
    # 打开账号文件，只读
    f = file(account_file, 'rb')
    # 默认False，用户匹配上了就是True
    match_flag = False

    for line in f.readlines():
        # 读取account.txt文件中的用户和密码，并赋给对应的字段
        user, paswd = line.strip('\n').split()
        # 判断用户和密码是否相等,匹配上了，直接跳出
        if username == user and password == paswd:
            print 'Match', username
            match_flag = True
            break
    f.close()

    if match_flag == False:
        print 'unmatch', username
        retry_count += 1
    else:
        #用户密码输入对了，跳到欢迎界面
        print 'welcome old boy python'
        break

else:
    print 'you account is locked'
    f = file(lock_file, 'ab')
    f.write(username)
    f.close()

# _*_ coding:utf-8 _*_
input_username = raw_input('请输入用户名:')
username = 'suhan'
passwd = '123'
chance = 0
while input_username == username:
    input_passwd = raw_input('请输入密码:')
    if input_passwd == passwd:
        print '登陆成功'
        # f = open('passwd.txt','a')
        # f.write(input_passwd)
        p = open('passwd.txt','r')
        s = p.read()
        p.close()
        if s == input_passwd:
            print '密码正确'
        else:
            print '密码错误'
        print s
        break
    else:
        print '登陆失败'
        chance = chance+1
        continue
else:
    print '用户名错误'

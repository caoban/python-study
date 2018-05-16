# -*- coding: utf-8 -*-
__Author__ = "suhan"
__Date__ = '2018/05/14/20:46'

"""
用户注册gitlab和发送邮件给用户
"""

import requests
import random
import string

url = 'http://gitlab.wuxingdev.cn'
token = 'zsm44PTux_r65p5rbTBG'

#拼接创建用户的url
CreateUserUrl = "%s/api/v3/users" %url
EmailExample = "guanaitong.com"

while True:
    # 输入需要创建的用户信息，密码是随机生成的
    name = input("请输入中文用户名:")
    email = input("请输入邮箱地址:")
    username = email.strip().split("@guanaitong.com")[0]
    password = "".join(random.sample(['A', 'b', '5', 'D', 'e', '7', 'g', 'h', '2', 'j', 'q'], 8))
    # print("输入信息为：\n中文用户名:%s\n邮箱地址:%s\n登录username:%s\n" %(name,email,username))

    if email.strip().split("@")[1] != EmailExample:
        print("邮箱格式不对!%s" %email)
        continue
    else:
        UserData = {'email': email, 'username': username, 'name': name, 'password': password, 'private_token': token}
        response = requests.post(CreateUserUrl, data=UserData)
        if response.status_code == 201:
            email2 = "han.su@guanaitong.com"
            data2 = {'tos':email2,'subject':"Gitlab密码",'content':"gitlab地址：" + url + " 登录用户：" + username + " 登录邮箱：" + email + " 密码：" + password }
            EmailUrl = "http://notice.ops.gat/sender/mail/"
            SendEmailResponse = requests.post(EmailUrl,data = data2)
            print("用户创建成功，并将密码发给用户")
            input("请输入任意字符退出:")
            break
        else:
            print("创建失败，请确认邮箱和用户名是否已存在")
            continue



#http://python-gitlab.readthedocs.io/en/stable/api-usage.html

#xurl = "%s/api/v3/projects?private_token=%s" %(url,token)
# x = requests.get(xurl)
# #两种都可以
# content = x.json()
# content2 = x.text
# print(content)

# -*- coding: utf-8 -*-
__Author__ = "suhan"
__Date__ = '2018/05/14/20:46'

"""
用户注册gitlab和发送邮件给用户
"""

import requests
import gitlab
import random
import string

url = 'http://gitlab.wuxingdev.cn'
token = 'zsm44PTux_r65p5rbTBG'

#登录
gl = gitlab.Gitlab(url,private_token='token')

#输入用户信息
name = input("请输入中文用户名:")
email = input("请输入邮箱地址:")
username = email.strip().split("@guanaitong.com")[0]
password = "".join(random.sample(['A','b','5','D','e','7','g','h','2','j','q'], 8))

print("name:%s\nemail:%s\nusername:%s\n" %(name,email,username))

UserData = {'email':email, 'username':username, 'name':name, 'password':password}
user = gl.users.create(UserData)





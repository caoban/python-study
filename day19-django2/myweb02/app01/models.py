from django.db import models

# Create your models here.


#数据库有变化的时候，执行这2个操作
# python3 manage.py makemigrations
# python3 manage.py migrate



#models.py这个文件名不能改变，只能是叫这个名字

class UserInfo(models.Model):
    #id列，自增，主键
    #用户名列，字符串类型，指定长度
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    #新增一列，默认是可以为空。  如果不写这个，在执行初始化的时候，需要选择输入默认值
    #如果取消，注销掉，重新设置就可以了
    #gender = models.CharField(max_length=60, null=True)
    test = models.EmailField(max_length=19,null=True)


# def suhan(x,*args):
#     print(x)
#     print(args)
#
# #suhan(1,2,3,4,5,66)
#
# suhan(*[1,2,3,4,5,99])#  args=tuple([1,2,3,4,5])  当做一个元祖输出



#**kwargs 把N个关键字参数，转换成字典的方式
# def suhan2(**kwargs):
#     print(kwargs)
#     print(kwargs['name'])
#     print(kwargs['age'])
#     print(kwargs['sex'])
#
# suhan2(name='alex',age=8,sex='F')


# suhan2(**{'name':'alex','age':8})

def logger(source):
    print("from %s" % source)

def suhan3(name,age=20,**kwargs):
    print(name)
    print(age)
    print(kwargs)
    logger("SUHAN")
suhan3('alex',222,sex='m',hobby='teshila')







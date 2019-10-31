#_*_coding:utf-8_*_
'''
@author:suhan
'''
#from file import demo




# def login(username):
#     if username == 'suhan':
#         return '登陆成功'
#     else:
#         return '登陆失败'
#
# def detail(user):
#     print '奖励1000元'
#
# if __name__ == '__main__':
#     user = raw_input('请输入用户：')
#     res = login(user)
#     if res == '登陆成功':
#         detail(user)
#     else:
#         print '没奖金了'
#

# def show(*arg):
#     for item in arg:
#         print item
#
# show('suhan','xiaolei','subei')

# def show(**args):
#     for item in args.items():
#         print item
# user_dict = {'k1':123,'k2':234}
# show(**user_dict)



''''
print range(10)
for item in xrange(10):
    print item


def Alexreadlines():
    seek = 0
    while True:
        with open('D:/tmp/tmp.txt','r')as f:
            f.seek(seek)
            data = f.readline()
            if data:
                seek = f.tell()
                yield data
            else:
                return

for item in Alexreadlines():
    print item
'''

#python3 是print(xxx) 2是print xxx
#
# tmp = None
# if 1 > 3 :
#     tmp = 'gt'
# else:
#     tmp = 'lt'
#
# print(tmp)
# #三元运算
# result = 'gt' if 1 > 3 else 'lt'
# print(result)
#
# a = lambda x,y:x+y
# print(a(4,10))






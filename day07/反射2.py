
def bulk(self):
    print("%s is yelling..." %self.name)

class Dog(object):

    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating....%s" %(self.name,food))

d = Dog("xiaobai")
choice = input(">>:").strip()

#getattr 根据字符串去获取obj对象里的对应的方法的内存地址
#hasattr 是判断是有输入的方法 或者变量什么的
if hasattr(d,choice):
    getattr(d,choice)

else:
    #setattr 是塞一个函数或者值进去
    setattr(d,choice,bulk)
    func = getattr(d,choice)
    func(d)

    # #因为我输入的 talk，相当于是把 bulk函数地址赋给了talk。
    # # 正常调用函数，传一个参数进去
    # d.talk(d)


def bulk(self):
    print("%s is yelling..." %self.name)

class Dog(object):

    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating....%s" %(self.name,food))


d = Dog("xiaobai")
choice = input(">>:").strip()

#hasattr 判断一个对象里面是否有对应的字符串的方法
print(hasattr(d,choice))

#getattr 根据字符串去获取obj对象里的对应的方法的内存地址
if hasattr(d,choice):
    func = getattr(d,choice)
    func("hei")
else:
    #动态装入一个方法
    #类外面的方法，假装是类里面的方法去使用。  bulk是类外面的，假装在类里面叫talk
    setattr(d,choice,bulk)
    d.talk(d)


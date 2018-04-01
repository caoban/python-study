#定义一个类。新式写法
class Dog(object):
    #构造函数
    def __init__(self,name):
        self.name = name

    @staticmethod #实际上跟类没什么关系。只是一个单纯的函数。名义上在类的下面。类管不了里面的东西。self不引用了。
    def eat(self,food):
        print("%s is eating %s" %(self.name,food))

d = Dog("陈荣华")
d.eat("包子")



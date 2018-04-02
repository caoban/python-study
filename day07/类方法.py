#定义一个类。新式写法
class Dog(object):

    #构造函数
    def __init__(self,name):
        self.name = name
        self.__food = None

    @property
    def eat(self):
        print("%s is eating %s" %(self.name,self.__food))

    @eat.setter
    def eat(self,food):
        print("eat setter ... %s" %food)
        #这个就相当于是保存了。
        self.__food = food

    @eat.deleter
    def eat(self):
        #删除 私有变量
        del self.__food
        print("删除完了")

    def __str__(self):
        return "obj:%s" %self.name

#print(Dog.__dict__)
d = Dog("chen")
print(d)
#print(d.__dict__)

# d.eat
# d.eat = "baozi"
# d.eat
#
# del d.eat
# d.eat



#class People: #经典类
class People(object): #新式类

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating 。。。" % self.name)

    def talk(self):
        print("%s is talking...." % self.name)

    def sleep(self):
        print("%s is sleeping....." % self.name)

class Relation(object):
    def make_friends(self,obj):
        print("%s is making friends with %s" %(self.name,obj.name))



class Man(People,Relation):

    #重构父类的构造函数，加入一个新的money参数
    #父类的所有参数，都要写一遍。因为调用的的时候是调用子类的构造函数，不是直接调用父类的构造函数了
    def __init__(self,name,age,money):
        #还需要父类中的方法，就再把参数传给父类。
        #People.__init__(self,name,age) #经典类的写法
        super(Man,self).__init__(name,age) #新式类的写法
        self.money = money
        #print("一出生就有钱%s" %self.money)

    def piao(self):
        print("%s is piaoing....20s" % self.name)

    def sleep(self):
        People.sleep(self)
        print("man is sleeping")

class Woman(People,Relation):
    def get_birth(self):
        print("%s is born a baby..." % self.name)


m1 = Man("suhan",22,100)
#调用父类的方法
m1.eat()



# #调用继承后的类的方法
# m1.piao()
# # #重构父类的方法。 既能打印出来父类的方法，还有自己加的方法
# m1.sleep()

w1 = Woman("lili",22)
# w1.get_birth()
# #一个子类，不能调用另一个子类的方法
# w1.piao()


m1.make_friends(w1)
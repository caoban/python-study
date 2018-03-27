
class Dog:
    #这个函数是传名字用的
    def __init__(self,name):
        self.name = name

    def bulk(self):
        print("%s wang wang wang" %self.name)

#传实参
d1 = Dog("陈1")
d2 = Dog("陈2")
d3 = Dog("陈3")

#调用里面的方法
d1.bulk()
d2.bulk()
d3.bulk()


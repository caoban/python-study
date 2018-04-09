
class MyType(type):
    def __init__(self, what, bases=None, dict=None):
        print("--MyType init---")
        super(MyType,self).__init__(what, bases, dict)

    def __call__(self, *args, **kwargs):
        print("---MyType call---")
        obj = self.__new__(self, *args, **kwargs)
        self.__init__(obj, *args, **kwargs)

class Foo(object):
    #__metaclass__ = MyType

    def __init__(self,name):
        self.name = name
        print("Foo ----init__")

    def __new__(cls, *args, **kwargs):
        print("Foo ---new---")
        return object.__new__(cls) #继承父类的__new__ 方法，cls是把自己传过去

#第一阶段:从上到下执行代码，创建Foo类
#第二阶段:通过Foo类创建obj对象
obj = Foo('alex')
print(obj.name)

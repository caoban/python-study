class Foo(object):
    def __init__(self):
        #这个就是不用传进去的实例变量
        self.data = {}

    def __getitem__(self, key):
        print('__getitem__',key)
        return self.data.get(key)

    def __setitem__(self, key, value):
        print('__setitem__',key,value)
        self.data[key] = value

    def __delitem__(self, key):
        print('__delitem__',key)

obj = Foo()
obj['name'] = 'alex'
print(obj.data['name'])
print(obj.data)

#触发删除的操作，那个方法里面可以写上自己想做的事情
del obj["name"]

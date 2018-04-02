#
# class Foo(object):
#     def __init__(self,name):
#         self.name = name
#
# f = Foo("alex")
# print(type(f))
# print(type(Foo))

def func(self):
    print("hello alex")

Foo = type('Foo',(),{'talk':func})
print(type(Foo))

f = Foo()
f.talk()

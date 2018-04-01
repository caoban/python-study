
class Animal:
    def __init__(self,name):
        self.name = name

    def talk(self):
        pass

    #没有 self
    @staticmethod
    def animal_talk(obj):
        obj.talk()

class Cat(Animal):
    def talk(self):
        print("Meow!")

class Dog(Animal):
    def talk(self):
        print("woof,woof!")

d = Dog("陈荣华")
# d.talk()
c = Cat("徐良为")
# c.talk()

#多态。同一个接口，传入不同的对象
Animal.animal_talk(c)
Animal.animal_talk(d)

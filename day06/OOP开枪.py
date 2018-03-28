class Role(object):
    n = 123 #类变量
    a_list = []
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        self.name = name    #实例变量
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value
        self.money = money

    def show_lifevalue(self):
        print("life_value:%s" %self.__life_value)

    def __del__(self):
        pass #print("%s 彻底死了。。。。")

    def shot(self):
        print("shooting。。。。。")

    def got_shot(self):
        print("an。。。,i am got shot")
    def buy_gun(self, gun_name):
        print("%s just buy gun %s" %(self.name,gun_name))

role1 = Role('Alex','police','AK47') #生成一个角色
role2 = Role('jack','terrorist','B22') #生成一个角色

print(role1.show_lifevalue())



    #可以改类变量
role1.n = ("改类变量")

#     #role1实例中没有改
# print(role1.n)
#     #role2 实例中没有改
# print(role2.n)

# Role.n = "ABC"
# print(role1.n,role2.n)
#
# role1.a_list.append("from r1")
# role2.a_list.append("from r2")
#
# print("role1 list: %s" %role1.a_list)
# print("role2 list: %s" %role2.a_list)
# print("Role类 list: %s" %Role.a_list)




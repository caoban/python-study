class Role(object):
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):
        print("shooting。。。。。")

    def got_shot(self):
        print("an。。。,i am got shot")
    def buy_gun(self, gun_name):
        print("%s just buy gun %s" %(self.name,gun_name))

role1 = Role('Alex','police','AK47') #生成一个角色
role2 = Role('jack','terrorist','B22') #生成一个角色

role1.buy_gun("AK47")
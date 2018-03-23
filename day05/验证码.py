import random

checkcode = ''

for i in range(4):
    current = random.randrange(0,4)
    #设置条件，一致就出字母，不一致就出数字
    if current == i:
        tmp = chr(random.randint(65,90))
    else:
        tmp=random.randint(0,9)

    checkcode+=str(tmp)
print(checkcode)
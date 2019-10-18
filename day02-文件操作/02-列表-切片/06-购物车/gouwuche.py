#_*_ coding:utf-8 _*_

#不要眼高手低，基本知识点记住。

if __name__ == '__main__':

    #定义一个列表，存放已经购买的商品。列表和字典这种在循环里面或者夸函数好像是可以保持数据的？变量肯定是不行的。
    choseHave = []

    #定义一个值，死循环的时候用，改变这个值就可以跳出循环了。
    limit = 0

    #定义一个字典dict，存放商品数据
    goods = {
        'book': 300,
        'yifu': 500,
        'zuozi': 400,
        'coffee': 200
    }

    #输入的金额，input在python3中输入值默认都变成str类型
    wallet = int(input("请输入总金额："))

    #循环打印字典中的值
    for i in goods:
        print(i,goods[i])

    #循环，改变这个值可以跳出循环。注意break和connitue的区别
    while limit == 0:
        chose = input("请输入你选择的商品:")

        if chose in goods:
            wallet = wallet - int(goods[chose])
            print("剩余钱为：",wallet)

            if wallet < 0:
                wallet = wallet + int(goods[chose])
                print("余额不足",wallet)
                continue

            #已买的商品追加保存
            choseHave.append(chose)
            print("已经购买的商品为：",choseHave)

        else:
            print("输入正确的商品")
            continue

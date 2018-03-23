#_*_coding:utf-8_*_
wallet = input('请输入总金额：')
limit = 0
goods = {
    'iphone':5000,
    'coffe':30,
    'shoes':300,
    't-Thits':200
}
for i in goods:
    print i, goods[i]
while limit == 0:
    choose = raw_input('请选择你的商品：')
    if choose in goods:
        wallet = wallet - goods[choose]
        for i in goods:
            print i, goods[i]
        if wallet < 0:
            print '当前余额不足:',wallet
            wallet = wallet + goods[choose]
            continue
        else:
            print '当前余额:',wallet
        continue






#_*_ coding:utf-8 _*_

if __name__ == '__main__':
    #定义一个列表list。下标从0开始算
    name = [1, 2, 3, 4, 5, 6, 2, 3, 2, 4]
    #定义初始位置
    firstPos = 0

    # print(name.count(2))
    # print(type(name.count(2)))

    #rang(10) 标识0-9 10个数字
    for i in range(name.count(2)):
        #定义一个切片，从firstPos到最后。顾头不顾尾，头的字符算，尾部下标的就不算在切片里了。
        newName = name[firstPos:]

        #切片中的第一个字符2的下标是多少,定义下一段切片
        nextPos = newName.index(2) + 1

        #firstPos 是切初始的那个列表的，所以数字是在变大的
        poS = newName.index(2) + firstPos
        print("pos",poS)

        #第一个位置，加上算出来的新的列表中的位置
        firstPos = firstPos + nextPos

#_*_ coding:utf-8 _*_

# index()函数的完整语法是这样的：
# str.index(str, beg=0, end=len(string))
# str – 指定检索的字符串
# beg – 开始索引，默认为0。
# end – 结束索引，默认为字符串的长度。

#主要是index的用法
if __name__ == '__main__':

    #定义一个列表，列表下标从0开始计算
    name = [1, 2, 3, 4, 5, 6, 2, 3, 2, 4]

    firstPos = 0
    for i in range(name.count(2)):
        if firstPos == 0:
            firstPos = name.index(2)
        else:

            #2表示字符串，从firstPos+1标识开始，默认到字符串结束
            firstPos = name.index(2,firstPos+1)

        print(firstPos)

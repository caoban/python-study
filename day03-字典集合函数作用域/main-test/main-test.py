#_*_coding:utf-8_*_

import sys,os

#获取当前文件的上级目录路径
lujin = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

#insert插入指定位置，append是追加到最后
sys.path.insert(0, lujin)
print("打印当前的path：", sys.path)

#file包和本文件不在同级，需要path中添加路径，才能找到。
#导入file包中的demo模块，然后就可以使用demo.foo() 引用demo模块中的内容
from file import demo

if __name__ == '__main__':

    print("打印当前的path：",sys.path)
    print("当前文件的绝对路径：",os.path.realpath(__file__))
    print("当前文件的目录路径：",os.path.dirname(os.path.realpath(__file__)))
    print("获取当前文件的上级目录路径：",os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


    demo.foo("suhan2")



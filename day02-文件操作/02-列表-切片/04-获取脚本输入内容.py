#_*_ conding:utf-8 _*_

import sys

if __name__ == '__main__':

    #sys.argv 是命令行执行时，输入的所有内容。以列表的形式

    print("脚本名",sys.argv[0])

    #
    for i in range(1,len(sys.argv)):
        print(i,sys.argv[i])

    print(sys.argv)

####结果#####
# python3 04-获取脚本输入内容.py 是发的 ss gg
# 脚本名 04-获取脚本输入内容.py
# 1 是发的
# 2 ss
# 3 gg
# ['04-获取脚本输入内容.py', '是发的', 'ss', 'gg']
#



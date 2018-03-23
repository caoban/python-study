#_*_coding:utf-8_*_
import sys
import pexpect
import commands
#print "脚本名:",sys.argv[0]
#for i in range(1,len(sys.argv)):
#    print '参数:',i,sys.argv[i]

for i in range(1,len(sys.argv)):
    if sys.argv[i] == "--bak":
        print '1111111'
        commands.getstatusoutput('cp -rp argv_replace.txt argv_replace.txt.bak')
    else:
        print '22222222'
        with open('argv_replace.txt','rw+') as f:
            t = f.read()
            t = t.replace('AAAA','123')
            f.seek(0,0) #跳到开头，不挑的话就是在尾部加上改后的内容，空格也算是一个位置
            f.write(t)



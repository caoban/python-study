#_*_ coding:utf-8 _*_

#不要眼高手低，有写代码的机会不容易，第五次学python

import sys
#commands在python3被取消了
import subprocess

#主函数
if __name__ == '__main__':
    #[1]表示下标为1的输入参数，就是第二个参数。[0]指脚本名称
    print("sys.argv[1]:",sys.argv[1])

    #for循环从1开始
    for i in range(1,len(sys.argv)):
        #根据输入做备份操作
        if sys.argv[i] == "--bak":
            #执行shell命令
            subprocess.getstatusoutput("cp -rp file.txt file.bak")

            #打开文件，这种不用关闭文件了
            with open(file="file.txt",mode="a+") as f:
                print(f.tell())
                print("开始")
                print(f.readlines())

                #循环替换，并且开始写文件
                for lines in f:
                    print("指针位置：", f.tell())
                    print("lines:",lines)
                    linesReplace=lines.replace("suhan","00000")
                    print(linesReplace)

                    #写到另外一个文件中时可以的，还是写在源文件，这个没成功
                    f.write(linesReplace)


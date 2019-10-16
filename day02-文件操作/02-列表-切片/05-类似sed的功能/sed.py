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
            subprocess.getstatusoutput("cp -rp file file.bak")

            #打开文件，这种不用关闭文件了
            with open("file",mode="w+",encoding="utf-8") as f:
                print("指针位置：", f.tell())
                for lines in f:
                    print("指针位置：", f.tell())
                    linesReplace=lines.replace("suhan","00000")
                    print(linesReplace)
                    f.write(linesReplace)


                # #打印文件指针所在的位置。mode是r的时候tell是0，mode是a+时tell是在文件最后
                # print("指针位置：",f.tell())
                # f.seek(0, 0)
                # t = f.readline()
                # t = t.replace("suhan","00000")
                # print(t)
                # f.seek(0, 0)
                # f.write(t)


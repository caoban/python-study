#_*_ coding:utf-8 _*_

#基础打捞，看基础的知识，写练习，不要眼高手低。

import sys

#主函数
if __name__ == '__main__':

    #先定义需要的字段
    retry_limt = 3
    retry_count = 0
    account_file = "account.txt"
    lock_file = "lock.txt"

    #死循环判断，if只能判断一次
    while retry_count < retry_limt:

        # 用户输入信息
        user_name_in = input("user name:")
        passwd_in = input("password:")


        #判断用户是否存在被锁的文件中。mode使用a+ 打开不了不知道是为什么
        with open(lock_file,mode="r",encoding="utf-8") as lockFile:
            for lockUserInfo in lockFile:
                if len(lockUserInfo) != 0:
                    lockUserName = lockUserInfo.strip("\n").split(",")[0]
                    if user_name_in == lockUserName:
                        print("此用户已经被锁")
                        exit(1)


        #accountFile 是个对象
        with open(account_file,mode='r',encoding="utf-8") as accountFile:
            for account in accountFile:
                #从文件中读取信息并去掉行尾的换行符并以逗号做切割，可以同时按位置赋值给2个值
                account_name,account_pwd=account.strip("\n").split(",")

                if user_name_in == account_name and passwd_in == account_pwd:
                    print("登录成功")
                    exit(0)



        #这个不能写在打开account_file里面，不然失败了会有一行数据就打印一次登录失败
        print("登录失败，请重新登录")

        #retry_count += 1 等于retry_count = retry_count + 1
        retry_count += 1

        if retry_count >= 3:
            #一般读写追加使用a+就够了
            with open(lock_file,mode="a+",encoding="utf-8") as lockFile2:
                lock_user = "\n" + user_name_in + "," + passwd_in
                print("lock_user:",lock_user)
                lockFile2.write(lock_user)

            print("登录尝试超过3次")
            exit(1)


#验证 线程之间，列表和字典的数据是共享的。

from multiprocessing import Process, Manager
import os

def f(dict2,list2,i):
    dict2[os.getpid()] = os.getpid()
    list2.append(os.getpid())
    print("进程：%s %s" %(i,list2))

if __name__ == '__main__':
    with Manager() as manager:
        dict1 = manager.dict() #生成一个字典可以在多个进程之间共享和传递
        list1 = manager.list(range(5)) #生成一个列表，可以在多个进程之间共享和传递

        #生成一个空列表
        p_list = []
        #启动 10个进程
        for i in range(10):
            p = Process(target=f,args=(dict1,list1,i))
            p.start()
            #进程对象放到一个列表里面，后面用
            p_list.append(p)

        #等待所有的结果
        for res in p_list:
            res.join()

        print(dict1)
        print(list1)





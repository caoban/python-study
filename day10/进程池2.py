from multiprocessing import Process, Pool, freeze_support

import greenlet

import time
import os

def FOO(i):
    time.sleep(2)
    print("in process", os.getpid())
    return i + 100

def Bar(arg):
    #这个arg 好像就是 Func函数的 return的数值
    #os.getpid 看看父进程还是子进程调用的这个函数
    print('---->exec done:', arg,os.getpid())


if __name__ == '__main__':
    #允许进程池同时放入5个进程
    pool = Pool(processes=5)

    print("主进程",os.getpid())

    for i in range(6):
        #callback回调。只有执行完func的函数，才会再执行callback的函数。
        pool.apply_async(func=FOO, args=(i,), callback=Bar)

        #pool.apply(func=FOO, args=(i,)) #串行
        #pool.apply_async(func=FOO, args=(i,)) #并行

    print('end')
    pool.close()
    #进程池中的进程执行完毕后再关闭，如果注释，那么程序直接关闭。
    pool.join()




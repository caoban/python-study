
from multiprocessing import Process, Lock

def f(l,i):
    #加锁
    l.acquire()
    print("hello %s" %i)
    #释放锁
    l.release()


if __name__ == '__main__':
    #创建一个锁实例
    lock = Lock()
    #10个进程
    for num in range(101):
        Process(target=f,args=(lock,num,)).start()


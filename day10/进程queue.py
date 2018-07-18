from multiprocessing import Process, Queue

def f(qq):
    #子进程里面 队列 put一个信息。 不是子线程
    qq.put([42, None, 'hello'])

if __name__ == '__main__':
    #定义一个队列的对象  子进程的是 queue.Queue
    duilie = Queue()
    #启动一个进程，不是线程
    p = Process(target=f,args=(duilie,))
    p.start()
    # 队列的对象 get
    print(duilie.get())
    #等都执行完
    p.join()

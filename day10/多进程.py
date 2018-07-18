import multiprocessing
import time,threading

def thread_run():
    #获取当前的线程号
    print(threading.get_ident())

#多进程里面再启动一个线程
def run(name):
    time.sleep(2)
    print("hello", name)
    p2 = threading.Thread(target=thread_run,)
    p2.start()

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=run, args=('suhan %s' %i,))
        p.start()

    #p.join()



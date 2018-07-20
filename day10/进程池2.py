from multiprocessing import Process, Pool, freeze_support

import time
import os

def FOO(i):
    time.sleep(2)
    print("in process", os.getpid())
    return i + 100

if __name__ == '__main__':
    #允许进程池同时放入5个进程
    pool = Pool(processes=5)

    for i in range(6):
        pool.apply(func=FOO, args=(i,))

    print('end')
    pool.close()
    #pool.join()




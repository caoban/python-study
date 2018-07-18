from multiprocessing import Process
import os

def info(title):
    print(title)
    #模块名
    print('module_name:', __name__)

    #getppid就是父进程的ID
    print('parent process:', os.getppid())
    #getpid 就是自己的ID
    print('process id:', os.getpid())
    print("\n")

def f(name):
    info('\033[31;1mfunction f\033[0m')
    print('hello', name)

if __name__ == '__main__':
    #主进程里面调用 info 打印进程号
    info('\033[31;1m main process f\033[0m')

    #子进程里面调用info 打印进程号
    p = Process(target=f,args=('bob',))
    p.start()
    p.join()















import threading,time


#继承threading.Thread
class MyThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num

    #类里面的这个函数的名称一定要是run
    def run(self):
        print("running task", self.num)

if  __name__ == '__main__':
    t1 = MyThread("11")
    t2 = MyThread("22")
    t1.start()
    t2.start()



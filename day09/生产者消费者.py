import threading,time,queue

q = queue.Queue(maxsize=10)

#生产者
def  Producer(name):
    count = 1
    while True:
        q.put("骨头%s" % count)
        print("生产了骨头",count)
        count +=1
        time.sleep(0.1)

#消费者
def Consumer(name):
    while True:
        print("[%s] 取到[%s] 并且吃了它..." %(name,q.get()))
        time.sleep(1)

#使用多线程  不是进程。 for 循环来启动多个线程
p = threading.Thread(target=Producer,args=("Alex",))
c = threading.Thread(target=Consumer,args=("suhan",))
c1 = threading.Thread(target=Consumer,args=("王森",))

#启动
p.start()
c.start()
c1.start()





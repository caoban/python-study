import threading,time

#这个函数名叫什么都行
def run2(n):
    lock.acquire()
    global num
    num += 1
    lock.release()



lock = threading.Lock()
num = 0

start_time = time.time()
for i in range(10):
    t = threading.Thread(target=run2,args=("t-%s" %i ,))
    t.setDaemon(True) #把子进程设置成守护进程。相当于子进程后台执行。
    t.start()

time.sleep(2)
print(num)

print("-----all threads has finished" , threading.current_thread(),threading.active_count())
print("cost:" ,time.time() - start_time)





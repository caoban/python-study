import threading,time

#这个函数名叫什么都行
def run2(n):
    print("task",n)
    time.sleep(2)

start_time = time.time()
t_objs  = []

for i in range(10):
    t = threading.Thread(target=run2,args=("t-%s" %i ,))
    t.start()
    t_objs.append(t)

for t in t_objs:
    t.join()

print("-----all threads has finished")
print("cost:" ,time.time() - start_time)

#t2 = threading.Thread(target=run2,args=("22",))

# t1.start()
# t2.start()



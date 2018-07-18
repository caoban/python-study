import queue

q = queue.PriorityQueue()

q.put((-1,"chengronghua"))
q.put((3,"suhan"))
q.put((10,"subei"))
q.put((6,"xiaolei"))

print(q.get())
print(q.get())
print(q.get())
print(q.get())



# #后进先出
# q = queue.LifoQueue()
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())
# print(q.get())
# print(q.get())




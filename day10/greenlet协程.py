
from greenlet import greenlet


def test1():
    print(12)
    gr2.switch() #手动切换到第二个协程
    print(34)
    gr2.switch()
def test2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(test1) #启动一个协程
gr2 = greenlet(test2) #启动第二个协程
gr1.switch() #手动切换到下一个协程
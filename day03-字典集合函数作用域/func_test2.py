
import time
def log():
    #最后按照定义的时间格式显示时间 %X 表示时分秒
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)

    with open('a.txt','a+') as f:
        f.write('%s write 1\n' %time_current)

def func1():
     """func1"""
     print('11111111')
     log()

def func2():
    """func2"""
    print('22222222')
    log()

def func3():
    """func3"""
    print('333333333')
    log()

func1()
func2()
func3()













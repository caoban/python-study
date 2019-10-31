
#函数
def func1():
    """test 1"""
    print('in the func1')
    return 0

#过程
def func2():
    """test 2"""
    print('in the func2')

x = func1()
y = func2()

print('from func1 return is %s' %x)
print('from func2 return is %s' %y)


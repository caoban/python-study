
def suhan():
    print('in the test1')

def suhan2():
    print('in the test2')
    return 0

def suhan3():
    print('in the test3')
    return 1,'hello',['alex','wupeiqi'],{'name':'alex'}

def suhan4():
    return suhan3

def suhan5():
    return suhan3()

n = suhan4()
print(n)

n2 = suhan5()
print(n2)



# x = suhan()
# y = suhan2()
# z = suhan3()
# print(x)
# print(y)
# print(z)




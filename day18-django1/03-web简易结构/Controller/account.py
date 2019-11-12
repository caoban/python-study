

#定义2个函数，根据输入的path不同执行不同的函数
def handle_index():

    #return 是把函数的结果返回给调用的地方。
    with open('View/index.html',mode='rb') as f:
        data = f.read()

        #替换vim/index.html中的数据，并且展示出来
        #python3 传输数据的时候使用的是 byte类型，所以要加b
        data = data.replace(b'@uuuuu','苏晗'.encode('utf-8'))
        return [data,]

def hanle_date():
    return ['<h1>date</h1>'.encode('utf-8'),]



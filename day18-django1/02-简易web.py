
from wsgiref.simple_server import make_server

#定义2个函数，根据输入的path不同执行不同的函数
def handle_index():
    print("index start")
    #return 是把函数的结果返回给调用的地方。
    return ['<h1>index</h1>'.encode('utf-8'),]

def hanle_date():
    return ['<h1>date</h1>'.encode('utf-8'),]

#path和函数的对应关系，只是一个函数地址，不用加()
URL_DICT = {
    "/index": handle_index,
    "/date": hanle_date,
}

#主要执行函数
def RunServer(environ, start_response):
    #environ客户发来的所有数据
    #start_response 封装要返回给用户的数据，响应头状态
    start_response('200 ok', [('Content-Type','text/html')])
    current_url = environ['PATH_INFO']

    #默认值，如果函数
    func = None
    if current_url in URL_DICT:
        func = URL_DICT[current_url]

    if func:
        #return 是吧结果返回给浏览器，这个return不能少。少了会报错
        return func()
    else:
        return ['<h1>404</h1>'.encode('utf-8'),]

if __name__ == '__main__':

    #绑定地址和端口和执行的函数
    httpd = make_server('',8000,RunServer)
    print("Server HTTP in port 8000")

    httpd.serve_forever()

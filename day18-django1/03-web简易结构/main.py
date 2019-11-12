
from wsgiref.simple_server import make_server

#把处理逻辑的函数都放在Controller目录下面
from Controller import account


#path和函数的对应关系，只是一个函数地址，不用加()
URL_DICT = {
    "/index": account.handle_index,
    "/date": account.hanle_date,
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

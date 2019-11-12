from django.shortcuts import render,redirect,HttpResponse

# Create your views here.


USER_DICT = {
    '1' : {'name':'suhan','email':'root@11.com'},
    '2': {'name': 'suhan', 'email': 'root@11.com'},
    '3': {'name': 'suhan', 'email': 'root@11.com'},
    '4': {'name': 'suhan', 'email': 'root@11.com'},
}



#urls写对应的url和视图函数，返回一个字符串
def index(request):
    return render(request,'index.html',{'user_dict':USER_DICT})





#request只是形参，表示请求，可以换成别的字符串
def login(request):
    if request.method == "GET":
        #login.html 这个因为settings.py中写了静态文件的路径，所以可以找到
        return render(request, "login.html")

    #判断提交的方式是什么类型的
    elif request.method == "POST":
        # #获取POST方式提交过来的数据，通过name来获取的
        # v = request.POST.get('gender')
        # print(v)
        #
        # #getlist 是获取多个值，复选框提交过来的值，列表的形式展示
        # aihao = request.POST.getlist('favor')
        # print(aihao)
        #

        v = request.POST.get('fafafa')
        print(v)

        tupian = request.FILES.get('fafafa')
        # tupian打印出来是个名称，type(tupian) 是一个对象，tupian.name也是名称
        print(tupian,type(tupian),tupian.name)

        #加一级文件目录
        import os
        file_path = os.path.join('upload', tupian.name)

        #打开一个同名的新文件，tupian.chunks()就是上传的图片的内容
        f = open(file_path, mode='wb')
        #写到同名的文件中，就算是保存下来了
        for i in tupian.chunks():
            f.write(i)
        f.close()

        return redirect('/index/')

    else:
        #PUT,DELETE等其他的方法。
        return redirect('/login/')



#导入模块
from django.views import View

#cbv的写法，定义一个类
class Home(View):

    #不管method是get还是post，都会执行dispatch方法。
    #所以可以在这边添加一些操作
    def dispatch(self, request, *args, **kwargs):
        #调用父类中的dispatch
        print('before')
        result = super(Home,self).dispatch(request, *args, **kwargs)
        print('after')
        return result


    #method是get的时候走这个
    def get(self,request):
        print(request.method)
        return render(request, 'home.html')

    #method是post的时候走这个
    def post(self,request):
        print(request.method,"post")
        return render(request, 'home.html')






'''

#request只是形参，表示请求，可以换成别的字符串
def login(request):
    if request.method == "GET":
        #login.html 这个因为settings.py中写了静态文件的路径，所以可以找到
        return render(request, "login.html")

    #判断提交的方式是什么类型的
    elif request.method == "POST":
        #获取POST方式提交过来的数据，通过name来获取的
        u = request.POST.get('user')
        p = request.POST.get('user')

        if u == '123' and p == '123':
            return redirect('/index/')
        #如果用户名和密码错误了也是调到登录界面
        else:
            return redirect('/login/')

    else:
        #PUT,DELETE等其他的方法。
        return redirect('/login/') 
'''
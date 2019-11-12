from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.
from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("<h1>hello cmdb</h1>")



def login(request):
    #先给个默认值
    error_msg = ""

    #获取提交的方法是get还是post，进行不同的操作
    if request.method == "POST":

        #打印请求的数据
        #print(request.POST)

        #根据input框中的name 值来获取提交的值，None表示默认值
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)

        #用户名和密码判断
        if user == "123" and pwd == "sss":
            #去跳转
            return redirect("https://www.baidu.com")

        else:
            error_msg = "用户名或密码错误"

    else:
        print("提交的方法错误")

    #{'error_msg_html':error_msg} 是字典的形式，赋值给页面上面的等待填充的地方
    return render(request,'login.html',{'error_msg_html':error_msg})


USER_LIST = [
    {'username':'alex','email':'sss@126.com','gender':'男'},
    {'username':'alex2', 'email': 'sss@126.com', 'gender': '男'},
    {'username':'alex3', 'email': 'sss@126.com', 'gender': '男'},
]


#定义一个home函数,urls.py中添加一个路由的函数的对应关系
#request就是用户提交过来的信息，像user-agent什么的都在这个里面
def home(request):
    #判断用户提交过来的方式
    if request.method == "POST":
        #获取用户提交的数据
        u = request.POST.get('username')
        e = request.POST.get('email')
        g = request.POST.get('gender')
        temp = {'username': u,'email':e,'gender':g}
        USER_LIST.append(temp)

    #把上面的USER_LIST中的内容到时候带入到模板中
    return render(request,'home.html',{'user_list':USER_LIST})



#下面这个放在这里留存查看
# def login(request):
#     #第一种方法：
#     #with open('templates/login.html', 'r', encoding='utf-8') as f:
#     #    data = f.read()
#     # return HttpResponse(data)
#     #第二种方法：
#     return render(request,'login.html')
#
#


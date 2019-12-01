from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

#urls写对应的url和视图函数，返回一个字符串
#函数和url在urls中对应起来的
def index(request):
    return render(request,'index.html')


#用户信息对应的函数
def user_info(request):
    if request.method == "GET":
        user_list = models.UserInfo.objects.all()
        #print(user_list.query )

        return render(request,'user_info.html',{'user_list':user_list})

    #如果提交方式是POST，
    elif request.method == "POST":
        #POST方式提交数据的时候获取数据。user，pwd是name
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        #models 是模块名，UserInfo是里面的类，objects固定写法，create表示动作
        models.UserInfo.objects.create(username=u,password=p)
        #提交数据后跳转会查看用户信息的界面
        return redirect("/cmdb/user_info/")


#显示用户线下信息函数
def user_detail(request,nid):
    obj = models.UserInfo.objects.filter(id=nid).first()

    #这种取数据，如果nid不存在，就直接程序报错了，不会返回None。需要自己加个try。
    #models.UserInfo.objects.get(id=nid)
    return render(request,'user_detail.html',{'obj':obj})


#删除对应的用户信息的函数
def user_del(request,nid):
    # models 是模块名，UserInfo是里面的类，objects固定写法，filter过滤数据，delete表示动作
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/cmdb/user_info/")


#编辑的时候触发的函数
def user_edit(request,nid):
    if request.method == "GET":
        #根据url中的id，来获取数据。obj里面包含id，name，password等信息
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request,"user_edit.html",{"obj":obj})

    elif request.method == "POST":
        #根据input标签中的name来获取值
        nid = request.POST.get('id')
        u = request.POST.get('username')
        p = request.POST.get('password')

        #models是模块名，UserInfo是里面的类，objects是固定写法，filter是过滤对应的条件，update是更新的意识
        models.UserInfo.objects.filter(id=nid).update(username=u,password=p)
        return redirect("/cmdb/user_info/")



#函数是一般的FBV。 传入类的是CBV
#request只是形参，表示请求，可以换成别的字符串
def login(request):
    if request.method == "GET":
        #login.html 这个因为settings.py中写了静态文件的路径，所以可以找到
        return render(request, "login.html")

    #判断提交的方式是什么类型的
    elif request.method == "POST":
        #user是html标签的名称
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        #根据条件过滤数据库中的信息。写多个表示and 的意识
        #加上.first() 表示获取第一个。不加就获取全部的。
        obj = models.UserInfo.objects.filter(username=u,password=p).first()

        #count = models.UserInfo.objects.filter(username=u,password=p).count()
        #可以根据返回结果是否有值，判断用户名和密码是否正确

        if obj:
            #redirect是跳转到对应的url
            return redirect('/cmdb/index/')

        #return render(request, 'login.html')

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


#导入自己写的数据库模块相关的代码
from app01 import models
def orm(request):

    #创建
    #插入数据的第一种方法：
    #表示在数据中插入一行数据，用户名和密码。
    # models.UserInfo.objects.create(
    #     username='root',
    #     password='123'
    # )

    # #第一种写法的另外一种形式
    # dic = {'username':'suhan2','password':'111'}
    # models.UserInfo.objects.create(**dic)

    # #插入数据的第二种方法
    # obj = models.UserInfo(username='suhan',password='123')
    # obj.save()


    #查询全部
    #result = models.UserInfo.objects.all()
    #result是个QuerySet类型的数据，Django提供的，可以理解为一个列表
    #查询，过滤条件
    # result = models.UserInfo.objects.filter(username='suhan')
    #
    # for row in result:
    #     print(row.id,row.username,row.password)
    #

    #删除


    #删除 id=4的数据
    #models.UserInfo.objects.filter(id='4').delete()
    #删除username='suhan' 的数据
    #models.UserInfo.objects.filter(username='suhan').delete()

    #更新所有的数据中的password='8899'
    models.UserInfo.objects.all().update(password='8899')
    #更新username='suhan2'的数据中的password='0011'
    models.UserInfo.objects.filter(username='suhan2').update(password='0011')

    return HttpResponse('orm')






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
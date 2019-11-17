"""myweb02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#url 中如果使用正则，需要导入这个
from django.urls import re_path

#从app01包中导入views这个模块，这样才能把urls和视图函数对应起来
from app01 import views
# from app01 import v1
# from app02 import v2

from django.conf.urls import url,include
urlpatterns = [
    #路由分发，访问/admin/的就会去，app01目录下url.py中去找对应的路由关系
    path('admin/', include("app01.urls")),
    path('cmdb/', include("app02.urls")),

]



#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#
#     #path('index/', views.index),
#
#     #url和对应的视图函数名称。记得这个url带不带后面的斜杠和from表单中的action保持一致
#     # 给路径起个名称，路径很长的时候就很方便。 form表达中的action也不用经常改了
#     path('login/', views.login),
#     path('loginxxxxxx/', views.login,name='loginx'),
#
#     #cbv的写法。Home是类名，as_view是固定写法
#     path('home/', views.Home.as_view()),
#     path('detail/', views.detail),
#     #使用正则表达式匹配路径。(\d+) 就是函数的传入的参数nid。def detail(request,nid):
#     #re_path(r'detail-(\d+)-(\d+).html', views.detail),
#
#     #(?P<nid>\d+) 这种写法在正则表达那节课讲过的。第一个\d+匹配到的就赋值给nid
#     re_path(r'detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail_id),
#
# ]

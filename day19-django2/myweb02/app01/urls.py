

from django.urls import path,re_path

from app01 import views
urlpatterns = [
    path('login/', views.login),
    path('index/', views.index),
    path('user_info/', views.user_info),
    #使用模板的方式，把正则匹配到的赋值给nid。 这里的正则要使用re_path
    re_path('userdetail-(?P<nid>\d+)/', views.user_detail),
    #删除的时候，在url中把id传进去，对应着删除函数
    re_path('userdel-(?P<nid>\d+)/', views.user_del),
    #编辑的时候，触发对应的函数
    re_path('useredit-(?P<nid>\d+)/', views.user_edit),
    path('orm/', views.orm),

]



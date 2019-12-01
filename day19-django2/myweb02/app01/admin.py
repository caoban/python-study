from django.contrib import admin

# Register your models here.
#这样加上就有后台管理了
from app01 import models
admin.site.register(models.UserInfo)

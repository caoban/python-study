from django.db import models

# Create your models here.

#业务线
class Business(models.Model):
    #默认有个id列
    caption =  models.CharField(max_length=32)
    #null=True 表示可以为空，
    code = models.CharField(max_length=32,null=True,default="SA")


#主机
class Host(models.Model):
    # 自己不写主键的话，会自动创建自增的主键。primary_key=True 表示主键。 主键也是个索引
    nid = models.AutoField(primary_key=True)
    # CharField 表示字符串.  db_index=True 表示索引
    hostname = models.CharField(max_length=32,db_index=True)
    ip = models.GenericIPAddressField(db_index=True)    #IPAddressField 也是字符串，不过可以帮忙验证下ip地址
    port = models.IntegerField()
    #主机一定要对应一个业务线。 主机表关联业务线表。   to表名，id是关联到业务线表的列
    b = models.ForeignKey(to='Business', to_field='id',on_delete=models.CASCADE)


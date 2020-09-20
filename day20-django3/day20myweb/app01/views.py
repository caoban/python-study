from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from app01 import models

def business(request):
    #QuerySet 类型
    #返回结果是 对象
    v1 = models.Business.objects.all()
    #返回结果是 字典
    v2 = models.Business.objects.all().values('id','caption')
    #返回结果是 元组
    v3 = models.Business.objects.all().values_list('id','caption')
    print("v1 :",v1,"\n","v2 :",v2,"\n","v3 :",v3,"\n")
    return render(request, 'business.html', {'v1':v1,'v2':v2,'v3':v3})

#
def host(request):
    if request.method == "GET":
        v1 = models.Host.objects.filter(nid__gt=0)
        v2 = models.Host.objects.filter(nid__gt=0).values('nid','hostname','b_id','b__caption')
        v3 = models.Host.objects.filter(nid__gt=0).values_list('nid','hostname','b_id','b__caption')
        b_list = models.Business.objects.all()
        return render(request,'host.html',{'v1':v1,'v2':v2,'v3':v3,'b_list':b_list})

    elif request.method == "POST":
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        models.Host.objects.create(
            hostname=h,
            ip=i,
            port=p,
            b_id=b
        )
        #redirect 是get请求，这样提交了数据后，再次走到get请求里面，再次刷新了页面。
        return redirect('/host')


# 对比说明 对象，字典，元祖时使用的
# def host(request):
#
#     # 对象
#     v1 = models.Host.objects.filter(nid__gt=0)
#     # for row in v1:
#     #     print(row.nid,row.hostname,row.ip,row.port,row.b_id,row.b.caption,row.b.code,sep='\t')
#
#     # 字典
#     v2 = models.Host.objects.filter(nid__gt=0).values('nid','hostname','b_id','b__caption')
#     print(v2)
#     print("------")
#     for row in v2:
#         print(row['nid'],row['hostname'],row['b_id'],row['b__caption'])
#
#     # 元组
#     v3 = models.Host.objects.filter(nid__gt=0).values_list('nid','hostname','b_id','b__caption')
#
#     return render(request, 'host.html', {'v1':v1,'v2':v2,'v3':v3})
#     #return HttpResponse("Host")


def test_ajax(request):
    import json
    ret = {'status':False,'error':None,'data':None}
    try:
        h = request.GET.get('hostname')
        i = request.GET.get('ip')
        p = request.GET.get('port')
        b = request.GET.get('b_id')
        if h and len(h) > 5:
            models.Host.objects.create(
                hostname=h,
                ip=i,
                port=p,
                b_id=b
            )
        else:
            ret['status'] = False
            ret['error'] = '太短了'
    except Exception as e:
        ret['status'] = False
        ret['error'] = '请求错误'
    return HttpResponse(json.dumps(ret))
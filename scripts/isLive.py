#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

#strip()方法 用于移除字符串头尾指定的字符（默认为空格）
#split()通过指定分隔符对字符串进行切片
#


with open("list1",'r') as f:
    for line in f:
        line = line.strip().split()
        ip = line[0]
        serviceslist = (line[1])
        # 服务信息 分离出来
        serviceslistsplit = serviceslist.strip().split(',')

        #for循环分离出服务的名称和端口，

        #Exception 抓取全部异常，并打印出来出问题的时候的那个字段的值

        for i in range(len(serviceslistsplit)):
            try:
                servicesname = serviceslistsplit[i].strip().split(':')[0]
                servicesport = serviceslistsplit[i].strip().split(':')[1]
            except Exception as e:
                print('Reason:',e,servicesname,servicesport)


            # 获取ip和端口，拼接执行 curl 命令,获取结果


            # 获取ip和端口，拼接执行 curl 命令,获取结果。requests 是可以curl的方式。有post或者get方法
            #replace 是替换

            servicesurl = "http://%s:%s/isLive" %(ip,servicesport)
            curlresult = requests.get(servicesurl)
            curlreturnvalue = str(curlresult.text).replace('\n',"").replace(' ',"")
            curlcode = curlresult.status_code
            curlheaderContentType = curlresult.headers.get('Content-Type')
            ShowResult = "%s,%s,%s,%s,%s\n" %(servicesname,servicesurl,curlreturnvalue,curlcode,curlheaderContentType)

            # 写入文件
            with open('result.csv', 'a+',encoding="utf-8") as file:
                file.write(ShowResult)


















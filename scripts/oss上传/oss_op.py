#!/usr/local/python2.7/bin/python
#coding:utf-8

import oss2
import os, sys

#python 脚本输入的3个参数
local_path = sys.argv[1]
local_dir = sys.argv[2]
remote_path = sys.argv[3]

#定义一个空的列表，后面多个文件都放在这个里面。 这个也是修改后，其他多个地方可以使用的。
file_list = []

auth = oss2.Auth('jIUSgxehNtnFCTsY','mf4gRstWHxRAwMraYOEM5Z3fJztMPy')           
endpoint = 'http://oss-cn-shanghai.aliyuncs.com/gzyct/'                         
bucket = oss2.Bucket(auth,endpoint,'gatstatic',connect_timeout=60)              

os.chdir(local_path)


if os.path.isdir(local_dir):

    #获取local_dir 目录下面的 各个文件的全路径
    #https://www.jianshu.com/p/bbad16822eab  参考这个文档
    for root, dir, file in os.walk(local_dir):
        if file != []:
            for j in file:
                #获取local_dir 目录下面的 各个文件的全路径
                path = os.path.join(root, j)
                #加到一个 列表中
                file_list.append(path)

    for file in file_list:
        remote_file = os.path.join(remote_path,'/'.join(file.split('/')[1:]))
        with open(file, 'rb') as f:
            bucket.put_object(remote_file, f)
else:
    remote_file = os.path.join(remote_path, local_dir)
    with open(local_dir, 'rb') as f:
        bucket.put_object(remote_file, f)



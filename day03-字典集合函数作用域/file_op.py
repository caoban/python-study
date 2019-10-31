#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

f = open("ye",'r',encoding="utf-8")
f_new = open("ye2",'w',encoding="utf-8")

for line in f:
    if "为遇见你伏笔" in line:
        line = line.replace("为遇见你伏笔","为遇见你伏笔")
    f_new.write(line)
f.close()
f_new.close()


'''

'''


'''
f = open("ye",'wb')
f.write("hello binary\n".encode())
print (f.tell())
print (f.read(5))
print (f.tell())
f.seek(0)
print (f.readline())


count = 0
for line in f:
    if count == 4:
        print ('我是第五行')
        count += 1
        continue
    print (line)
    count += 1
    
    
for index,line in enumerate(f.readlines()):
    if index == 4:
        print ('------我是第五行')
        continue
    print (line.strip())
'''















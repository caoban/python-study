
#-*-encoding:gbk-*-
import sys
#print 出来的 sys 就是这个pycharm系统的编码 是 setting里面设置的 utf-8
print(sys.getdefaultencoding())

#s 是unicode 是python3 的默认数据类型，字符串的编码是 unicode
s = "你好"

print(s.encode("gbk"))
print(s.encode("utf-8"))

#decode里面不写格式，默认是utf-8解码到unicode，实际上是gb2312，所以报错。
print(s.encode("utf-8").decode("utf-8").encode("gb2312").decode("gb2312"))



#-*-encoding:gbk-*-
import sys
#print ������ sys �������pycharmϵͳ�ı��� �� setting�������õ� utf-8
print(sys.getdefaultencoding())

#s ��unicode ��python3 ��Ĭ���������ͣ��ַ����ı����� unicode
s = "���"

print(s.encode("gbk"))
print(s.encode("utf-8"))

#decode���治д��ʽ��Ĭ����utf-8���뵽unicode��ʵ������gb2312�����Ա���
print(s.encode("utf-8").decode("utf-8").encode("gb2312").decode("gb2312"))


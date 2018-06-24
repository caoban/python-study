#导入包
import paramiko

#创建ssh对象
ssh = paramiko.SSHClient()
#允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

#连接服务器
ssh.connect(hostname='xxxx',port=22,username='xxxx',password='123')
#执行命令
#stdin是标准输入 stdout是标准输出 stderr是标准错误
stdin, stdout, stderr = ssh.exec_command('df')
#获取命令结果
result = stdout.read()

#关闭连接
ssh.close()

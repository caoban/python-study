#导入包
import paramiko

#指定本地公钥位置
private_key = paramiko.RSAKey.from_private_key_file('id_rsa.txt')

#创建ssh对象
ssh = paramiko.SSHClient()
#允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

#连接服务器
ssh.connect(hostname='10.101.11.201',port=22,username='root', pkey=private_key)
#执行命令
#stdin是标准输入 stdout是标准输出 stderr是标准错误
stdin, stdout, stderr = ssh.exec_command('df -h;hostname')

#获取命令结果
#三元运算，这样正确的和错误的结果都能获取到。
res,err = stdout.read(),stderr.read()
result = res if res else err

#result = stdout.read()
#打印结果 因为结果是二进制的所以加个decode
print(result.decode())
#关闭连接
ssh.close()


import paramiko
transport = paramiko.Transport(('hostname',22))
transport.connect(username='sssss',password='123')
#创建一个对象
sftp = paramiko.SFTPClient.from_transport(transport)
#将location.py 上传至文件服务器 /tmp/test.py
sftp.put('/tmp/location.py','/tmp/test.py')

#将remove_path 的问题下载到本地
sftp.get('remove_path','local_path')

#注意不是sftp的对象close
transport.close()


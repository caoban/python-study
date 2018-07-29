
import pika

# credentials = pika.PlainCredentials('alex', 'alex3714')

#建立个基本的连接
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost',5672)
)

#声明一个管道
channel = connection.channel()

#声明一个queue
# durable=True 表示持久化的意思。consumer和producer都要写。只能持久化队列queue,队列里的内容不能持久化
channel.queue_declare(queue='hello')

#下面才开始真正发消息
channel.basic_publish( exchange='',
                       routing_key='hello', #queue名称
                       body='HELLO suhan',
                       # properties=pika.BasicProperties(
                       # delivery_mode=2, #队列queue里面的内容，持久化。只要producer这边写就好了
                       # ))
                       )

print("[x] send HELLO suhan ")

#把队列关闭
connection.close()








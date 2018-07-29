
import pika
import time

# credentials = pika.PlainCredentials('alex', 'alex3714')

#建立个基本的连接
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)


#建立个管道
channel = connection.channel()

#建立个 queue,因为不确定生产者先启动还是消费者先启动
channel.queue_declare(queue='hello')


#回调函数。 函数处理完了，代表消息处理完了，函数没完代表消息没完。
def callback(ch, method, properties, body):
    print(ch,method,properties)
    time.sleep(10)
    print("[x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)



#声明开始收消息
channel.basic_consume(#三个参数是消费消息的参数
                      callback, #如果收到消息就调用callback函数处理消息
                      queue='hello',
                      #no_ack=True #处理完或者没处理完，不确认。默认是确认的
                        )


print(' [*] Waiting for messages. To exit press CTRL+C')
#开始收
channel.start_consuming()




import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))

channel = connection.channel()

#先用一个之前传过来的 queue的名称，再把消息传回去的时候，用另外一个 queue
channel.queue_declare(queue='rpc_queue')

#就是 斐波那契的一个递归函数
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#消息过来后的，处理的过程的函数
def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] fib(%s)" % n)
    response = fib(n)

    #利用 queue传输的 默认的参数来，写一个queue传输的时候的东西。
    #routing_key=props.reply_to 就是client端多声明的那个queue的名称
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id= \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

#我处理完一个再给我下一下
channel.basic_qos(prefetch_count=1)

#声明开始处理。on_request是回调函数
channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
#开始处理
channel.start_consuming()








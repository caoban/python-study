
#client 发送端
import pika
import uuid

class FibonacciRpcClient(object):
    #初始化函数
    def __init__(self):
        self.connnection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'
        ))
        self.channel = self.connnection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        #声明开始消费，不是真的开始.on_response是回调函数
        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    #回调函数，里面的几个参数，都是用队列的时候 带的一些参数
    def on_response(self,ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body


    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())

        #声明 队列传输的信息
        #routing_key='rpc_queue'是这次传输的 queue名称
        #reply_to=self.callback_queue 是再定义一个回来的时候的queue的名称
        #correlation_id=self.corr_id 是传输的是带一个id ，当做辨识的。
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                        ),
                                   body=str(n))

        #如果返回值是空的，就一直收
        while self.response is None:
            self.connnection.process_data_events()

        return int(self.response)

#初始化一个对象
fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(30)
print(" [.] Got %r" % response)






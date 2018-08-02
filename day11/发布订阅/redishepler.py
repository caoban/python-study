import redis


class RedisHelper():
    #初始化，连接这台机器
    def __init__(self):
        self.__conn = redis.Redis(host='10.101.9.115',port=6379,db=15)
        self.chan_sub = 'fm104.5'
        self.chan_sub = 'fm104.5'

    #发布消息的函数
    #直接写上频道就发送消息走了
    def public(self, msg):
        self.__conn.publish(self.chan_sub, msg)
        return True

    #订阅
    def subscribe(self):
        #开始订阅，相当于打开收音机
        pub = self.__conn.pubsub()
        #调频道
        pub.subscribe(self.chan_sub)
        #准备接受
        pub.parse_response()
        #再调用一次才是真正的接收
        return pub




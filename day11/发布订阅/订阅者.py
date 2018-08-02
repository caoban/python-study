
#从redishepler.py 文件中导入 RedisHelper类
from redishepler import RedisHelper

#实例化
obj = RedisHelper()

redis_sub = obj.subscribe()

while True:
    msg = redis_sub.parse_response()
    print(msg)



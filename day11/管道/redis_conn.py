import redis
import time

pool = redis.ConnectionPool(host='10.101.9.115',port=6379,db=15)

r = redis.Redis(connection_pool=pool)

pipe = r.pipeline(transaction=True)


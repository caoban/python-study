
from urllib import request
import gevent,time
from gevent import monkey

#把当前程序的所有IO操作打上标记
#因为gevent不知道 urllib 在不在做IO操作
monkey.patch_all()


def f(url):
    print('GET %s' %url)

    resp = request.urlopen(url)
    print("开始%s" % resp)
    data = resp.read()
    f1 = open("url.html","wb")
    f1.write(data)
    f1.close()
    print('%d bytes received from %s.' % (len(data), url))

statrt_time = time.time()

# # # 携程并发
# gevent.joinall([
#     gevent.spawn(f, 'https://v.iivey.com/'),
#     gevent.spawn(f, 'https://v.iivey.com/'),
#     gevent.spawn(f, 'https://v.iivey.com/'),
# ])



urls = [
'https://v.iivey.com/',
'https://v.iivey.com/',
'https://v.iivey.com/'
]
for i in urls:
    f(i)

print("总时间" , time.time() - statrt_time)


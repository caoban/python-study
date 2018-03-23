# import hashlib
#
# m = hashlib.md5()
# m.update(b"hello")
#
# #十进制的加密方式
# print(m.digest())
#
# #十六进制的加密方式
# print(m.hexdigest())
#


import hmac
h = hmac.new(b"12312321",b"adadfaf")
print(h.hexdigest())
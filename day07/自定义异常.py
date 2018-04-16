class SuhanException(Exception):
    def __init__(self,msg):
        self.message = msg

try:
    #raise 是触发的意思
    raise SuhanException('我的异常')
except SuhanException as e:
    print(e)

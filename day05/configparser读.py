import  configparser

conf = configparser.ConfigParser()

conf.read("example.ini")

#读取默认的 配置
print(conf.defaults())

#读取指定的一段配置的 一个key
print(conf['bitbucket.org']['user'])

#这个读不了默认的 [DEFAULT] 这种读不了
print(conf.sections())

sec = conf.remove_section('bitbucket.org')
conf.write(open('example.ini','w'))



import configparser

config = configparser.ConfigParser()

#第一种生成的方式，key-value的形式
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

#第二种写入形式
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'

#第三种写入形式
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here

#第四种写入形式
config['DEFAULT']['ForwardX11'] = 'yes'

#最后 一步写入文件
with open('example.ini', 'w') as configfile:
    config.write(configfile)

#import yaml
from pyaml import dumps as dump
from yaml import load

#打开并load源文件
podtest21001 = open('podtest21001.yaml')
deployment = load(podtest21001)

num = 21000

while num < 21036:
    num+=1
    name='deploytest' + str(num)

    #替换的部分
    deployment['metadata']['labels']['k8s-app'] = name
    deployment['metadata']['name'] = name
    deployment['spec']['selector']['matchLabels']['k8s-app'] = name
    deployment['spec']['template']['metadata']['labels']['k8s-app'] = name
    deployment['spec']['template']['spec']['containers'][0]['env'][3]['value'] = name
    deployment['spec']['template']['spec']['containers'][0]['name'] = name
    deployment['spec']['template']['spec']['volumes'][0]['hostPath']['path'] = "/data1/log/tomcat/" + name


    podtest21001Service = open('podtest21001Service.yaml')
    deploymentService = load(podtest21001Service)

    deploymentService['metadata']['labels']['k8s-app'] = name
    deploymentService['metadata']['name'] = name
    deploymentService['spec']['ports'][0]['nodePort'] = num
    deploymentService['spec']['selector']['k8s-app'] = name


    #join 把两个用 --- 连接起来
    result = '---\n'.join((dump(deployment).decode(), dump(deploymentService).decode()))

    #dump 并写入文件
    with open(name+".yaml",'w') as f:
        f.write(result)



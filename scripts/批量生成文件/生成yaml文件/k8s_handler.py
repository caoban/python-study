#!/usr/bin/env python
# coding:utf8

import logging
import os

import requests
from pyaml import dumps as dump
from yaml import load

from gat_utils import syncfile, frigate_config, k8s_deployment_template, k8s_deployment_node_template, \
    k8s_service_template, k8s_ingress_template

logger = logging.getLogger("GAT")


class K8sYaml(object):
    def __init__(self, config_id):
        self.config_id = config_id
        self._load_detail()

    def _load_detail(self):
        logger.info("初始config_id: %s APPENVCONFIG详情及关联用户" % self.config_id)

        url = '%s?id=%s' % (frigate_config.API.get('API_GET_APP_ENV_ALIAS_CONFIG_BY_ID'), self.config_id)
        logger.debug(url)
        self.region_config_detail = eval(requests.get(url).content.replace("null", "None"))
        logger.debug(self.region_config_detail)

        url = '%s?id=%s' % (frigate_config.API.get('API_GET_APP_ENV_CONFIG_BY_ID'), self.config_id)
        logger.debug(url)
        self.config_detail = eval(requests.get(url).content.replace("null", "None"))
        logger.debug(self.config_detail)

        url = '%s?id=%s' % (frigate_config.API.get('API_GET_APPLICATION_BY_ID'),
                            self.config_detail.get('applicationId'))
        logger.debug(url)
        self.app_detail = eval(requests.get(url).content.replace("null", "None"))
        logger.debug(self.app_detail)

    def preview(self):
        # load template
        service = load(k8s_service_template.k8s_service)
        ingress = load(k8s_ingress_template.k8s_ingress)

        # application
        name = self.app_detail.get('name')
        appType = self.app_detail.get('appType')
        application_config = eval(self.app_detail.get("config"))
        package_name = application_config.get("packageName")
        abs_package_name = package_name.split(".")[0]
        # ingress 0:ws, 1:web
        ingress_type = application_config.get("ingress")

        # applicationEnvConfig
        configExtension = eval(self.config_detail.get('configExtension'))
        env, idc = self.region_config_detail.get('env'), self.region_config_detail.get('idc')
        domain = self.config_detail.get("domain")
        # name = '-'.join([name, env, idc])
        # {'env': ['test', 'dev', 'uat', 'prod']}
        # {'appType': {1: 'java', 2: 'php', 3: 'static', 4: 'node'}}

        if appType == 1:
            deployment = load(k8s_deployment_template.k8s_deployment)

            # 名称
            deployment['metadata']['labels']['k8s-app'] = name
            deployment['metadata']['name'] = name

            # namespace
            if env == 'test': deployment['metadata']['namespace'] = env

            deployment['spec']['selector']['matchLabels']['k8s-app'] = name
            deployment['spec']['template']['metadata']['labels']['k8s-app'] = name
            deployment['spec']['template']['spec']['containers'][0]['name'] = name
            deployment['spec']['template']['spec']['containers'][0][
                'image'] = 'registry.wuxingdev.cn/java/{}'.format(abs_package_name)
            deployment['spec']['template']['spec']['volumes'][0]['hostPath'][
                'path'] = '/data1/log/tomcat/{}'.format(
                name)
            deployment['spec']['template']['spec']['containers'][0]['env'][3]['value'] = name

            deployment['spec']['template']['spec']['containers'][0]['env'][0]['value'] = env
            deployment['spec']['template']['spec']['containers'][0]['env'][1]['value'] = idc

            deployment['spec']['template']['spec']['nodeSelector']['env'] = env

            # 副本集
            deployment['spec']['replicas'] = configExtension.get('k8sReplicas')

            # cpu & mem
            deployment['spec']['template']['spec']['containers'][0]['resources']['limits']['cpu'] = \
                configExtension.get('k8sCpuLimit')
            deployment['spec']['template']['spec']['containers'][0]['resources']['limits']['memory'] = \
                str(configExtension.get('k8sMemoryLimit')).split('.')[0] + "Mi"
            deployment['spec']['template']['spec']['containers'][0]['resources']['requests']['cpu'] = \
                configExtension.get('k8sCpuRequest')
            deployment['spec']['template']['spec']['containers'][0]['resources']['requests']['memory'] = \
                str(configExtension.get('k8sMemoryRequest')).split('.')[0] + "Mi"

        elif appType == 4:
            deployment = load(k8s_deployment_node_template.k8s_deployment)

            # 名称
            deployment['metadata']['labels']['k8s-app'] = name
            deployment['metadata']['name'] = name

            # namespace
            if env == 'test': deployment['metadata']['namespace'] = env

            deployment['spec']['selector']['matchLabels']['k8s-app'] = name
            deployment['spec']['template']['metadata']['labels']['k8s-app'] = name
            deployment['spec']['template']['spec']['containers'][0]['name'] = name
            deployment['spec']['template']['spec']['containers'][0][
                'image'] = 'registry.wuxingdev.cn/node/{}'.format(abs_package_name)

            deployment['spec']['template']['spec']['volumes'][0]['hostPath']['path'] = '/data1/log/node/{}'.format(
                name)

            deployment['spec']['template']['spec']['containers'][0]['command'][3] = "--env={}".format(env)
            deployment['spec']['template']['spec']['containers'][0]['env'][3]['value'] = name

            deployment['spec']['template']['spec']['containers'][0]['env'][0]['value'] = env
            deployment['spec']['template']['spec']['containers'][0]['env'][1]['value'] = idc
            deployment['spec']['template']['spec']['nodeSelector']['env'] = env

            # 副本集
            deployment['spec']['replicas'] = configExtension.get('k8sReplicas')

            # cpu & mem
            deployment['spec']['template']['spec']['containers'][0]['resources']['limits']['cpu'] = \
                configExtension.get('k8sCpuLimit')
            deployment['spec']['template']['spec']['containers'][0]['resources']['limits']['memory'] = \
                str(configExtension.get('k8sMemoryLimit')).split('.')[0] + "Mi"
            deployment['spec']['template']['spec']['containers'][0]['resources']['requests']['cpu'] = \
                configExtension.get('k8sCpuRequest')
            deployment['spec']['template']['spec']['containers'][0]['resources']['requests']['memory'] = \
                str(configExtension.get('k8sMemoryRequest')).split('.')[0] + "Mi"

        # service
        service['metadata']['labels']['k8s-app'] = name
        service['metadata']['name'] = name

        # namespace
        if env == 'test': service['metadata']['namespace'] = env

        service['spec']['selector']['k8s-app'] = name
        service['spec']['ports'][0]['nodePort'] = configExtension.get("k8sNodePort")

        # ingress
        # 名称
        ingress['metadata']['name'] = name
        # namespace
        if env == 'test': ingress['metadata']['namespace'] = env

        ingress['spec']['rules'][0]['host'] = domain
        ingress['spec']['rules'][0]['http']['paths'][0]['backend']['serviceName'] = name

        if ingress_type == 0:
            return '---\n'.join((dump(deployment), dump(service), dump(ingress)))
        else:
            return '---\n'.join((dump(deployment), dump(service)))

    def sync(self, path):
        with open(path, 'w') as f: f.write(self.preview())
        env = self.config_detail.get('env')
        filename = self.app_detail.get('name') + '.yaml'

        path_dict = frigate_config.APPTYPE

        remote_path = os.path.join(
            frigate_config.REMOTE_CMD.get('k8s').get(env).get('remote_path'),
            path_dict.get(self.app_detail.get('appType'))
        )
        cmd = frigate_config.REMOTE_CMD.get('k8s').get(env).get('cmd') % (
            os.path.join(
                "k8sApp",
                path_dict.get(self.app_detail.get('appType')),
                filename)
        )

        # 传输文件到ansible
        syncfile.Sync(env).sync_file(path, os.path.join(remote_path, filename))

        # 记录日志
        with open(path) as f: content = f.read()
        logger.info("生成的k8s配置: %s" % content)
        logger.info("执行的ansible命令: %s" % cmd)

        # 执行ansible命令
        return syncfile.Sync(env).exec_remote_cmd(cmd)

#!/usr/bin/python
# coding:utf-8

import os
import sys
import logging

import docker
import requests
from artifactory_config import IMAGE_BUILD_CONFIG

logger = logging.getLogger("GAT")


def create_war_docker_file(path, package):
    if not os.path.exists(os.path.join(path, package)):
        err = "no target war %s,please check it!" % package
        logger.error(err)
        sys.exit(2)

    if not os.path.exists(os.path.join(path, 'war.Dockerfile')):
        content = '''
#
# tomcat 8.5  
#

FROM registry.wuxingdev.cn/base/tomcat-gat:8.5.31

MAINTAINER august.zhou@guanaitong.com

ADD %s $CATALINA_HOME/webapps/ROOT.war

WORKDIR $CATALINA_HOME

EXPOSE 80

CMD ["catalina.sh", "run"]''' % package

        with open(os.path.join(path, 'war.Dockerfile'), 'w') as f: f.write(content)


# build images
def build_war(imageTag, latestTag, path, name, build_id):
    logger.info('开始构建镜像')

    client = docker.from_env()
    try:
        client.images.build(path=path, dockerfile='war.Dockerfile', tag=imageTag, forcerm=True)
        client.api.tag(imageTag, latestTag)
        logger.info('%s -- 镜像构建成功' % imageTag)
    except Exception as e:
        logger.error('%s build error: %s' % (imageTag, e))
        return False

    try:
        client.images.push(imageTag)
        logger.info('%s -- 镜像推送成功' % imageTag)
    except Exception as e:
        logger.error('%s push error: %s' % (imageTag, e))
        return False

    try:
        client.images.push(latestTag)
        logger.info('%s:latest -- 镜像推送成功' % latestTag)
    except Exception as e:
        logger.error('%s:latest push error: %s' % (latestTag, e))
        return False

    try:
        status_code = requests.get(IMAGE_BUILD_CONFIG.get("check_api") % ("java", name, build_id)).status_code
        if status_code != 200:
            logger.error('%s -- 镜像检测失败' % imageTag)
        else:
            logger.info('%s -- 镜像检测成功' % imageTag)
    except Exception as e:
        logger.error('%s -- 镜像检测失败, Error: %s' % (imageTag, e))

    try:
        status_code_latest = requests.get(IMAGE_BUILD_CONFIG.get("check_api") % ("java", name, 'latest')).status_code
        if status_code_latest != 200:
            logger.error('%s:latest -- 镜像检测失败' % latestTag)
        else:
            logger.info('%s:latest -- 镜像检测成功' % latestTag)
    except Exception as e:
        logger.error('%s -- 镜像检测失败, Error: %s' % (imageTag, e))

    try:
        client.images.remove(image=imageTag, force=True)
        logger.info('%s -- 镜像删除成功' % imageTag)
    except Exception as e:
        logger.error('%s remove error: %s' % (imageTag, e))

    try:
        client.images.remove(image=latestTag, force=True)
        logger.info('%s:latest -- 镜像删除成功' % latestTag)
    except Exception as e:
        logger.error('%s remove error: %s' % (latestTag, e))

    logger.info("镜像构建结束")
    return True

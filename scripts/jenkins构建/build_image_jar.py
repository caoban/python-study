#!/usr/bin/python
# coding:utf-8

import os
import sys
import logging

import docker
import requests
from artifactory_config import IMAGE_BUILD_CONFIG

logger = logging.getLogger("GAT")


def create_jar_script(path, name):
    if not os.path.exists(path):
        logger.error("未找到对应的路径: %s" % path)
        sys.exit(2)

    with open(os.path.join(path, 'startjar.sh'), 'w') as f:
        content = '''#!/bin/bash
    
echo "start exe script, author---------------------------- august.zhou@guanaitong.com"
source /etc/profile
env=${WORK_ENV}
JAVA_OPTS="${JAVA_OPTS} -XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap -XX:MaxRAMFraction=1 -XshowSettings:vm -Dclient.encoding.override=UTF-8 -Dfile.encoding=UTF-8 -Duser.language=zh -Duser.region=CN -XX:+PrintGCDateStamps -XX:+PrintGCDetails -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=logs/heapDump.hprof  -Xloggc:logs/gc.log"
#---------------------------------




echo "Start service %s in $env env ----------------------------------------------------------------------------------------------------------------------"

$JAVA_HOME/bin/java ${JAVA_OPTS} -jar  %s --server.port=80 --spring.profiles.active=$env --server.tomcat.max-threads=500 --server.tomcat.basedir=.
''' % (
            name, name
        )
        f.write(content)


def create_jar_docker_file(path, name):
    if not os.path.isfile(os.path.join(path, name)):
        errmsg = "no target jar %s,please check it!" % name
        logger.error(errmsg)
        sys.exit(2)

    if not os.path.exists(os.path.join(path, 'jar.Dockerfile')):
        with open(os.path.join(path, 'jar.Dockerfile'), 'w') as f:
            content = '''
#
# jdk
#

FROM registry.wuxingdev.cn/base/jdk-gat:8u171

MAINTAINER august.zhou@guanaitong.com

ENV WORK_HOME /usr/lib/tomcat/apache-tomcat
ENV PATH $WORK_HOME:$PATH


ADD %s.jar $WORK_HOME/
ADD startjar.sh $WORK_HOME/
RUN chmod +x $WORK_HOME/startjar.sh

WORKDIR $WORK_HOME

EXPOSE 80
CMD ["startjar.sh"]''' % (os.path.splitext(name)[0])

            f.write(content)


def build_jar(imageTag, latestTag, path, name, build_id):
    client = docker.from_env()

    logger.info('开始构建镜像')
    try:
        client.images.build(path=path, dockerfile='jar.Dockerfile', tag=imageTag, forcerm=True)
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



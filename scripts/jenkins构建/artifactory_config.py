#!/usr/bin/python
# coding:utf-8

import logging
from collections import namedtuple

JENKINS_CONFIG = {
    "user": "liang.yao",
    "password": "11b07f9ae4a593b0370d69986d39ce4030",
    "url": "http://jenkins.wuxingdev.cn/jenkins/"
}

FILESYSTEM_CONFIG = {
    "user": "guanai",
    "password": "goforg@t",
    "api": "http://%s/%s",
    "domain": "filestorage.wuxingdev.cn",
    "network_card_name": "eth0"
}

DOCKER_CONFIG = {
    "version": "17.06.0-ce",
    "framework": "amd64",
    "osversion": "linux"
}

FRIGATE_CONFIG = {
    # "api": "http://frigate.api.wuxingdev.cn/application/getApplicationByName?name=%s"
    "api": "http://frigate.api.wuxingdev.cn/application/getApplicationByJenkinsProjectName?jenkinsProjectName=%s",
    "auto_publish_api": "http://frigate.api.wuxingdev.cn/publish/autoPublish",
    "app_type": {
        1: "java",
        2: "php",
        3: "static",
        4: "node",
        5: "go",
        6: "python"
    }
}

ARTIFACTORY_METADATA_CONFIG = {
    "api": "http://artifactory.wuxingdev.cn/postArtifactoryMetaData",
    "delete_api": "http://artifactory.wuxingdev.cn/deleteArtifactoryMetaData2?applicationId=%s&commitId=%s",
    "check_api": "http://artifactory.wuxingdev.cn/checkArtifactoryMetaData",
    "status": 0
}

IMAGE_BUILD_CONFIG = {
    "check_api": "http://registry.wuxingdev.cn/api/repositories/%s%%2F%s/tags/%s/manifest",
    "image_tag": "registry.wuxingdev.cn/%s/%s:%s",
    "latest_tag": "registry.wuxingdev.cn/%s/%s"
}

FIELDS = [
    "applicationId",
    "tag",
    "commitId",
    "jenkinsBuildId",
    "jenkinsJobName",
    "changeMsg",
    "builder",
    "buildStartTime",
    "buildEndTime",
    "fileArtifactoryUrl",
    "fileArtifactorySize",
    "fileArtifactoryMd5sum",
    "imageUrl",
    "imageTag",
    "imageDockerVersion",
    "imageFramework",
    "imageOsVersion",
    "status"
]

AUTO_PUBLISH_FIELDS = [
    "commitId",
    "jenkinsJobName"
]

Application = namedtuple(
    "Application",
    "counts,"
    "ids, "
    "names, "
    "paths, "
    "package_names, "
    "types"
)

logger = logging.getLogger("GAT")
logger.setLevel(logging.DEBUG)

# 格式化输出
hdr = logging.StreamHandler()
# fmt = logging.Formatter('[%(asctime)s] %(lineno)d:%(levelname)s: %(message)s')
fmt = logging.Formatter('%(levelname)s: %(message)s')
hdr.setFormatter(fmt)

logger.addHandler(hdr)

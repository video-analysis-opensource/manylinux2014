# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/6/28
import requests


quay_io_data_amd64 = requests.get('https://quay.io/api/v1/repository/pypa/manylinux2014_x86_64/tag'
                            '/?limit=100&page=1&onlyActiveTags=true').json()
quay_io_data_arm64 = requests.get('https://quay.io/api/v1/repository/pypa/manylinux2014_aarch64/tag'
                            '/?limit=100&page=1&onlyActiveTags=true').json()
relate_tags = []
_amd = [i['name'] for i in quay_io_data_amd64['tags']][:10]
_arm = [i['name'] for i in quay_io_data_arm64['tags']][:10]
for i in _amd:
    if i in _arm and i !='latest':
        relate_tags.append(i)
print(relate_tags)

github_amd64 = requests.get('https://hub.docker.com/v2/repositories/zhoukunpeng505/'
                            'manylinux2014-amd64/tags/?page_size=25&page=1&name&ordering').json()
github_arm64 = requests.get('https://hub.docker.com/v2/repositories/zhoukunpeng505/'
                            'manylinux2014-arm64/tags/?page_size=25&page=1&name&ordering').json()
print(github_amd64, github_arm64)


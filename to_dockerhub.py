# coding:utf-8
__author__ = "zkp"
# create by zkp on 2023/6/28
import os
import requests
import copy


quay_io_data_amd64 = requests.get('https://quay.io/api/v1/repository/pypa/manylinux2014_x86_64/tag'
                            '/?limit=100&page=1&onlyActiveTags=true').json()
quay_io_data_arm64 = requests.get('https://quay.io/api/v1/repository/pypa/manylinux2014_aarch64/tag'
                            '/?limit=100&page=1&onlyActiveTags=true').json()
relate_tags = []
_amd = [i['name'] for i in quay_io_data_amd64['tags']][:10]
_arm = [i['name'] for i in quay_io_data_arm64['tags']][:10]
for i in _amd:
    if  i !='latest':
        relate_tags.append(i)
relate_tags.reverse()
print(relate_tags)

github_amd64 = requests.get('https://hub.docker.com/v2/repositories/zhoukunpeng505/'
                            'manylinux2014-amd64/tags/?page_size=25&page=1&name&ordering').json()
github_arm64 = requests.get('https://hub.docker.com/v2/repositories/zhoukunpeng505/'
                            'manylinux2014-arm64/tags/?page_size=25&page=1&name&ordering').json()
github_cross = requests.get('https://hub.docker.com/v2/repositories/zhoukunpeng505/'
                            'manylinux2014/tags/?page_size=25&page=1&name&ordering').json()

github_amd64 = [i['name'] for i in copy.deepcopy(github_amd64.get("results", []))]
github_arm64 = [i['name'] for i in copy.deepcopy(github_arm64.get("results", []))]
github_cross = [i['name'] for i in copy.deepcopy(github_cross.get("results", []))]


for index,tag in  enumerate(relate_tags):
    if index == len(relate_tags) -1:
        is_end_loop = True
    else:
        is_end_loop = False

    if tag not in github_amd64:
        os.system(f"docker pull quay.io/pypa/manylinux2014_x86_64:{tag}")
        os.system(f"docker tag quay.io/pypa/manylinux2014_x86_64:{tag} zhoukunpeng505/manylinux2014_amd64:{tag}")
        os.system(f"docker push zhoukunpeng505/manylinux2014_amd64:{tag}")
        if is_end_loop:
            os.system(f"docker tag quay.io/pypa/manylinux2014_x86_64:{tag} zhoukunpeng505/manylinux2014_amd64:latest")
            os.system(f"docker push zhoukunpeng505/manylinux2014_amd64:latest")

    if tag not in github_arm64:
        os.system(f"docker pull quay.io/pypa/manylinux2014_aarch64:{tag}")
        os.system(f"docker tag quay.io/pypa/manylinux2014_aarch64:{tag} zhoukunpeng505/manylinux2014_arm64:{tag}")
        os.system(f"docker push zhoukunpeng505/manylinux2014_arm64:{tag}")
        if is_end_loop:
            os.system(f"docker tag quay.io/pypa/manylinux2014_aarch64:{tag} zhoukunpeng505/manylinux2014_arm64:latest")
            os.system(f"docker push zhoukunpeng505/manylinux2014_arm64:latest")


    if tag not in github_cross:
        if not is_end_loop:
            os.system(f"docker buildx build --platform linux/arm64,linux/amd64  "
                      f"--build-arg FROM_TAG='{tag}' -t zhoukunpeng505/manylinux2014:{tag} "
                      f" .  --push")
        else:
            os.system(f"docker buildx build --platform linux/arm64,linux/amd64  "
                      f"--build-arg FROM_TAG='{tag}' -t zhoukunpeng505/manylinux2014:{tag}  "
                      f"-t zhoukunpeng505/manylinux2014:latest  .  --push ")


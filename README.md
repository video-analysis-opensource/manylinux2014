# manylinux2014
manylinux2014 cross platform docker images。<br/>
每天凌晨自动执行，从https://quay.io/organization/pypa 拉取，然后推送到dockerhub：
- 拉取 manylinux2014_aarch64 最新的tag，推送到zhoukunpeng505/manylinux2014_arm64
- 拉取 manylinux2014_x86_64  最新的tag，推送到zhoukunpeng505/manylinux2014_amd64
- 根据 manylinux2014_aarch64 和 manylinux2014_x86_64，合成跨平台镜像推送到 zhoukunpeng505/manylinux2014

docker hub地址： https://hub.docker.com/r/zhoukunpeng505/manylinux2014/tags


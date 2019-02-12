下载搭建私有仓库需要的镜像
docker pull registry

docker run -d -v /opt/registry:/var/lib/registry -p 5000:5000 --restart=always --name registry registry

查看仓库里的镜像
curl http://192.168.37.129:5000/v2/_catalog



curl http://192.168.5.8:5001/v2/_catalog

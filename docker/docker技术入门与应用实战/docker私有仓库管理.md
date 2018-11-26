docker tag wordpress:v1 192.168.37.129:5000/wordpress:v1

docker push  192.168.37.129:5000/wordpress:v1


```

配置私有仓库可信任(出现异常Get https://192.168.37.129:5000/v2/: http: server gave HTTP response to HTTPS client)
 vi /etc/docker/daemon.json
{"insecure-registries":["192.168.37.129:5000"]}

重启加载json数据
service docker restart


打标签
docker tag wordpress:v1 192.168.37.129:5000/wordpress:v1

上传
docker push  192.168.37.129:5000/wordpress:v1

下载
docker pull  192.168.37.129:5000/wordpress:v1

查看镜像
curl http://192.168.37.129:5000/v2/_catalog

列出镜像标签
curl http://192.168.37.129:5000/v2/wordpress/tags/list



```
docker run -itd --name wordpress -p 88:80 192.168.37.129:5000/wordpress:v1


 docker rm $(docker ps -q -a)

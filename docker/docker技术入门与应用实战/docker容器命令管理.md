#### 容器基本操作
docker ps -a
docker ps -q
docker ps -s

attach
rm
start
stop
kill
pause/unpause
rename


#### 容器进阶操作：
docker inspect name


docker exec name ls

docker top name

docker port

docker cp file_path   name:path
docker cp name:path file_path   

docker diff

docker logs

收集动态容器信息
docker stats

收集静态容器信息
docker stats --no-stream name


docker update

查看容器指定时间或者类型事件
docker events

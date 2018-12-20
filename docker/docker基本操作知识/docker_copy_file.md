将宿主机文件复制到容器内部指定地方
docker cp 本地文件路径 容器ID全程：容器内部文件路径

docker cp /var/a87.sql  42cbb4ba3f2d9f217611192f81166b236df794d889ca6154a22497383cf60144:/var/


容内部文件传送至宿主机上
docker cp  容器ID全程：容器内部文件路径  宿主机文件路径


docker cp 42cbb4ba3f2d9f217611192f81166b236df794d889ca6154a22497383cf60144:/a87.sql /var/

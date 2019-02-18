docker pull mysql:5.7


```
docker run -d -it -p 3306:3306 -v /var/log/mysql:/var/log  -e MYSQL_ROOT_PASSWORD=123123  --name=mysql   mysql/mysql-server --character-set-server=utf8 || :

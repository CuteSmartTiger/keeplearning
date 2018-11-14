sudo docker pull mysql/mysql-server

docker tag mysql/mysql-server mysql

sudo docker run --name=mysqltest -it -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123123 -d mysql

# 创建mysql数据库容器
docker run -itd --name lnmp_mysql -p 3308:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql --character-set-server=utf8
# 创建wp数据库
docker exec lnmp_mysql sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD" -e"create database wp"'
# 创建PHP环境容器
docker run -itd --name lnmp_web --link lnmp_mysql:db -p 88:80 -v /container_data/web:/var/www/html richarvey/nginx-php-# 以wordpress博客为例测试
wget https://cn.wordpress.org/wordpress-4.7.4-zh_CN.tar.gz
tar zxf wordpress-4.7.4-zh_CN.tar.gz
mv wordpress/* /container_data/web/
# 浏览器测试访问
http://IP:88

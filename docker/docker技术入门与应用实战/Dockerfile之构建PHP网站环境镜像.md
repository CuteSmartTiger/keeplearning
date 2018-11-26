```
FROM centos:6
MAINTAINER lizhenliang
RUN yum install -y httpd php php-gd php-mysql mysql mysql-server
ENV MYSQL_ROOT_PASSWORD 123456
RUN echo "<?php phpinfo()?>" > /var/www/html/index.php

ADD start.sh /start.sh
RUN chmod +x /start.sh

ADD https://cn.wordpress.org/wordpress-4.7.4-zh_CN.tar.gz /var/www/html
#COPY wp-config.php /var/www/html/wordpress

VOLUME ["/var/lib/mysql"]

CMD /start.sh

EXPOSE 80 3306
```


cat /start.sh
```
service httpd start
service mysqld start
mysqladmin -uroot password $MYSQL_ROOT_PASSWORD
tail -f
```


docker build -t wordpress:v1 .

docker build -t wordpress:v1 . --no-cache

docker run -itd --name wordpress -p 88:80 liuhu:v1

docker ps -a

docker exec wordpress ls /var/www/html

需要进入容器解压
tar -xzf wordpress-4.7.4-zh_CN.tar.gz

mysql -uroot -p$MYSQL_ROOT_PASSWORD


docker run -itd --name wordpress -p 88:80 wordpress:v1

docker cp wp-config.php wordpress:/var/www/html/wordpress
 docker exec wordpress ls /var/www/html/wordpress

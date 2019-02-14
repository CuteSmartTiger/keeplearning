先更新源

sudo apt-get install apache2

sudo /etc/init.d/apache2 restart

ab -V

ab -n 1000 -c 10 http://192.168.6.92/admin/home

docker 清理对象
参考网址：https://blog.csdn.net/wennuanddianbo/article/details/78453325






### prune everything
清理everything：images ，containers，networks一次性清理操作命令：
docker system prune
在Docker 17.06.0 以及更早的版本中，这个docker system prune也会将volume一起清理掉；
在Docker 17.06.1以及后期的版本中则必须要手动指定--volumes标志才能够清理掉volumes

##### memory locking requested for elasticsearch process but memory is not locked

问题
```
[1] bootstrap checks failed
[1]: memory locking requested for elasticsearch process but memory is not locked
```
解决方法：
```
要么是bootstrap.memory_lock: true这个没设置，要
么就是max locked memory这个没配置么

针对只适用于通过PAM认证登录用户的资源限制，登
录用户的限制，通过 /etc/security/limits.conf 来配置
vi /etc/security/limits.conf

* soft nofile 65536
* hard nofile 65536
* soft nproc 32000
* hard nproc 32000
* hard memlock unlimited
* soft memlock unlimited



对于systemd service的资源限制，现在放
在 /etc/systemd/system.conf 和 /etc/systemd/user.conf
主要的修改对象vi /etc/systemd/system.conf，在文件里添加

DefaultLimitNOFILE=65536
DefaultLimitNPROC=32000
DefaultLimitMEMLOCK=infinity


然后重启并查看
/bin/systemctl daemon-reload
/bin/systemctl enable elasticsearch.service
systemctl start elasticsearch.service
systemctl status elasticsearch.service
```
参考文章
- [记录一次Ubuntu16.04上安装Elasticsearch踩的坑，memory lock问题](https://segmentfault.com/a/1190000014891856)

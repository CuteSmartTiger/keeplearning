#### 创建容器命令格式：
只创建
Usage:  docker create [OPTIONS] IMAGE [COMMAND] [ARG...]

创建并运行
Usage:  docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

#### OPTIONS（常用选项）
```
-	i, --interactive
-	t, --tty
-	d, --detach
--add-host list
-	a, --attach list
--cap-add list
--cap-drop list
--cidfile string
--device list
--dns list
-	e, --env list
--env-file list
--expose list
-	h, --hostname string --ip string
--link list

--log-driver
（none、json-file、syslog、fluentd、splunk等） --log-opt
--mount mount
--network string
--oom-kill-disable
--pid string

-	p, --publish list
-	P, --publish-all=true|false --restart
--ulimit ulimit
-	v, --volume list
--volumes-from list
-	w, --workdir string

--cpu-period int
--cpu-quota int




-	c, --cpu-shares int
-	c, --cpu-shares int
--cpuset-cpus string
--device-read-bps list
--device-write-bps list
--device-read-iops list
--device-write-iops list
-	m, --memory bytes
--memory-reservation bytes
--memory-swap bytes
--memory-swappiness int
--storage-opt list只支持devicemapper存储驱
```

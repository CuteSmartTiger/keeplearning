
```shell
#!/bin/bash

vir_ip=$(echo `egrep '([0-9]{1,3}\.){1,3}[0-9]{1,3}' /etc/keepalived/keepalived.conf | awk '{ print $1 }'`)



ping_ip=$(echo `ping -c 1  ${vir_ip} | grep "packet loss" | awk '{ print $4 }'`)

if [ "${ping_ip}"x == "0"x ];then
  `service keepalived restart`
  echo 'loss virtual ip '
else
  echo 'get virtual ip'
fi
```

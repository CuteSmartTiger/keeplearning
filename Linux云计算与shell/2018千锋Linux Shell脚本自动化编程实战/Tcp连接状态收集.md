- 收集tcp信息给人看
```SHELL
ss -an | grep ^tcp | awk '{tcp_connect_status[$2]++} END {for(i in tcp_connect_status){print i,tcp_connect_status[i]}}'
```

- 结合zabbix收集信息
```SHELL
#!/usr/bin/env bash
LISTEN(){
  ss -an | grep '^tcp' | grep 'LISTEN' | wc -l
}

SYN_RECV(){
  ss -an | grep '^tcp' | grep 'SYN[_-]RECV' | wc -l
}

ESTABLISHED(){
  ss -an | grep '^tcp' | grep 'ESTAB' | wc -l
}

TIME_WAIT(){
  ss -an | grep '^tcp' | grep 'TIME[_-]WAIT' | wc -l
}

$1
```

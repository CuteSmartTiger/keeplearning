```SHELL
#!/usr/bin/env bash
# for zabbix

Uptime() {
  mysqladmin status |awk '{print $2}'
}

Slow_queries() {
  mysqladmin status |awk '{print $9}'
}

Com_insert() {
mysqladmin extended-status | awk '/\<Com_insert\>/{print $4}'
}

Com_delete() {
mysqladmin extended-status | awk '/\<Com_delete\>/{print $4}'
}

Com_update() {
mysqladmin extended-status | awk '/\<Com_update\>/{print $4}'
}

Com_select() {
mysqladmin extended-status | awk '/\<Com_select\>/{print $4}'
}

Com_commit() {
mysqladmin extended-status | awk '/\<Com_commit\>/{print $4}'
}

Com_rollback() {
mysqladmin extended-status | awk '/\<Com_rollback\>/{print $4}'
}

$1
```

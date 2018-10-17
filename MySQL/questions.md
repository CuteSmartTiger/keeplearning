1. docker 数据卷的数据存储位置   




2. (_mysql_exceptions.OperationalError) (1105, 'Percona-XtraDB-Cluster prohibits use of DML command on a table (desktop.alembic_version) without an explicit primary key with pxc_strict_mode = ENFORCING or MASTER') [SQL: u"INSERT INTO alembic_version (version_num) VALUES ('0001')"]

体现了pxc的特性，所有的标都需要主键

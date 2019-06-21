# Dump of table tenant
# ------------------------------------------------------------

DROP TABLE IF EXISTS `tenant`;

CREATE TABLE `tenant` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增长ID',
  `is_deleted` tinyint(1) NOT NULL COMMENT '是否删除',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime NOT NULL COMMENT '更新时间',
  `creator` varchar(255) DEFAULT NULL COMMENT '创建者',
  `updator` varchar(255) DEFAULT NULL COMMENT '更新者',
  `name` varchar(255) NOT NULL DEFAULT '' COMMENT '租户名称',
  `ad_server_uri` varchar(255) DEFAULT NULL COMMENT '租户AD服务地址',
  `ad_bind_dn` varchar(255) DEFAULT NULL COMMENT '租户AD服务DN',
  `admin_ad` varchar(255) DEFAULT NULL COMMENT '租户管理员DN',
  `admin_password` varchar(255) DEFAULT NULL COMMENT '租户管理员密码',
  PRIMARY KEY (`id`),
  UNIQUE KEY `tenant_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `tenant` WRITE;
/*!40000 ALTER TABLE `tenant` DISABLE KEYS */;

INSERT INTO `tenant` (`id`, `is_deleted`, `create_time`, `update_time`, `creator`, `updator`, `name`, `ad_server_uri`, `ad_bind_dn`, `admin_ad`, `admin_password`)
VALUES
	(1,0,'2018-03-19 03:19:00','2018-03-19 03:19:00','admin','admin','贝壳金控','10.56.10.113','OU=贝壳金控,OU=BKJK,dc=corp,dc=bkjk,dc=com','CN=dalmore,CN=Users,DC=corp,DC=bkjk,DC=com','BKJKops123!@'),
	(2,0,'2018-03-19 03:19:00','2018-03-19 03:19:00','admin','admin','理房通','10.12.3.30','OU=理房通,DC=corp,DC=ehomepay,DC=com,DC=cn','CN=达尔摩,OU=贝壳,OU=理房通,DC=corp,DC=ehomepay,DC=com,DC=cn','LFTeh0mepay!');

/*!40000 ALTER TABLE `tenant` ENABLE KEYS */;
UNLOCK TABLES;



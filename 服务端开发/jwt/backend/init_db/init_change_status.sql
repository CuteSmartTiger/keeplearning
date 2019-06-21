LOCK TABLES `changestatus` WRITE;

INSERT INTO `changestatus` (`id`, `is_deleted`, `create_time`, `update_time`, `creator`, `updator`, `code`, `desc`)
VALUES
	(1,0,'2018-03-20 14:58:00','2018-03-20 14:58:00',NULL,NULL,'WAIT_QA','待测试'),
	(2,0,'2018-03-20 14:58:00','2018-03-20 14:58:00',NULL,NULL,'WAIT_APPROVE','待审批'),
	(3,0,'2018-03-20 14:58:00','2018-03-20 14:58:00',NULL,NULL,'WAIT_OPS','待执行'),
	(4,0,'2018-03-20 14:58:00','2018-03-20 14:58:00',NULL,NULL,'WAIT_DEV','待验收'),
	(5,0,'2018-03-20 14:58:00','2018-03-20 14:58:00',NULL,NULL,'DONE','已完成'),
	(6,0,'2018-03-20 14:58:00','2018-03-20 14:58:00',NULL,NULL,'CANCEL','已取消'),
	(7,0,'2018-03-20 14:58:00','2018-03-20 14:58:00',NULL,NULL,'REJECT','已拒绝');

UNLOCK TABLES;

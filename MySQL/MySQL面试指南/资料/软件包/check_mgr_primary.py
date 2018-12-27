#!/usr/bin/env python
#coding=utf-8
import MySQLdb
import socket,sys
user='repl'
pwd='123456'
local='10.102.13.2'
#config sentinel server list
try:
	conn = MySQLdb.connect(host =local,user ='repl',passwd = '123456',db = 'information_schema',charset="utf8")
except MySQLdb.Error, e:
	print "Error %d: %s \n" % (e.args[0], e.args[1])
	run=1
	while run <=3:
		try:
			conn = MySQLdb.connect(host =local,user ='repl',passwd = '123456',db = 'information_schema',charset="utf8")
		except Exception,error:
			run=run+1
			continue

try:
	cursor = conn.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute("""show status like 'group_replication_primary_member'""")
	results = cursor.fetchall()
	for row in results:
		primary = row["Value"]
		#print "primary : %s",primary
	cursor.execute("""show variables like 'server_uuid';""")
	results = cursor.fetchall()
	for row in results:
		server_uuid=row["Value"]
		#print "server_uuid:%s",server_uuid

except Exception,error:
	print "End ERROR: %s"%error
	sys.exit(1)
if server_uuid == primary:
        print 'true'
        sys.exit(0)
else:
        print 'free vip'
        sys.exit(1)

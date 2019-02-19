#!/bin/bash
set -e

function start_salt(){
	echo $(date) starting salt ...
	service salt-master restart							
	service salt-api restart
}								
function start_nginx(){
	echo $(date) starting nginx ...
	service nginx restart
}

function handle_database(){
	echo $(date) handle database ...
	mysql=( mysql -uroot -p123123 -hvdidesktop-mysql )

	for i in {30..0}; do
		if echo 'SELECT 1' | "${mysql[@]}" &> /dev/null; then
			break
		fi
		echo 'try to connecting mysql ...'
		sleep 1
	done
	if [ "$i" = 0 ]; then
		echo >&2 'MySQL init process failed.'
		exit 1
	fi

	if [ ! -z "`mysql -uroot -p123123 -hvdidesktop-mysql -qfBse "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME='desktop'" 2>/dev/null`" ]; then   
		echo "DATABASE ALREADY EXISTS"; 
		./flask/bin/python manage.pyc db upgrade; 
	else   
		echo "DATABASE DOES NOT EXIST"; 
		mysql -uroot -p123123 -hvdidesktop-mysql -qfBse "create database desktop" 2>/dev/null; 
		./flask/bin/python manage.pyc db upgrade; 
		./flask/bin/python db_init.pyc; 
	fi				
}

function handle_i18n(){
	echo $(date) handle i18n ...
	./flask/bin/python 03_tr_compile.pyc || :
}

function handle_celery(){
	echo $(date) handle tasks ...
	export C_FORCE_ROOT="true"
	export LANG=en_US.UTF-8    # for celery encoding

	rm -f x.pid
	./flask/bin/celery multi start x -A app.celery --discard --logfile=/var/log/vdidesktop/celery.log
	./flask/bin/python run_tasks.pyc
	./flask/bin/celery beat -A app.celery --detach --logfile=/var/log/vdidesktop/celery.log   # scheduled tasks
}

function start_vdidesktop(){
	echo $(date) start vdidesktop ...
	uwsgi_python --ini vdidesktop.ini
}

function main(){
	cd /opt/vdidesktop
	mkdir -p /var/log/vdidesktop

	if [ "$1" == "dm" ];then
		start_salt
		sleep 1000000d
	elif [ "$1" == "frontend" ];then
		while true;do
			redis-cli -h vdidesktop-redis blpop backend-ready 0 
			if [ $? -eq 0 ];then
				break
			else
				sleep 1
			fi
		done
		start_nginx
		sleep 1
		start_vdidesktop
	elif [ "$1" == "backend" ];then
		handle_database
		handle_i18n
		handle_celery
		while true;do
			redis-cli -h vdidesktop-redis rpush backend-ready 1
			if [ $? -eq 0 ];then
				break
			else
				sleep 1
			fi
		done
		sleep 1000000d
	else
		start_salt
		start_nginx
		handle_database
		handle_i18n
		handle_celery
		sleep 1
		start_vdidesktop
	fi
}

echo $(date) entry script ...
main $1


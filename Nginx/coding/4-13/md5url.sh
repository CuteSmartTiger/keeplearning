#!/bin/sh
#
#Auth:Jeson@imoocc.com
servername="jeson.t.imooc.io"
download_file="/download/file.img"
time_num=$(date -d "2018-10-18 00:00:00" +%s)
secret_num="imoocc"

res=$(echo -n "${time_num}${download_file} ${secret_num}"|openssl md5 -binary | openssl base64 | tr +/ -_ | tr -d =)

echo "http://${servername}${download_file}?md5=${res}&expires=${time_num}"

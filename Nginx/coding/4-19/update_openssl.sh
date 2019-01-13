#!/bin/sh
#jeson@imoocc.com
cd /opt/download
wget https://www.openssl.org/source/openssl-1.0.2k.tar.gz
tar -zxvf openssl-1.0.2k.tar.gz
cd openssl-1.0.2k
./config --prefix=/usr/local/openssl 
make && make install 
mv /usr/bin/openssl   /usr/bin/openssl.OFF 
mv /usr/include/openssl   /usr/include/openssl.OFF 
ln -s   /usr/local/openssl/bin/openssl   /usr/bin/openssl 
ln -s   /usr/local/openssl/include/openssl   /usr/include/openssl 
echo "/usr/local/openssl/lib"  >>/etc/ld.so.conf 
ldconfig -v
openssl version -a

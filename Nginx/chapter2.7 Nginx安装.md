#### Nginx安装：
- 获取nginx认证钥匙以便包管理器认证nginx包
wget http://nginx.org/keys/nginx_signing.key

- 添加key
sudo apt-key add nginx_signing.key

- 末尾添加下载源
vi /etc/apt/sources.list
```
deb http://nginx.org/packages/ubuntu/ xenial nginx
deb-src http://nginx.org/packages/ubuntu/ xenial nginx
```
- 更新apt-get
apt-get update
此处更新的source.list中的源


- 安装
apt-get install nginx


- 检查Nginx
nginx -V
出现安装依赖

nginx -v
出现版本信息

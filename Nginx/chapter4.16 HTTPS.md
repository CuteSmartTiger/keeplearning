HTTPS
对传输信息加密与身份认证

对称加密



非对称加密


CA签名证书，防止中间人伪造客户端与服务端



### 生成密钥与CA证书
[参考文章](https://blog.csdn.net/shion0305/article/details/73776449)
先查看有没有安装openSLL
openssl version


nginx -v
--with-http_ssl_module

第一步：生成key密钥
cd /etc/nginx目录下

查看open相关的包
rpm -qa|grep open

mkdir ssl_key

生成密钥
openssl genrsa -idea -out jesonc.key 1024
提示输入密码，需要记住
生成jesonc.key的文件

生成请求密文，并按提示输入之前的密码
openssl req -new -key jesonc.key -out jesonc.csr

生成jesonc.csr文件

基于个人：
openssl x509 -req -days 3650 in jesonc.csr -signkey jesonc.key -out jseson.crt
3650一定要写，否则默认是三十天


第二步：生成证书的签名请求文件

第三步：生成证书签名文件（CA文件）


Nginx的HTTPS配置示例：
```
server
 {
   #HTTPS默认监听的端口443
   listen       443;
   server_name  116.62.103.228 jeson.t.imooc.io;

   keepalive_timeout 100;

   #开启
   ssl on;
   ssl_session_cache   shared:SSL:10m;
   ssl_session_timeout 10m;

   #ssl_certificate /etc/nginx/ssl_key/jesonc.crt;
   ssl_certificate /etc/nginx/ssl_key/jesonc_apple.crt;
   ssl_certificate_key /etc/nginx/ssl_key/jesonc.key;
   #ssl_certificate_key /etc/nginx/ssl_key/jesonc_nopass.key;

   index index.html index.htm;
   location / {
       root  /opt/app/code;
   }
}

```
配置完后查看443端口

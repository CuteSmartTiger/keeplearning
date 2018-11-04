### geoip_module模块

基于IP地址匹配MaxMind GeoIP 二进制文件，读取IP所在地域信息





### http_geoip_module场景
- 区别国内外

- 区别国内城市地域做HTTP访问规则


第一步安装：
安装前先检测下载源是否添加
apt-get install nginx-module-geoip

第二步：查看模块，检测是否成功
cd /etc/nginx/modules/  

第三步：编译配置文件
vi /etc/nginx/nginx.conf

加载模块信息,在文件开头写入：
```
load_module "modules/ngx_http_geoip_module.so";
load_module "modules/ngx_stream_geoip_module.so";
```
下载地域相关的文件：
名字为：
GeoLiteCoutry/GeoIP.dat.gz
GeoLiteCity.dat.gz

然后解压

配置
vi /etc/nginx/nginx.d/test_geo.conf
```
#加载信息
geoip_country /etc/nginx/geoip/GeoIP.dat;
geoip_city /etc/nginx/geoip/GeoLiteCity.dat;
```

kibana安装脚本
```shell
# 下载kibana的tar.gz的软件包
wget https://artifacts.elastic.co/downloads/kibana/kibana-5.4.0-linux-x86_64.tar.gz

# 解压kibana的tar包
tar -xzf kibana-5.4.0-linux-x86_64.tar.gz

# 进入解压好的kibana
mv kibana-5.4.0-linux-x86_64 /usr/local

# 创建kibana的软连接
ln -s /usr/local/kibana-5.4.0-linux-x86_64/ /usr/local/kibana

```


进入源码安装的目录
cd /usr/local/src

下载包

查看
screen -ls

进入
screen -r

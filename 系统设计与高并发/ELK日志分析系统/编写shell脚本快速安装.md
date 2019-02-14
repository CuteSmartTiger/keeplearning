- 编写Java安装的shell脚本
```shell
# 添加ppa
sudo add-apt-repository ppa:webupd8team/java

sudo apt-get update

# 安装oracle-java-installer
sudo apt-get install -y  oracle-java8-installer

# 设置系统默认jdk
sudo update-java-alternatives -s java-8-oracle

#查看Java是否安装成功
echo `java -version`
```






```shell
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

sudo apt-get install apt-transport-https

echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list

sudo apt-get update

sudo apt-get install elasticsearch


# 针对logstash的安装
sudo apt-get install logstash

# 创建一个软连接，每次执行命令的时候不用在写安装路劲（默认安装在/usr/share下）
ln -s /usr/share/logstash/bin/logstash /bin/
```

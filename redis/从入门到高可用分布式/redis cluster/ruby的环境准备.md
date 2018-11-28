soft目下下载ruby
wget https://cache.ruby-lang.org/pub/ruby/2.3/ruby-2.3.1.tar.gz

tar -xvf ruby-2.3.1.tar.gz
cd ruby-2.3.1
./configure --prefix=/usr/local/ruby
make && make install

检测ruby是否安装成功ls
ruby -v

cd /usr/local/ruby
cp bin/ruby /usr/local/bin
cp bin/gem /usr/local/bin


安装rubygem redis
wget http://rubygems.org/downloads/redis-3.3.0.gem
gem install -l redis-3.3.0.gem
gem list -- check redis gem

安装redis-trib.rb
cp ${REDIS_HOME}/src/redis-trib.rb /usr/local/bin


-  编写安装脚本
vim /opt/soft/redis-5.0.0/script/ruby.sh
```
wget https://cache.ruby-lang.org/pub/ruby/2.3/ruby-2.3.1.tar.gz
tar -xvf ruby-2.3.1.tar.gz
cd ruby-2.3.1
./configure -prefix=/usr/local/ruby
make
make install


wget http://rubygems.org/downloads/redis-3.3.0.gem
sudo gem install -l redis-3.3.0.gem
sudo gem list -- check redis gem
```





自己的安装方法：
sudo apt-get install ruby-full

检测ruby是否安装成功ls
ruby -v

wget http://rubygems.org/downloads/redis-3.3.0.gem
sudo gem install -l redis-3.3.0.gem
sudo gem list -- check redis gem

查看redis-trib.rb
/opt/soft/redis-5.0.0/src/redis-trib.rb

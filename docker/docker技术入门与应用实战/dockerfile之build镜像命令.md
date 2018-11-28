#### 使用Dockerfile文件构建镜像
Usage:  docker build [OPTIONS] PATH | URL |

#### -Options:
-t, --tag list  # 镜像名称
-f, --file string  # 指定Dockerfile文件位置


#### 示例：
```
docker build .   # 默认找当前目录以Dockerfile为命名的文件
docker build -t shykes/myapp .
docker build -t shykes/myapp -f /path/Dockerfile /path
docker build -t shykes/myapp - < Dockerfile
docker build -t shykes/myapp - < context.tar.gz
docker build -t shykes/myapp http://www.example.com/Dockerfile
docker build -f shykes/myapp http://www.example.com/contex.tar.gz
```

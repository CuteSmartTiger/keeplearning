- [sed命令用法](https://www.cnblogs.com/maxincai/p/5146338.html)

```SHELL
#删除配置文件中的#号注释行
sed -ri '/^[ \t]*#/d' file.conf

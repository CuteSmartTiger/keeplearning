- SELECT 模型
逻辑代码：
while True{
  选择信息不为空的流，这样CPU不会空耗
  select(streams[])
  for i in streams[]{
    if i has data
    read until unavailable
  }
}



- Epoll模型
从select模型演变而来，优势：
一则：解决select模型对文件句柄FD打开限制

二则：采用callback函数回调机制优化模型效率

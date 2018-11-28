#### RUN、CMD和ENTRYPOINT指令区别
1. RUN在building时运行，可以写多条
2. CMD和ENTRYPOINT在运行container时运行，只能写一条，如果写多条，最后一条生效。
3. CMD在run时可以被COMMAND覆盖，ENTRYPOINT不会被COMMAND覆盖，但可以指定—entrypoint覆盖。

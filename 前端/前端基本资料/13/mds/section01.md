## 主动触发与自定义事件

** 主动触发 **  
可使用jquery对象上的trigger方法来触发对象上绑定的事件。



** 自定义事件 **  
除了系统事件外，可以通过bind方法自定义事件，然后用tiggle方法触发这些事件。
```
//给element绑定hello事件
element.bind("hello",function(){
    alert("hello world!");
});
       
//触发hello事件
element.trigger("hello");
```






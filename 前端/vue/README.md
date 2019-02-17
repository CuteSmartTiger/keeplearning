属性绑定
MVVM 双向数据绑定
dom节点
localstorage缓存对象


- 生命周期函数(挂载与销毁两个重点)
定义：组件挂载、以及组件更新、组件销毁、的时候触发的一系列的方法  这些方法就叫做生命周期函数
作用：mounted()与methods方法同级
示例：
  ```
  mounted(){     /*请求数据，操作dom , 放在这个里面  mounted*/
             console.log('模板编译完成4');

  beforeDestroy(){   /*页面销毁的时候要保存一些数据，就可以监听这个销毁的生命周期函数*/
           console.log('实例销毁之前');

  ```


<hr >

- 组件（手动挂载，或者路由动态挂载）：
创建组件
引入组件
挂载组件
模板中使用

```
<!-- 局部样式 scoped -->
<style lang="scss" scoped>

    /*css  局部作用域  scoped*/

    h2{

        color:red
    }


</style>
```



- 请求数据
  1. 插件vue-resource（可以获取请求数据的body，headers，status,可以在浏览器调试console时看）
  ```
  /*使用vue-resource请求数据的步骤

  1、需要安装vue-resource模块，  注意加上  --save

  npm install vue-resource --save /  cnpm install vue-resource --save  

  2、main.js引入 vue-resource

    import VueResource from 'vue-resource';

  3、main.js  Vue.use(VueResource);

  4、在组件里面直接使用

    this.$http.get(地址).then(function(){

    })  
  ```
  2.axios  的使用
  ``` /*
    1、安装  cnpm  install  axios --save

    2、哪里用哪里引入axios

    ```


- Vue父组件给子组件传值 Vue父组件给子组件传方法  Vue父组件把整个实例传给子组件
  1. 方法一：
    ```
    1.父组件调用子组件的时候 绑定动态属性
        <v-header :title="title"></v-header>
    2、在子组件里面通过 props接收父组件传过来的数据
    ```

  2. 父组件主动获取子组件的数据和方法：
  ```
    1.调用子组件的时候定义一个ref

        <v-header ref="header"></v-header>

    2.在父组件里面通过

        this.$refs.header.属性

        this.$refs.header.方法

    ```
    3. 子组件主动获取父组件的数据和方法：  
    ```
    this.$parent.数据

    this.$parent.方法
    ```

- 非父子组件传值（此方法稍微麻烦）
  ```
  1、新建一个js文件   然后引入vue  实例化vue  最后暴露这个实例

  2、在要广播的地方引入刚才定义的实例

  3、通过 VueEmit.$emit('名称','数据')

  4、在接收收数据的地方通过 $om接收广播的数据
    VueEmit.$on('名称',function(){
    })
  ```

- 通过路由加载组件
  ```
    1. vue-router 介绍官网https://router.vuejs.org/zh/
    详细方法参见“17Vue中的路由 以及默认路由跳转”
  ```

- 路由
  1. [动态路由传值与get传值](https://router.vuejs.org/zh/guide/essentials/dynamic-matching.html#%E5%93%8D%E5%BA%94%E8%B7%AF%E7%94%B1%E5%8F%82%E6%95%B0%E7%9A%84%E5%8F%98%E5%8C%96)

  2. 路由结合请求数据实现访问网页



  3. [如何很好的理解跨域](https://blog.csdn.net/hansexploration/article/details/80314948)


  4. Vue路由编程式导航(通过js实现页面跳转)以及hash模式


- VueUI框架MintUI ，看官方文档或者在GitHub上搜索demo实例

-

-  webpack

- 路由模块化

- Vuex 的使用 State Mutation(用的频率高) Getter Action（后两种频率不高）  以及实现不同组件新闻数据共享 以及新闻数据的持久化（vuex小型项目不推荐使用）



##### 补充说明
- [js的练习网站](http://www.w3school.com.cn/js/js_htmldom_elements.asp)

- [快速布局element](http://element-cn.eleme.io/#/zh-CN/component/installation)

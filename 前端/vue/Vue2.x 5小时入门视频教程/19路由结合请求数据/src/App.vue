<template>


  <div id="app"> 

    <header class="header">

      <router-link to="/home">首页</router-link>
      <router-link to="/news">新闻</router-link>

    </header>

    <hr>

       <router-view></router-view>

  </div>
</template>

<script>


/*1、不同路由传值：动态路由

    1、配置动态路由

       routes: [
        // 动态路径参数 以冒号开头
        { path: '/user/:id', component: User }
      ]


    2、在对应的页面

      this.$route.params获取动态路由的值


*/

   export default {     
      data () { 
        return {
         
         msg:'你好vue'
        }
      }
     
    }
</script>
<style lang="scss">

  .header{


    height:4.4rem;

    background:#000;

    color:#fff;

    line-height:4.4rem;

    text-align:center;

    a{
      color:#fff;

      padding:0 2rem

    }
  }
</style>
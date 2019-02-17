<template>


  <div id="app"> 

    <header class="header">

      <router-link to="/home">首页</router-link>
      <router-link to="/news">新闻</router-link>
       <router-link to="/user">用户</router-link>
    </header>

    <hr>
    <router-view></router-view>

  </div>
</template>
<script>

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
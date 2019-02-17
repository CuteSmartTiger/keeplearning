<template>


  <div id="app"> 


    <router-link to="/home">首页</router-link>
    <router-link to="/news">新闻</router-link>

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


</style>
<template>


  <div id="app"> 
    

     <v-home></v-home>



     <hr >

     <br>

     <v-news></v-news>
     
  </div>
</template>

<script>

  /*
  1、引入组件

  2、挂载组件

  3、在模板中使用
  */
   import Home from './components/Home.vue';

   import News from './components/News.vue';

   export default {     
      data () { 
        return {
         
         msg:'你好vue'
        }
      },
      components:{   /*前面的组件名称不能和html标签一样*/
        'v-home':Home,
        'v-news':News
      }
    }
</script>


<style lang="scss">


</style>
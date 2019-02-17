<template>


  <div id="app"> 
    

     <v-home></v-home>

   
     
  </div>
</template>

<script>

  /*
  1、引入组件

  2、挂载组件

  3、在模板中使用


  生命周期函数/生命周期钩子： 

    组件挂载、以及组件更新、组件销毁、的时候触发的一系列的方法  这些方法就叫做生命周期函数
  */
   import Home from './components/Home.vue';

   export default {     
      data () { 
        return {
         
         msg:'你好vue'
        }
      },
      components:{   /*前面的组件名称不能和html标签一样*/
        'v-home':Home,       
      },
      mounted(){
        console.log('我是一个声明周期函数');
      }
    }
</script>


<style lang="scss">


</style>
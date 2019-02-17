<template>


  <div id="app"> 
    

     <v-home></v-home>

    <br>
    <hr>
    <br>
    <v-news></v-news>
     

  </div>
</template>

<script>

  /*非父子组件传值
  1、新建一个js文件   然后引入vue  实例化vue  最后暴露这个实例


  2、在要广播的地方引入刚才定义的实例


  3、通过 VueEmit.$emit('名称','数据')


  4、在接收收数据的地方通过 $om接收广播的数据
    VueEmit.$on('名称',function(){


    })

  
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
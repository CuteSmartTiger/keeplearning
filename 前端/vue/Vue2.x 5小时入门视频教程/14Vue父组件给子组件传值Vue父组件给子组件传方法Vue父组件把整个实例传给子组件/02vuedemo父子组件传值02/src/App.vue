<template>


  <div id="app"> 
    

     <v-home></v-home>
  
     
  </div>
</template>

<script>

   import Home from './components/Home.vue';

   export default {     
      data () { 
        return {
         
         msg:'你好vue'
        }
      },
      components:{   /*前面的组件名称不能和html标签一样*/
        'v-home':Home,       
      }
     
    }
</script>


<style lang="scss">


</style>
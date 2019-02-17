<template>
    <div>
        <v-header></v-header>
        <h2>这是一个新闻组件</h2>
    
        <ul>

            <li >

                    111111
            </li>
            <li>
            
              2222
            </li>
            <li>
            
              333333
            </li>
        </ul>
    </div>

</template>

<script>

  //引入头部组件

   import Header from './Header.vue';

    export default {

      

        data(){

            return{

                msg:'我是一个新闻组件'
            }
        },components:{

            'v-header':Header
        }

    };
</script>

<style lang="scss">
    

    
</style>
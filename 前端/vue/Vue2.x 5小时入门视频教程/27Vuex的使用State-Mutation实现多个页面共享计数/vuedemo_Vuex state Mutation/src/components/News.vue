<template>    
    <div id="news">    
       我是新闻组件   --{{this.$store.state.count}}



        
        <br>

        <button @click="incCount()">增加数量</button>
        
    </div>

</template>


<script>
    //1. 引入store

    import store from '../vuex/store.js';

    export default{
        data(){
            return {               
               msg:'我是一个新闻组件'
              
            }
        },
        store,
        methods:{

            incCount(){

                this.$store.commit('incCount');
            }
        }
    }

</script>





<style lang="scss" scoped>
    
    .list{

        li{
            height:3.4rem;

            line-height:3.4rem;

            boder-bottom:1px solid #eee;

            font-size:1.6rem;

            a{

                color:#666;

                
            }
        }
    }

</style>
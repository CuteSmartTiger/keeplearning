<template>
    <!-- 所有的内容要被根节点包含起来 -->
    <div id="home">
    
       我是首页组件

       <br>

       <button @click="emitNews()">给News组件广播数据</button>

        <br>

    </div>

</template>


<script>

//引入 vue实例


    import VueEvent from '../model/VueEvent.js';

    export default{
        data(){
            return {               
               msg:'我是一个home组件',
               title:'首页111'
            }
        },methods:{

            emitNews(){
                //广播数据

                VueEvent.$emit('to-news',this.msg)

            }
        },
        mounted(){

            //监听news 广播的数据
            VueEvent.$on('to-home',function(data){
                console.log(data);
            })
        }

    }

</script>

<style lang="scss" scoped>


    
</style>
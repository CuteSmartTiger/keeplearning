<template>
    <!-- 所有的内容要被根节点包含起来 -->
    <div id="home">

            <v-header></v-header>
            <br>
            <hr>

            <h2>这是一个首页组件--{{msg}}</h2>

            <button @click="run()">执行run方法</button>


    </div>

</template>


<script>
    //引入头部组件

    import Header from './Header.vue';


    export default{

        data(){

            return {

                msg:'我是一个首页组件msg'
            }
        },
        methods:{

            run(){

                alert(this.msg);
            }
        },
        components:{

            'v-header':Header
        }

    }

</script>

<style lang="scss" scoped>

    /*css  局部作用域  scoped*/

    h2{

        color:red
    }

    
</style>
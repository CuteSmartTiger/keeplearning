<template>
    <!-- 所有的内容要被根节点包含起来 -->
    <div id="home">
    
        <v-header :title="title"></v-header>

        <hr>
         首页组件   

    </div>

</template>


<script>


/*
父组件给子组件传值

    1.父组件调用子组件的时候 绑定动态属性
        <v-header :title="title"></v-header>

    2、在子组件里面通过 props接收父组件传过来的数据





*/

    import Header from './Header.vue';

    export default{
        data(){
            return {               
               msg:'我是一个home组件',
               title:'首页111'
            }
        },
        components:{

            'v-header':Header
        },
        methods:{

            run(data){

                alert('我是Home组件的run方法'+data);
            }
        }


    }

</script>

<style lang="scss" scoped>

    /*css  局部作用域  scoped*/

    h2{

        color:red
    }

    
</style>
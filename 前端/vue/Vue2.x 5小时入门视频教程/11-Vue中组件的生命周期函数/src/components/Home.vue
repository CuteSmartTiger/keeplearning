<template>
    <!-- 所有的内容要被根节点包含起来 -->
    <div id="home">

            <v-header></v-header>
            <br>
            <hr>
            
            <v-life v-if="flag"></v-life>

             <br>
              <br>
               <br>

            <button @click="flag=!flag">挂载以及卸载life组件</button>

    </div>

</template>


<script>
    //引入头部组件

    import Header from './Header.vue';

    
    import Life from './Lify.vue';



    export default{

        data(){

            return {

                msg:'我是一个首页组件msg',
                flag:true
            }
        },
        methods:{

            run(){

                alert(this.msg);
            }
        },
        components:{

            'v-header':Header,
            'v-life':Life
        }

    }

</script>

<style lang="scss" scoped>

    /*css  局部作用域  scoped*/

    h2{

        color:red
    }

    
</style>
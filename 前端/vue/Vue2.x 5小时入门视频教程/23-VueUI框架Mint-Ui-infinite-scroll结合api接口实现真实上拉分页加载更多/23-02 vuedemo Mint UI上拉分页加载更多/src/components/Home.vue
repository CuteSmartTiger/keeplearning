<template>
    <!-- 所有的内容要被根节点包含起来 -->
    <div id="home">    
       我是首页组件


        <button @click="goNews()">通过js跳转到新闻页面</button>


        <mt-button type="default">default</mt-button>
        <br>
        <mt-button type="primary">primary</mt-button>



        <mt-index-list>
        <mt-index-section index="A">
            <mt-cell title="Aaron"></mt-cell>
            <mt-cell title="Alden"></mt-cell>
            <mt-cell title="Austin"></mt-cell>
        </mt-index-section>
        <mt-index-section index="B">
            <mt-cell title="Baldwin"></mt-cell>
            <mt-cell title="Braden"></mt-cell>
        </mt-index-section>

        
        <mt-index-section index="C">
            <mt-cell title="ccc"></mt-cell>
            <mt-cell title="ccccc"></mt-cell>
        </mt-index-section>

         <mt-index-section index="D">
            <mt-cell title="DDD"></mt-cell>
            <mt-cell title="DDDD"></mt-cell>
        </mt-index-section>
        
        <mt-index-section index="Z">
            <mt-cell title="Zack"></mt-cell>
            <mt-cell title="Zane"></mt-cell>
        </mt-index-section>
        </mt-index-list>
       
    </div>
</template>


<script>
    export default{
        data(){
            return {               
               msg:'我是一个home组件'
             
            }
        },
        methods:{

            goNews(){


                    this.$router.push({ name: 'news'})


                

            }
        }
    }

</script>

<style lang="scss" scoped>
    
</style>
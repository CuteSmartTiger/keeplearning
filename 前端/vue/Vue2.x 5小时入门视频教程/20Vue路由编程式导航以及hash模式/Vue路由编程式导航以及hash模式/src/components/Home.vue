<template>
    <!-- 所有的内容要被根节点包含起来 -->
    <div id="home">    
       我是首页组件


        <button @click="goNews()">通过js跳转到新闻页面</button>
       
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


                // 注意：官方文档写错了


                //第一种跳转方式

                // this.$router.push({ path: 'news' })


                // this.$router.push({ path: '/content/495' });







                //另一种跳转方式

                    //   { path: '/news', component: News,name:'news' },


                    // router.push({ name: 'news', params: { userId: 123 }})


                    this.$router.push({ name: 'news'})


                

            }
        }
    }

</script>

<style lang="scss" scoped>
    
</style>
<template>
   
    <div id="content">    
       我是详情页面
    </div>
</template>


<script>
    


    export default{

        data(){

            return{

                msg:'数据'
            }
        },
        mounted(){

                console.log(this.$route.params);  /*获取动态路由传值*/

        }

    }
</script>
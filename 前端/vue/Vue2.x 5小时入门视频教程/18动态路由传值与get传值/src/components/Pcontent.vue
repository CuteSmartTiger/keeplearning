<template>
   
    <div id="content">    
      商品详情
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

              //获取get传值


              console.log(this.$route.query);
        }

    }
</script>
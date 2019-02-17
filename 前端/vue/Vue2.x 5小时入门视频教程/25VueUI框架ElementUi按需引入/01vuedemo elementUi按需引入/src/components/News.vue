<template>    
    <div id="news">    
       我是新闻组件   

    </div>

</template>


<script>

    export default{
        data(){
            return {               
               msg:'我是一个新闻组件'
              
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
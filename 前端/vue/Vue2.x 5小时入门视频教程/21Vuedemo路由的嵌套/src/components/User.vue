<template>
    <!-- 所有的内容要被根节点包含起来 -->
    <div id="user">    
      

        <div class="user">    
      
                    <div class="left">    
                        <ul>
                            <li>
                               <router-link to="/user/useradd"> 增加用户</router-link>
                            </li>


                            <li>
                                 <router-link to="/user/userlist"> 用户列表</router-link>
                            </li>
                        </ul>


                
                    </div>

                    <div class="right">    
      
                         <router-view></router-view>

       
                     </div>

       
         </div>
       
    </div>
</template>


<script>
    export default{
        data(){
            return {               
               msg:'我是一个user组件'
             
            }
        }       
    }

</script>

<style lang="scss" scoped>


    .user{

        display:flex;

        .left{

            width:200px;

            min-height:400px;

            border-right:1px solid #eee;

            li{

                line-height:2;
            }
        }

        .right{
            flex:1;
        }

    }
</style>
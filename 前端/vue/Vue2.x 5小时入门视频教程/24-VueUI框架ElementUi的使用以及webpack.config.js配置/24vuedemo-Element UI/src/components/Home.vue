<template>
    <!-- 所有的内容要被根节点包含起来 -->
    <div id="home">    
       我是首页组件
    
        <el-button type="success">成功按钮</el-button>
        <el-button type="warning">警告按钮</el-button>
        <el-button type="danger">危险按钮</el-button>

        <br>

        <i style="font-size:40px;" class="el-icon-menu"></i>

         <el-rate v-model="value1"></el-rate>
       
    </div>
</template>


<script>
    export default{
        data(){
            return {               
               msg:'我是一个home组件',
                value1: null,
             
            }
        }
    }

</script>

<style lang="scss" scoped>
    
</style>
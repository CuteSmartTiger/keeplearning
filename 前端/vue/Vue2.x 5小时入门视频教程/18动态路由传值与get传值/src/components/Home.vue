<template>
    <!-- 所有的内容要被根节点包含起来 -->
    <div id="home">    
       我是首页组件

        <ul>
            <li v-for="(item,key) in list">
                <router-link :to="'/pcontent?id='+key">{{key}}--{{item}}</router-link>
            </li>
        </ul>
    </div>
</template>


<script>
    export default{
        data(){
            return {               
               msg:'我是一个home组件',
               list:['商品111111','商品222222','商品333333']    
            }
        }
    }

</script>

<style lang="scss" scoped>
    
</style>
<template>
    <!-- 所有的内容要被根节点包含起来 -->
    <div id="home">
         首页组件

        <button @click="getData()">请求数据</button>
        <hr>
        <br>
       
        <ul>
            <li v-for="item in list">
            
                {{item.title}}
              {{statusCode}}
              {{statusText}}
            </li>
        </ul>
    

    </div>

</template>


<script>

/*

请求数据的模板

    axios  的使用

    1、安装  cnpm  install  axios --save


    2、哪里用哪里引入axios

    
*/
   
   import Axios from 'axios';

    export default{
        data(){
            return {               
                list:[],
              statusCode:'',
              statusText:''
            }
        },
        methods:{

            getData(){
                
                var api='http://www.phonegap100.com/appapi.php?a=getPortalList&catid=20&page=1';
                Axios.get(api).then((response)=>{
                  console.log(response)
                    this.list=response.data.result;
                    this.statusCode=response.status;
                    this.statusText=response.statusText
                }).catch((error)=>{
                    console.log(error);

                })

            }
        },
        mounted(){  /*生命周期函数*/

            this.getData();

        }
       

    }

</script>

<style lang="scss" scoped>

    /*css  局部作用域  scoped*/

    h2{

        color:red
    }

    
</style>

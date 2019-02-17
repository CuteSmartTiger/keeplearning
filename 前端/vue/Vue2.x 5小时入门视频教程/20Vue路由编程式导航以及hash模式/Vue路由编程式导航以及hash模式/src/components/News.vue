<template>    
    <div id="news">    
       我是新闻组件   


     <ul class="list">
        <li v-for="(item,key) in list">
             <router-link :to="'/content/'+item.aid">{{item.title}}</router-link>
        </li>
     </ul>
          
    </div>

</template>


<script>

    export default{
        data(){
            return {               
               msg:'我是一个新闻组件'  ,    
               list:[]        
            }
        },
        methods:{

            requestData(){

                //jsonp请求的话  后台api接口要支持jsonp

                var api='http://www.phonegap100.com/appapi.php?a=getPortalList&catid=20&page=1';

                this.$http.jsonp(api).then((response)=>{

                   console.log(response);

                   //注意：用到this要注意this指向

                   this.list=response.body.result;


                },function(err){

                        console.log(err);
                })
            }
        },
        mounted(){

            this.requestData();
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
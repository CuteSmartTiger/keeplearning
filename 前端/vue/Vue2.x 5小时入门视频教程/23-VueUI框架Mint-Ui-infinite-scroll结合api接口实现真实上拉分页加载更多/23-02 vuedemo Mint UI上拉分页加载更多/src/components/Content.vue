<template>
   
    <div id="content">    
        <h2>{{list.title}}</h2>

        <div v-html="list.content"></div>
    </div>
</template>


<script>
    


    export default{

        data(){

            return{

                msg:'数据',
                list:[]
            }
        },
        mounted(){

               // console.log(this.$route.params);  /*获取动态路由传值*/

                var aid=this.$route.params.aid;

                //调用请求数据的方法

                this.requestData(aid);

        },
        methods:{

            requestData(aid){

                //get请求如果跨域的话 后台php java 里面要允许跨域请求

                var api='http://www.phonegap100.com/appapi.php?a=getPortalArticle&aid='+aid;


                this.$http.get(api).then((response)=>{
                        console.log(response);

                        this.list=response.body.result[0];

                },(err)=>{

                    console.log(err)
                })
            }
        }

    }
</script>

<style lang="scss">


#content{

    padding:1rem;

    line-height:2;

    img{

        max-width:100%;
    }
}
    
</style>
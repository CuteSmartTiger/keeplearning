<template>    
    <div id="news">    
       我是新闻组件   

        <ul
        v-infinite-scroll="loadMore"
        infinite-scroll-disabled="loading"
        infinite-scroll-distance="10" class="list">
            <li v-for="item in list">{{ item.title }}</li>
        </ul>   

        <div>loading....</div>
    </div>

</template>


<script>

    export default{
        data(){
            return {               
               msg:'我是一个新闻组件'  ,    
               list:[]  ,
               page:1,               
               loading:false
            }
        },
        methods:{

            loadMore() {                
               this.requestData(); 
                
            },
            requestData(){
                
                this.loading=true;  /*请求数据的开关*/

                var api='http://www.phonegap100.com/appapi.php?a=getPortalList&catid=20&page='+this.page;   


                this.$http.get(api).then((response)=>{

                        this.list=this.list.concat(response.body.result);

                        ++this.page;  /*每次请求完成page++*/
 
                        //判断最后一页是否有数据
                        if(response.body.result.length<20){
                            
                                this.loading=true;     /*终止请求*/
                        }else{
                                this.loading=false;     /*继续请求*/
                        }
                        
                },(err)=>{
                        console.log(err);
                })     

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
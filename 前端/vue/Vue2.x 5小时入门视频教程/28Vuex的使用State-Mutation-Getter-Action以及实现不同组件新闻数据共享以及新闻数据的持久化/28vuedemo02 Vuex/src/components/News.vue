<template>    
    <div id="news">    
       我是新闻组件   --{{this.$store.state.count}}



        
        <br>

        <button @click="incCount()">增加数量</button>

                <br><br>
                <br><br>

                <ul>
                    <li v-for="item in list">
                    
                        {{item.title}}
                    </li>
                </ul>

                        
    </div>

</template>


<script>
    //1. 引入store

    import store from '../vuex/store.js';

    export default{
        data(){
            return {               
               msg:'我是一个新闻组件',
               list:[]
              
            }
        },
        store,
        methods:{

            incCount(){

                this.$store.commit('incCount');
            },

            requestData(){

                  //请求数据

                    var api='http://www.phonegap100.com/appapi.php?a=getPortalList&catid=20&page=1';


                    this.$http.get(api).then((response)=>{
                        console.log(response);

                        //注意this指向

                        this.list=response.body.result;

                        //数据放在store里面

                        this.$store.commit('addList',response.body.result);



                    },function(err){

                            console.log(err);

                    })
            }
        },mounted(){


            //判断 store里面有没有数据
            var listData=this.$store.state.list;

            console.log(listData.length);

            if(listData.length>0){
                    this.list=listData;

            }else{

                 this.requestData();

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
<template>    
    <div id="news">    
       我是用户组件


       <br>

       <v-actionsheet></v-actionsheet>


        <br>
        <mt-button @click.native="flag = true" size="large">选择用户头像</mt-button>
        <mt-actionsheet :actions="actions" v-model="flag"></mt-actionsheet>

        
    </div>

</template>


<script>

    import ActionSheet from './ActionSheet.vue';

    export default{
        data(){
            return {               
               msg:'我是一个新闻组件'  ,    
               list:[],
               flag:false,
               actions:[]
            }
        },
        components:{

           'v-actionsheet':ActionSheet
        },

        methods:{


            takePhoto(){

                alert('执行拍照');
            },
             openAlbum(){

                alert('打开相册');
            }
        }

        ,

        mounted() {
            this.actions = [{
                name: '拍照',
                method: this.takePhoto
            }, {
                name: '从相册中选择',
                method: this.openAlbum
            }];
        
        }
       
    }

</script>

<style lang="scss" scoped>
  

</style>
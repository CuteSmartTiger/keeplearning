<template>


    <div>
    
        <h2>我是头部组件</h2>

      
          <button @click="getParentData()">获取父组件的数据和方法</button>

       
    </div>
</template>




<script>
    
export default{


    data(){

        return{
            msg:'子组件的msg'
        }
    },
    methods:{
       
            run(){

                alert('我是子组件的run方法')
            },
            getParentData(){


                /*
                子组件主动获取父组件的数据和方法：  


                this.$parent.数据

                this.$parent.方法

                
                */
                // alert(this.$parent.msg);

                this.$parent.run();
            }
    }
    
}

</script>

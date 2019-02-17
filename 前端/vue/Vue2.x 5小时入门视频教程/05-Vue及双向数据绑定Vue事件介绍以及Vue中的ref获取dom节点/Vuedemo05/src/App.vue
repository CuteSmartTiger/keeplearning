<template>


  <div id="app">  
    
      <h2>{{msg}}</h2>

      <input type="text" v-model='msg' />


      <button v-on:click="getMsg()">获取表单里面的数据get</button>


      <button v-on:click="setMsg()">设置表单的数据set</button>

      <br>
      <br>
      <hr>

      <br>
      <br>
      <input type="text" ref="userinfo" />
      <br>
      <br>
      <div ref="box">我是一个box</div>

      <br>
      <br>
      <button v-on:click="getInputValue()">获取第二个表单里面的数据</button>

      

  </div>
</template>

<script>


  /*
  双向数据绑定   MVVM   vue就是一个MVVM的框架。

  M  model

  V  view

  MVVM：  model改变会影响视图view，view视图改变反过来影响model


  双向数据绑定必须在表单里面使用。


  */

    export default {     
      data () {  /*业务逻辑里面定义的数据*/
        return {
          msg: '你好vue'         
        }
      },methods:{   /*放方法的地方*/

          getMsg(){

              // alert('vue方法执行了');

              //方法里面获取data里面的数据


                alert(this.msg);



          },
          setMsg(){
              this.msg="我是改变后的数据";

          }, getInputValue(){

              //获取ref定义的dom节点
              console.log(this.$refs.userinfo);


              this.$refs.box.style.background='red';

              alert(this.$refs.userinfo.value);


              
              
          }

      }



    }
</script>


<style lang="scss">



</style>

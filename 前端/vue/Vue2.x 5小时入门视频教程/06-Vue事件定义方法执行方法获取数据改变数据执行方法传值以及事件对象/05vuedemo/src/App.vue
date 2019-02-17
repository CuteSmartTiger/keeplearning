<template>


  <div id="app">  
    
<!-- 
      <img v-bind:src='url' />

      <img :src='url' /> -->

      {{msg}}
    <br>
    <br>
    <br>


      <button v-on:click="run1()">执行方法的第一种写法</button>
      <br><br><br>

      <button @click="run2()">执行方法的第二种写法</button>

      <br>
      <br>
      <br>
     
      <button @click="getMsg()">获取data里面的msg</button>


      <br>
      <br>
      <br>
      
      <button @click="setMsg()">改变data里面的msg</button>


      <br>
      <br>
      <br>
      
      <button @click="requestData()">请求数据</button>

      <hr>

      <ul>

        <li v-for="(item,key) in list">
          {{key}}---   {{item}}
        </li>
      </ul>

      <br>
      <br>
      <br>
      <button @click="deleteData('111')">执行方法传值111</button>

      <br>
      <br>
      <button @click="deleteData('222')">执行方法传值2222</button>
      <br>
      <br>
      <br>
      <button data-aid='123' @click="eventFn($event)">事件对象</button>      

  </div>
</template>

<script>



    export default {     
      data () { 
        return {
          msg: '你好vue',
          list:[]      
        }
      },
      methods:{

        run1:function(){

          alert('这是一个方法');

        },

        run2(){
          alert('这是另一个方法');
        },
        getMsg(){
            alert(this.msg);
        },
        setMsg(){

          this.msg="我是改变后的数据"
        },
        requestData(){

            for(var i=0;i<10;i++){

              this.list.push('我是第'+i+'条数据');
            }
        }
        ,
        deleteData(val){

            alert(val);
        },
        eventFn(e){
          console.log(e);

          // e.srcElement  dom节点



          e.srcElement.style.background='red';


          console.log(e.srcElement.dataset.aid);  /*获取自定义属性的值*/
        }

      }

    }
</script>


<style lang="scss">



</style>

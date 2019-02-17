<template>


  <div id="app">  
    
      <h2>{{msg}}</h2>

      <br>

      <div v-bind:title="title">鼠标瞄上去看一下</div>


      <img src="https://www.itying.com/themes/itying/images/logo.gif" />

       <br>

        <br>
       
       <!-- 绑定属性 -->

       <img v-bind:src="url" />

        <br>
        <img :src="url" />

        <br>

        <br>
        {{h}} 


        <!-- 绑定html -->


        <div v-html="h">

        </div>


        <!-- 绑定数据的另一种方法 -->

       <div v-text="msg">
       </div>


    


       <!-- v-bind:class  :class的使用 -->


       <div v-bind:class="{'red':flag}">

        我是一个div
       </div>

    <br>
    <br>

    <div :class="{'red':flag,'blue':!flag}">
    
      我是另一个div
    </div>

     
      <br>
      <br>
      <!-- 循环数据 第一个数据高量 -->
      <ul>
        <li v-for="(item,key) in list">
          {{key}}---{{item}}
        </li>
      </ul>
      
        <br>
        <br>
      <ul>
        <li v-for="(item,key) in list"  :class="{'red':key==0,'blue':key==1}">
          {{key}}---{{item}}
        </li>
      </ul>
      <br>
      <br>


      <!-- v-bind:style  :style的使用 -->

    <div class="box" v-bind:style="{'width':boxWdith+'px'}">

      我是另一个div
    </div>
      

  </div>
</template>

<script>
    export default {     
      data () {  /*业务逻辑里面定义的数据*/
        return {
          msg: '你好vue',
          title:'我是一个title',
          url:'https://www.itying.com/themes/itying/images/logo.gif',

          h:'<h2>我是h2</h2>',
          list:['1111','2222','3333'],
          flag:false,
          boxWdith:500
        }
      }
    }
</script>


<style lang="scss">


  .red{

    color: red;
  }
  .blue{

    color:blue;
  }

  .box{

    height: 100px;

    width: 100px;

    background: red;
  }

</style>

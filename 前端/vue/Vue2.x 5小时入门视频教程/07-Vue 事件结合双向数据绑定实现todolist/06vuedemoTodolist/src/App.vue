<template>


  <div id="app"> 
      
      <input type="text" v-model='todo' />
      <button @click="doAdd()">+增加</button>

      <br>

      <hr>

      <br>

      <ul>

        <li v-for="(item,key) in list">

          {{item}}   ----  <button @click="removeData(key)">删除</button>
        </li>
      </ul>


  </div>
</template>

<script>

    export default {     
      data () { 
        return {
          todo:'请输入任务清单' ,
          list:[]
        }
      },
      methods:{

        doAdd(){
            //1、获取文本框输入的值   2、把文本框的值push到list里面

            this.list.push(this.todo);

            this.todo='';
        },
        removeData(key){

            // alert(key)

            //splice  js操作数组的方法

            this.list.splice(key,1);
        }
      }

    }
</script>


<style lang="scss">



</style>

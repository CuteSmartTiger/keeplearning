<template>


  <div id="app"> 
      <!--添加键盘事件-->
      <input type="text" v-model='todo' @keydown="doAdd($event)" />


      <br>

      <hr>

      <br>

    <h2>进行中</h2>
          <ul>

            <li v-for="(item,key) in list" v-if="!item.checked">

              <input type="checkbox" v-model='item.checked'> {{item.title}}   ----  <button @click="removeData(key)">删除</button>
            </li>
          </ul>


    <br>
    <h2>已完成</h2>
    <ul class="finish">

      <li v-for="(item,key) in list" v-if="item.checked">

          <input type="checkbox" v-model='item.checked'> {{item.title}} ----<button @click="removeData(key)">删除</button>
      </li>
    </ul>


    <h2 v-if='ok'>这是一个ok</h2>

    <h2 v-if='!ok'>这是一个No</h2>

    <button @click="getList()">获取list的值</button>

  </div>
</template>

<script>

  /*
       ['录制nodejs','录制ionic']


          [

            {
              title:'录制nodejs',
              checked:true
            },
              {
              title: '录制ionic',
              checked: false
            }
          ]
          
          */

    export default {     
      data () { 
        return {
          // ok:false,
          ok:true,
          todo:'' ,
          list: [

            {
              title: '录制nodejs',
              checked: true
            },
            {
              title: '录制ionic',
              checked: false
            }
          ]

         
        }
      },
      methods:{

        doAdd(e){
              console.log(e.keyCode)

              if(e.keyCode==13){
              //1、获取文本框输入的值   2、把文本框的值push到list里面
              this.list.push({

                title: this.todo,
                checked: false
              })

              this.todo='';
            }
        },
        removeData(key){

            // alert(key)

            //splice  js操作数组的方法
            this.list.splice(key,1);
        },

        getList(){

          console.log(this.list.values())
          alert(this.list.values())
        }
      }

    }
</script>


<style lang="scss">

.finish{

  
  li{
    background:#eee;
  }
}

</style>

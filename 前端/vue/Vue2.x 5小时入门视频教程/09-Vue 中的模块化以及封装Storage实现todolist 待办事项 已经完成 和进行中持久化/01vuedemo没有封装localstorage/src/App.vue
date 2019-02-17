<template>


  <div id="app"> 
      
      <input type="text" v-model='todo' @keydown="doAdd($event)" />
  
      <hr>
    <br>

    <h2>进行中</h2>

      <ul>

        <li v-for="(item,key) in list" v-if="!item.checked">
           <input type="checkbox" v-model="item.checked" @change="saveList()" /> {{item.title}}   --  <button @click="removeData(key)">删除</button>
        </li>
      </ul>

    <br>  
    <br>
    <h2>已完成</h2>



      <ul>      
        <li v-for="(item,key) in list" v-if="item.checked">
          <input type="checkbox"  v-model="item.checked" @change="saveList()" /> {{item.title}}  -- <button @click="removeData(key)">删除</button>
        </li>
      </ul>
  </div>
</template>

<script>

    export default {     
      data () { 
        return {
         
          todo:'' ,
          list: []
        }
      },
      methods:{

        doAdd(e){
              // console.log(e);
              if(e.keyCode==13){
                  this.list.push({
                    title:this.todo,
                    checked:false
                  })
              }

              localStorage.setItem('list',JSON.stringify(this.list))
        },
        removeData(key){

            this.list.splice(key,1)
           
            localStorage.setItem('list', JSON.stringify(this.list))
        }
        , saveList(){

           localStorage.setItem('list', JSON.stringify(this.list))
        }

      },mounted(){   /*生命周期函数       vue页面刷新就会触发的方法*/

          var list=JSON.parse(localStorage.getItem('list'));

          if(list){  /*注意判断*/
            this.list=list;
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
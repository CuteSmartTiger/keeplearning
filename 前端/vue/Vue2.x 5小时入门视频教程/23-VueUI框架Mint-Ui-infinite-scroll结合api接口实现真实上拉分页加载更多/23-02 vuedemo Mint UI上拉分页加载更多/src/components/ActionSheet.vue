<template>
  <div class="page-actionsheet">
    


    <div class="page-actionsheet-wrapper">
      <mt-button @click.native="sheetVisible = true" size="large">点击上拉 action sheet</mt-button>

     

    </div>    
    <mt-actionsheet :actions="actions" v-model="sheetVisible"></mt-actionsheet>
  
  </div>
</template>

<style>
 /*创建项目的时候必须选 scss*/


  @component-namespace page {
    @component actionsheet {
      @descendent wrapper {
        padding: 0 20px;
        position: absolute 50% * * *;
        width: 100%;
        transform: translateY(-50%);

        button:first-child {
          margin-bottom: 20px;
        }
      }
    }
  }
  
</style>

<script type="text/babel">
  export default {
    data() {
      return {
        sheetVisible: false,
        sheetVisible2: false,
        actions: []
       
      };
    },

    methods: {
      takePhoto() {
        console.log('taking photo');
      },

      openAlbum() {
        console.log('opening album');
      }
    },

    mounted() {
      this.actions = [{
        name: '拍照',
        method: this.takePhoto
      }, {
        name: '从相册中选择',
        method: this.openAlbum
      }];
     
    }
  };
</script>

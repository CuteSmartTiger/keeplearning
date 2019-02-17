<template>
  <div>
    <Card shadow>
      <p slot="title"> 虚拟化环境管理平台</p>
      <Form ref="editForm"   :style="{width:'500px'}">
        <FormItem >版本：{{version}} <a :href="helpUrl" target="_blank">查看帮助文档</a></FormItem>
        <FormItem > <Button type="success" @click="onDownloadDate()" icon="ios-download">点击获取平台日志</Button></FormItem>
      </Form>
    </Card>

  </div>
</template>

<script>
  import {getAboutData,getLog} from '@/api/help'
  import CONFIG from '_conf/config'
  export default {
    name: 'help',
    data() {
      return {
        version:"",
        helpUrl:CONFIG.BASE+'help_platform.pdf'
      }
    },
    methods: {
      handleList() {
        getAboutData().then(res => {
          this.version = res.version;
        },err=> {
          this.version = "获取版本号失败"
        })
      },
      onDownloadDate() {
        getLog().then(res => {
          if (res != null && res.url != undefined && res.url != '') {
            window.location.href = res.url;
          } else {
            this.$Message.error('下载地址获取失败');
          }

        })

      },
    },
    mounted() {
      this.handleList()
    }

  }
</script>
<style lang="less">
  .ivu-form-item .ivu-form-item-content{
    font-size:14px !important;
    a{margin-left:20px;}
  }

</style>

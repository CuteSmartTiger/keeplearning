<template>
    <dvi>
      <Card>
        <Form ref="editForm" :model="editForm" :label-width="120" :rules="ruleValidate"  :style="{width:'500px'}">

          <FormItem label="终端背景图片" >
            <Upload
              :on-success="uploadSuccess"
              :on-error="uploadError"
              :format="['png']"
              :data="editForm"
              :on-format-error="handleFormatError"
              :name="background"
              :show-upload-list="false"
              action="/v2/display/">
              <Button icon="ios-cloud-upload-outline" >选择上传图片</Button>
            </Upload>

          </FormItem>
          <FormItem   label="温馨提示">
            <Alert type="warning" show-icon>图片仅支持png格式</Alert>
          </FormItem>

        </Form>
      </Card>
    </dvi>
</template>

<script>
    import {getRules} from '@/libs/ruleValidate'
    import {getbackground} from '@/api/systemSet'
    import {getType} from '@/api/common'
    export default {
      name: "system_set_page",
      data() {
        return {
          edit: true,
          isShow: false,
          model: {
            edit: {
              loading: true,
              open: false,
              title: ""
            }
          },
        }
      },
      methods: {
        handleFormatError (file) {
          this.$Message.warning('文件 ' + file.name + ' 格式不正确，请上传 png 格式的图片。');
        },
        uploadSuccess (res) {
            this.$Message.success('上传成功')
        },
        uploadError () {
          this.$Message.error('上传失败')
        },
      },

    }
</script>

<style lang="less">
  .ivu-form-item {
    margin-bottom: 20px;
  }
</style>

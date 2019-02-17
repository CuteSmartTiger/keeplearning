<template>
  <div>
    <Card>
      <Form ref="editForm" :model="editForm" :label-width="120" :rules="ruleValidate"  :style="{width:'500px'}">
        <FormItem label="许可证服务器" prop="hostname">
          <Input v-model="editForm.hostname">
            <Button slot="append" @click="onFinger()" type="primary">修改</Button>
          </Input>
        </FormItem>
        <FormItem label="许可证信息"  >
          <Alert type="error" v-show="info == 2">
            暂无信息
          </Alert>
          <Alert type="success" v-show="info == 1">
            <Row>
              <Col :span="8">机器码（指纹码）</Col>
              <Col :span="14">{{result.host_fingerprint}}</Col>
            </Row>
            <Row v-show = "result.issue_date && result.issue_date != ''">
              <Col :span="8">发布日期</Col>
              <Col>{{result.issue_date}}</Col>
            </Row>
            <Row  v-show = "result.issue_to && result.issue_to != ''">
              <Col :span="8">发布对象</Col>
              <Col :span="14">{{result.issue_to}}</Col>
            </Row>
            <Row  v-show = "result.num_modules && result.num_modules != ''">
              <Col :span="8">模型数量</Col>
              <Col :span="14">{{result.num_modules}}</Col>
            </Row>
            <Row  v-show = "result.module_license_volume && result.module_license_volume != ''">
              <Col :span="8">许可数量</Col>
              <Col :span="14">{{result.module_license_volume}}</Col>
            </Row>
            <Row  v-show = "result.module_name && result.module_name != ''">
              <Col :span="8">模型名称</Col>
              <Col :span="14">{{result.module_name}}</Col>
            </Row>
            <Row  v-show = "result.module_license_expire_day && result.module_license_expire_day != ''">
              <Col :span="8">有效时长</Col>
              <Col :span="14">{{result.module_license_expire_day}}天</Col>
            </Row>
          </Alert>
        </FormItem>
        <FormItem label="申请许可证" >
          <Upload
            :on-success="uploadSuccess"
            :on-error="uploadError"
            :format="['txt']"
            :max-size="5"
            :on-format-error="handleFormatError"
            :on-exceeded-size="handleMaxSize"
            name="licensefile"
            :show-upload-list="false"
            action="/v2/license/allowed/">
            <Button icon="ios-cloud-upload-outline" >选择上传文件</Button>
          </Upload>

        </FormItem>
        <FormItem label="温馨提示" >
          <Alert type="warning" show-icon>上传文件为txt格式，文件大小不超过5KB</Alert>
        </FormItem>
      </Form>
    </Card>

  </div>
</template>

<script>
  import {getRules} from '@/libs/ruleValidate'
  import {getLicensesData,postLicensesData,fileLicensesData} from '@/api/licences'
  export default {
    name: 'licences_manage_page',
    data() {
      return {
        editForm: {
          hostname:''
        },
        info: 0,
        result: {},
        ruleValidate: getRules(['hostname']),
      }
    },
    methods: {
      handleList() {
        getLicensesData().then(res => {
          this.editForm.hostname = res.hostname || '';
          this.result = res;
          this.info = 1;
        },err=> {
          this.result = {};
          this.info = 2;
        })
      },
      handleFormatError (file) {
        this.$Message.warning('文件 ' + file.name + ' 格式不正确，请上传 txt 格式的文件。');
      },
      handleMaxSize (file) {
        this.$Message.warning('文件 ' + file.name + ' 太大，不能超过 5KB。');
      },
      uploadSuccess (res) {
        if(typeof res == 'object'){
          this.result = res;
          this.info = 1;
          this.$Message.success('上传成功')
        }else{
          this.$Message.err(res)
        }
      },
      uploadError () {
        this.$Message.error('上传失败')
      },
      onFinger() {
        this.$refs['editForm'].validate((valid) => {
          if (valid) {
            postLicensesData(this.editForm).then(res => {
              this.result = res;
              this.info = 1;
              this.$Message.success('修改成功')
            },err=> {
              this.result = {};
              this.info = 2;
            })
          }
        })
      }
    },
    mounted() {
      this.handleList()
    }

  }
</script>
<style lang="less">
  .ivu-form-item {
    margin-bottom: 20px;
  }

</style>

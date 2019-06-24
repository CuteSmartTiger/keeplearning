<template>
  <v-card color="grey lighten-3" class="mb-5" v-if="item">
    <v-layout row wrap>
      <!-- 基本信息 -->
      <v-flex xs6>
        <v-subheader>申请人: {{item.creator}}</v-subheader>
      </v-flex>
      <v-flex xs6>
        <v-subheader>申请日期: {{item.create_time | utc2local }}</v-subheader>
      </v-flex>
      <v-flex xs6>
        <v-subheader>上线的系统: {{item.system}}</v-subheader>
      </v-flex>
      <v-flex xs6>
        <v-subheader>上线的版本: {{item.version}}</v-subheader>
      </v-flex>
      <v-flex xs6>
        <v-subheader>计划上线时间: {{item.plan_time | utc2local }}</v-subheader>
      </v-flex>
      <v-flex xs6 v-if="item.db_type">
        <v-subheader>数据库类型: {{item.db_type}}</v-subheader>
      </v-flex>
      <v-flex xs6 v-if="item.db_config">
        <v-subheader>数据库配置: {{item.db_config}}</v-subheader>
      </v-flex>
      <v-flex xs6>
        <v-subheader>审核: {{item.approver}}</v-subheader>
      </v-flex>
      <v-flex xs6>
        <v-subheader>测试: {{item.qa}}</v-subheader>
      </v-flex>
      <v-flex xs6>
        <v-subheader>运维: {{item.ops}}</v-subheader>
      </v-flex>
      <v-flex xs6>
        <v-subheader>开发: {{item.dev}}</v-subheader>
      </v-flex>
      <v-flex xs6>
        <v-subheader>DBA: {{item.dba}}</v-subheader>
      </v-flex>
      <v-flex xs6>
        <v-subheader>PM: {{item.pm}}</v-subheader>
      </v-flex>
      <v-flex xs6 v-if="item.cc">
        <v-subheader>邮件组抄送: {{item.cc}}</v-subheader>
      </v-flex>
      <v-flex xs12 v-if="item.db_sql">
        <v-text-field
          label="SQL"
          :value="item.db_sql"
          readonly
          textarea>
        </v-text-field>
      </v-flex>
      <v-flex xs12>
        <v-text-field
          label="上线内容"
          :value="item.content"
          readonly
          textarea>
        </v-text-field>
      </v-flex>
      <!-- 操作日志 -->
      <v-flex xs12>
        <v-divider></v-divider>
      </v-flex>
      <v-flex xs6 v-if="item.dev_time">
        <v-subheader>验收确认时间: {{item.dev_time | utc2local }}</v-subheader>
        <v-subheader>验收阶段操作确认人员: {{item.operate_dev }}</v-subheader>
      </v-flex>
      <v-flex xs6 v-if="item.pm_time">
        <v-subheader>验收确认时间: {{item.pm_time | utc2local }}</v-subheader>
        <v-subheader>验收阶段操作确认人员: {{item.operate_pm }}</v-subheader>
      </v-flex>
      <v-flex xs6 v-if="item.ops_time">
        <v-subheader>OPS确认时间: {{item.ops_time | utc2local }}</v-subheader>
        <v-subheader>执行阶段操作人员: OPS:{{item.operate_ops }}</v-subheader>
      </v-flex>
      <v-flex xs6 v-if="item.dba_time">
        <v-subheader>DBA确认时间: {{item.dba_time | utc2local }}</v-subheader>
        <v-subheader>执行阶段操作人员: DBA:{{item.operate_ops }}</v-subheader>
      </v-flex>
      <v-flex xs6 v-if="item.qa_time">
        <v-subheader>测试确认时间: {{item.qa_time | utc2local }}</v-subheader>
        <v-subheader>测试阶段操作人员: {{item.operate_qa }}</v-subheader>
      </v-flex>
      <v-flex xs6 v-if="item.approver_time">
        <v-subheader>审核确认时间: {{item.approver_time | utc2local }}</v-subheader>
        <v-subheader>审核阶段操作人员: {{item.operate_approver }}</v-subheader>
      </v-flex>
      <v-flex xs6>
        <v-subheader>最后操作时间: {{item.update_time | utc2local }}</v-subheader>
        <v-subheader>最后操作人: {{item.updator }}</v-subheader>
      </v-flex>
      <v-flex xs12>
        <v-divider></v-divider>
      </v-flex>
      <!-- 上传文件 -->
      <v-flex xs12>
        <v-chip label color="blue" text-color="white" @click.stop="dialog = true" v-if="item.status <5">
          <v-icon left>add</v-icon>
          上传文件
        </v-chip>
        <v-chip v-for="file in upload_files">
          <a style="text-decoration:none;" :href="file.access_url">{{ file.file_name }}</a>
        </v-chip>
      </v-flex>
      <!-- 评论内容 -->
      <v-flex xs12 v-if="comments">
        <v-text-field
          label="评论内容"
          :value="comments"
          readonly
          autofocus
          textarea>
        </v-text-field>
      </v-flex>
      <v-dialog v-model="dialog" max-width="400px">
        <v-card>
          <v-card-title>
            上传文件
          </v-card-title>
          <v-card-text>
            <v-chip label color="blue" text-color="white" @click.stop="show">
              <v-icon left>folder</v-icon>
              选择文件
            </v-chip>
            <input id="deploy_files_temp" type="file" name="file"/>
          </v-card-text>
          <v-card-actions>
            <v-btn @click.stop="upload">上传</v-btn>
            <v-btn color="blue" flat @click.stop="dialog = false">关闭</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-layout>
  </v-card>
</template>

<script>
  import {uploadDeploy} from '@/api';

  export default {
    name: 'DeployDetailInfo',
    props: ["item", "comments", "upload_files"],
    data: () => ({
      dialog: false,
    }),
    mounted: () => ({}),
    methods: {
      show() {
        document.getElementById('deploy_files_temp').click();
      },
      async upload() {
        let formData = new FormData();
        let files = document.getElementById('deploy_files_temp').files;
        formData.append('file', files[0]);
        formData.append('deploy_id', this.item.ID);
        const res = await uploadDeploy(formData);
        if (res.data.status === 0) {
          const data = res.data.data;
          const access_url = data.access_url;
          const file_name = data.file_name;
          this.upload_files.push({access_url: access_url, file_name: file_name});
          this.$store.dispatch('showSnackBar', {text: '上传成功', level: 'success'});
        }
      },
    }
  }
</script>

<style scoped>
  #deploy_files_temp {
    pointer-events: none;
    margin-left: -79px;
  }
</style>

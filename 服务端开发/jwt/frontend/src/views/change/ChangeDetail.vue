<template>
  <div>
    <Breadcrumbs :breadcrumbs_items="breadcrumbs_items"></Breadcrumbs>
    <v-layout row wrap>
      <v-flex xs12>
        <v-card>
          <v-stepper v-model="step">
            <v-stepper-header>
              <v-stepper-step step="1" :complete="step > 1" :rules="[() => step != 1 || same]">
                <template v-if="step <= 1">
                  待测试
                </template>
                <template v-else>
                  测试通过( {{ item.operate_qa }} )
                </template>
              </v-stepper-step>
              <v-divider></v-divider>
              <v-stepper-step step="2" :complete="step > 2" :rules="[() => step != 2 || same]">
                <template v-if="step <= 2">
                  待审批
                </template>
                <template v-else>
                  审批通过( {{ item.operate_approver }} )
                </template>
              </v-stepper-step>
              <v-divider></v-divider>
              <v-stepper-step step="3" :complete="step > 3" :rules="[() => step != 3 || same]">
                <template v-if="step <= 3">
                  待执行
                  <template v-if="item.operate_ops && !item.operate_dba">
                    [OPS已执行,待DBA执行]
                  </template>
                  <template v-if="item.operate_dba && !item.operate_ops">
                    [DBA已执行,待OPS执行]
                  </template>
                </template>
                <template v-else>
                  执行结束(
                  <template v-if="item.operate_ops">
                    OPS:{{ item.operate_ops }},
                  </template>
                  <template v-if="item.operate_dba">
                    DBA:{{ item.operate_dba }}
                  </template>
                  )
                </template>
              </v-stepper-step>
              <v-divider></v-divider>
              <v-stepper-step step="4" :complete="step > 4" :rules="[() => step != 4 || same]">
                <template v-if="step <= 4">
                  待验收
                </template>
                <template v-else>
                  验收结束( {{ item.operate_dev ? item.operate_dev : item.operate_pm }} )
                </template>
              </v-stepper-step>
              <v-divider></v-divider>
              <v-stepper-step step="5" :complete="step > 5" :rules="[() => step != 5 || same]">
                完成
              </v-stepper-step>
            </v-stepper-header>
            <div style="padding: 28px">
              <Info :item="item" :comments="comments" :upload_files="upload_files"></Info>
              <v-form v-model="valid" ref="change_comment_form" lazy-validation v-if="item.status <5">
                <v-layout row wrap>
                  <v-flex xs10>
                    <v-text-field
                      label="评论"
                      v-model="comment"
                      :rules="commentRules"
                      required
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs2 class="text-xs-right">
                    <v-btn color="primary" @click.native="addChangeComment">发送</v-btn>
                    <v-btn @click="clear">清空</v-btn>
                  </v-flex>
                </v-layout>
              </v-form>
            </div>
            <v-stepper-items>
              <template v-for="i in [1,2,3,4,5]">
                <v-stepper-content :step="i">
                  <template v-if="item.status <5">
                    <v-btn color="primary" @click.native="operateChange('approve')">通过</v-btn>
                    <v-btn flat @click.native="operateChange('reject')">拒绝</v-btn>
                    <v-btn flat @click.native="operateChange('cancel')">取消</v-btn>
                  </template>
                </v-stepper-content>
              </template>
            </v-stepper-items>
          </v-stepper>
        </v-card>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
  import {utc2local} from '@/filter';
  import Breadcrumbs from '@/components/Breadcrumbs';
  import Info from '@/views/change/ChangeDetailInfo';
  import {listChange, operateChange, addChangeComment} from '@/api';


  export default {
    name: 'ChangeDetail',
    components: {
      Breadcrumbs: Breadcrumbs,
      Info: Info,
    },
    data: () => ({
      breadcrumbs_items: [
        {text: "变更流程"},
        {text: "流程详细"},
      ],
      valid: true,
      item: {},
      step: 1,
      same: true,
      comment: '',
      comments: '',
      upload_files: [],
      commentRules: [
        v => !!v || '评论不能为空'
      ],
    }),
    mounted: function () {
      this.listChange();
    },
    methods: {
      async listChange() {
        const changeID = this.$route.params.ID;
        const res = await listChange({
          params: {
            ID: changeID,
          }
        });
        const data = res.data.data;
        const change = data.change;
        const change_comments = data.change_comments;
        this.item = change;
        this.comments = '';
        this.upload_files = [];
        change_comments.sort((a, b) => {
          return b.ID - a.ID;
        });
        change_comments.forEach(value => {
          this.comments += `${utc2local(value.create_time)}   ${value.creator}:   ${value.content}\n`;
        });
        this.upload_files = data.change_files;
        this.step = this.item.bak_status;
        this.same = this.item.bak_status === this.item.status;
      },
      async operateChange(action) {
        const changeID = this.$route.params.ID;
        const res = await operateChange({
          ID: changeID,
          action: action,
        });
        if (res.data.status === 0) {
          this.listChange();
          this.$root.eventHub.$emit('get_todos');
        }
      },
      async addChangeComment() {
        if (this.$refs.change_comment_form.validate()) {
          const changeID = this.$route.params.ID;
          const res = await addChangeComment({
            ID: changeID,
            comment: this.comment,
          });
          if (res.data.status === 0) {
            this.clear();
            this.listChange();
          }
        }
      },
      clear() {
        this.$refs.change_comment_form.reset();
      }
    }
  }
</script>

<style scoped>
</style>

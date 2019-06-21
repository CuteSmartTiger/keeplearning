<template>
  <div>
    <Breadcrumbs :breadcrumbs_items="breadcrumbs_items"></Breadcrumbs>
    <v-layout row wrap>
      <v-flex xs12>
        <v-card style="padding: 24px">
          <v-form v-model="valid" ref="change_form" lazy-validation>
            <v-layout row wrap>
              <v-flex xs6>
                <v-select
                  :items="systems"
                  v-model="system"
                  label="变更的系统"
                  :rules="systemRules"
                  prepend-icon="apps"
                  autocomplete
                  required
                ></v-select>
              </v-flex>
              <v-flex xs6>
                <v-select
                  :items="change_types"
                  v-model="change_type"
                  label="变更类型"
                  :rules="changeTypeRules"
                  prepend-icon="merge_type"
                  required
                ></v-select>
              </v-flex>
              <v-flex xs6>
                <v-text-field
                  v-model="version"
                  label="版本"
                  :rules="versionRules"
                  prepend-icon="train"
                  required
                ></v-text-field>
              </v-flex>
              <v-flex xs6>
                <v-text-field
                  v-model="cc"
                  label="邮件组抄送"
                  prepend-icon="email"
                  single-line
                ></v-text-field>
              </v-flex>
              <v-flex xs6>
                <v-select
                  :items="approvers"
                  v-model="approver"
                  label="审核"
                  :rules="approverRules"
                  prepend-icon="person"
                  autocomplete
                  required
                ></v-select>
              </v-flex>
              <v-flex xs6>
                <v-select
                  :items="qas"
                  v-model="qa"
                  label="测试"
                  :rules="qaRules"
                  prepend-icon="person"
                  multiple
                  autocomplete
                  required
                ></v-select>
              </v-flex>
              <v-flex xs6>
                <v-select
                  :items="opss"
                  v-model="ops"
                  label="运维"
                  :rules="opsRules"
                  prepend-icon="person"
                  multiple
                  autocomplete
                  required
                ></v-select>
              </v-flex>
              <v-flex xs6>
                <v-select
                  :items="devs"
                  v-model="dev"
                  label="开发"
                  :rules="devRules"
                  prepend-icon="person"
                  multiple
                  autocomplete
                  required
                ></v-select>
              </v-flex>
              <v-flex xs6>
                <v-select
                  :items="dbas"
                  v-model="dba"
                  label="DBA"
                  :rules="dbaRules"
                  prepend-icon="person"
                  multiple
                  autocomplete
                  required
                ></v-select>
              </v-flex>
              <v-flex xs6>
                <v-select
                  :items="pms"
                  v-model="pm"
                  label="产品经理"
                  :rules="pmRules"
                  prepend-icon="person"
                  multiple
                  autocomplete
                  required
                ></v-select>
              </v-flex>
              <v-flex xs6>
                <v-menu
                  ref="plan_menu"
                  lazy
                  :close-on-content-click="false"
                  v-model="plan_menu"
                  transition="scale-transition"
                  offset-y
                  full-width
                  :nudge-right="40"
                  min-width="290px"
                  :return-value.sync="plan_date">
                  <v-text-field
                    slot="activator"
                    label="预计变更日期"
                    v-model="plan_date"
                    :rules="dateRules"
                    prepend-icon="event"
                    readonly>
                  </v-text-field>
                  <v-date-picker v-model="plan_date" no-title scrollable>
                    <v-spacer></v-spacer>
                    <v-btn flat color="primary" @click="plan_menu = false">Cancel</v-btn>
                    <v-btn flat color="primary" @click="$refs.plan_menu.save(plan_date)">OK</v-btn>
                  </v-date-picker>
                </v-menu>
              </v-flex>
              <v-flex xs6>
                <v-menu
                  ref="plan_time_menu"
                  lazy
                  :close-on-content-click="false"
                  v-model="plan_time_menu"
                  transition="scale-transition"
                  offset-y
                  full-width
                  :nudge-right="40"
                  max-width="290px"
                  min-width="290px"
                  :return-value.sync="plan_time">
                  <v-text-field
                    slot="activator"
                    label="计划变更时间"
                    v-model="plan_time"
                    :rules="timeRules"
                    prepend-icon="access_time"
                    readonly>
                  </v-text-field>
                  <v-time-picker v-model="plan_time" @change="$refs.plan_time_menu.save(plan_time)"></v-time-picker>
                </v-menu>
              </v-flex>
              <v-flex xs12>
                <v-text-field
                  v-model="problem_desc"
                  label="线上问题描述"
                  :rules="contentRules"
                  required
                  textarea>
                </v-text-field>
              </v-flex>
              <v-flex xs12>
                <v-text-field
                  v-model="content_desc"
                  label="变更内容描述"
                  :rules="contentRules"
                  required
                  textarea>
                </v-text-field>
              </v-flex>
              <v-flex xs12>
                <v-text-field
                  v-model="risk_desc"
                  label="变更执行风险描述"
                  :rules="contentRules"
                  required
                  textarea>
                </v-text-field>
              </v-flex>
              <v-flex xs12>
                <v-checkbox
                  label="是否有对应SQL"
                  v-model="have_sql"
                ></v-checkbox>
              </v-flex>
              <v-flex xs6 v-if="have_sql">
                <v-text-field
                  v-model="db_type"
                  label="数据库类型(MYSQL)"
                  prepend-icon="storage"
                  single-line
                ></v-text-field>
              </v-flex>
              <v-flex xs6 v-if="have_sql">
                <v-text-field
                  v-model="db_config"
                  label="数据库配置(IP、Port)"
                  prepend-icon="settings"
                  single-line
                ></v-text-field>
              </v-flex>
              <v-flex xs12 v-if="have_sql">
                <v-text-field
                  v-model="db_sql"
                  label="数据库(SQL)"
                  textarea
                ></v-text-field>
              </v-flex>
              <v-flex xs12>
                <v-divider></v-divider>
              </v-flex>
              <v-flex xs12>
                <v-chip label color="blue" text-color="white" @click.stop="dialog = true">
                  <v-icon left>add</v-icon>
                  上传文件
                </v-chip>
                <v-chip v-for="file in upload_files">
                  <a style="text-decoration:none;" :href="file.access_url">{{ file.file_name }}</a>
                  <v-avatar @click="deleteFile(file)">
                    <v-icon right>close</v-icon>
                  </v-avatar>
                </v-chip>
              </v-flex>
              <v-flex xs12>
                <v-divider></v-divider>
              </v-flex>
              <v-flex xs12>
                <v-btn @click="submit" :disabled="!valid">提交</v-btn>
                <v-btn @click="clear">重置</v-btn>
              </v-flex>
            </v-layout>
          </v-form>
        </v-card>
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
            <input id="change_files" type="file" name="file"/>
          </v-card-text>
          <v-card-actions>
            <v-btn @click.stop="upload">上传</v-btn>
            <v-btn color="blue" flat @click.stop="dialog = false">关闭</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-layout>
  </div>
</template>

<script>
  import Breadcrumbs from '@/components/Breadcrumbs';
  import {listSystem, listUser, createChange, uploadChange, deleteFileChange} from '@/api';

  export default {
    name: 'ChangeCreate',
    components: {
      Breadcrumbs: Breadcrumbs
    },
    data: () => ({
      breadcrumbs_items: [
        {text: "变更流程"},
        {text: "新建流程"},
      ],
      valid: true,
      dialog: false,
      system: '',
      systems: [],
      system_users: {},
      change_type: '',
      change_types: [{text: 'DB变更'}, {text: 'Hotfix'}],
      version: '',
      db_type: '',
      db_config: '',
      db_sql: '',
      dev: [],
      devs: [],
      qa: [],
      qas: [],
      ops: [],
      opss: [],
      approver: '',
      approvers: [],
      dba: [],
      dbas: [],
      pm: [],
      pms: [],
      cc: '',
      plan_date: null,
      plan_menu: false,
      plan_time: null,
      plan_time_menu: false,
      problem_desc: '',
      content_desc: '',
      risk_desc: '',
      upload_files: [],
      have_sql: false,
      systemRules: [
        v => !!v || '请选择变更系统'
      ],
      changeTypeRules: [
        v => !!v || '请选择变更类型'
      ],
      devRules: [
        v => (v && v.length > 0) || '请选择开发'
      ],
      qaRules: [
        v => (v && v.length > 0) || '请选择测试'
      ],
      opsRules: [
        v => (v && v.length > 0) || '请选择运维'
      ],
      dbaRules: [
        v => (v && v.length > 0) || '请选择DBA'
      ],
      pmRules: [
        v => (v && v.length > 0) || '请选择产品经理'
      ],
      approverRules: [
        v => !!v || '请选择审核'
      ],
      dateRules: [
        v => !!v || '请选择预计变更日期'
      ],
      timeRules: [
        v => !!v || '请选择预计变更时间'
      ],
      contentRules: [
        v => !!v || '内容不能为空'
      ],
      versionRules: [
        v => !!v || '请填写版本号'
      ],
    }),
    watch: {
      system: function (val) {
        if (val !== undefined && val !== null) {
          let system = val.text;
          this.dev = [];
          this.qa = [];
          this.ops = [];
          this.dba = [];
          this.pm = [];
          this.approver = {};
          let user_roles = this.system_users[system] !== undefined ? this.system_users[system] : [];
          user_roles.forEach(value => {
            let role = value[0];
            let username = value[1];
            let name = value[2];
            let temp = {};
            let single_temp = '';
            if (name !== undefined) {
              single_temp = `${username} (${name})`;
              temp = {'text': `${username} (${name})`};
            } else {
              single_temp = value.name;
              temp = {'text': value.name};
            }
            switch (role) {
              case 'DEV':
                this.dev.push(temp);
                break;
              case 'OPS':
                this.ops.push(temp);
                break;
              case 'QA':
                this.qa.push(temp);
                break;
              case 'DBA':
                this.dba.push(temp);
                break;
              case 'PM':
                this.pm.push(temp);
                break;
              case 'APPROVER':
                this.approver = single_temp;
                break;
            }
          });
        }
      },
    },
    mounted: function () {
      this.init();
    },
    methods: {
      init() {
        this.listSystem();
        this.listUser();
      },
      changeList(data, no_name = true) {
        let temp_data = [];
        data.forEach(value => {
          if (no_name) {
            temp_data.push({'text': `${value.username} (${value.name})`});
          } else {
            temp_data.push({'text': value.name});
          }
        });
        return temp_data;
      },
      changeList2(data) {
        let temp_data = [];
        data.forEach(value => {
          temp_data.push(`${value.username} (${value.name})`);
        });
        return temp_data;
      },
      translateList(data) {
        let temp_data = [];
        data.forEach(value => {
          let temp = value.text;
          if (typeof temp === 'string') {
            temp = temp.replace('(', '').replace(')', '').split(' ')[0];
            temp_data.push(temp);
          }
        });
        return temp_data.join(',');
      },
      async listSystem() {
        const res = await listSystem({});
        const data = res.data.data;
        const systems = data.systems;
        const system_users = data.system_users;
        this.systems = this.changeList(systems, false);
        this.system_users = system_users;
      },
      async listUser() {
        let roles = ['DEV', 'QA', 'OPS', 'APPROVER', 'DBA', 'PM'];
        const res = await listUser({
          params: {
            roles: roles.join(',')
          }
        });
        const data = res.data.data;
        this.devs = this.changeList(data.DEV ? data.DEV : []);
        this.qas = this.changeList(data.QA ? data.QA : []);
        this.opss = this.changeList(data.OPS ? data.OPS : []);
        this.dbas = this.changeList(data.DBA ? data.DBA : []);
        this.pms = this.changeList(data.PM ? data.PM : []);
        this.approvers = this.changeList2(data.APPROVER ? data.APPROVER : []);

      },
      async createChange() {
        const res = await createChange({
          system: this.system.text,
          change_type: this.change_type.text,
          dev: this.translateList(this.dev),
          qa: this.translateList(this.qa),
          ops: this.translateList(this.ops),
          dba: this.translateList(this.dba),
          pm: this.translateList(this.pm),
          approver: this.translateList([{'text': this.approver}]),
          plan_date: this.plan_date,
          plan_time: this.plan_time,
          problem_desc: this.problem_desc,
          content_desc: this.content_desc,
          risk_desc: this.risk_desc,
          version: this.version,
          db_type: this.db_type,
          db_config: this.db_config,
          db_sql: this.db_sql,
          cc: this.cc,
          upload_files: this.upload_files,
          have_sql: this.have_sql,
        });
        if (res.data.status === 0) {
          this.$router.push('/change/todo');
          this.$root.eventHub.$emit('get_todos');
        }
      },
      submit() {
        if (this.$refs.change_form.validate()) {
          this.createChange();
        }
      },
      clear() {
        this.$refs.change_form.reset()
      },
      show() {
        document.getElementById('change_files').click();
      },
      async upload() {
        let formData = new FormData();
        let files = document.getElementById('change_files').files;
        formData.append('file', files[0]);
        const res = await uploadChange(formData);
        if (res.data.status === 0) {
          const data = res.data.data;
          const access_url = data.access_url;
          const file_name = data.file_name;
          this.upload_files.push({access_url: access_url, file_name: file_name});
          this.$store.dispatch('showSnackBar', {text: '上传成功', level: 'success'});
        }
      },
      async deleteFile(changeFile) {
        const res = await deleteFileChange({
          ID: changeFile.ID,
          file_name: changeFile.file_name,
        });
        if (res.data.status === 0) {
          if (this.upload_files !== null) {
            let index = this.upload_files.indexOf(changeFile);
            this.upload_files.splice(index, 1);
            this.$store.dispatch('showSnackBar', {text: '删除成功', level: 'success'});
          }
        }
      },
    }
  }
</script>

<style scoped>
  #change_files {
    pointer-events: none;
    margin-left: -79px;
  }
</style>

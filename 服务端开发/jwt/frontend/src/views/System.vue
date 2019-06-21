<template>
  <div>
    <Breadcrumbs :breadcrumbs_items="breadcrumbs_items"></Breadcrumbs>
    <v-layout row wrap>
      <v-flex xs12>
        <v-text-field
          append-icon="search"
          label="Search"
          single-line
          hide-details
          v-model="search"
          class="todo_search"
        ></v-text-field>
        <v-chip label color="blue" text-color="white" class="todo_add_system" @click.stop="dialog = true">
          <v-icon left>add</v-icon>
          添加系统
        </v-chip>
      </v-flex>
      <v-flex xs12>
        <v-card>
          <v-data-table
            :headers="headers"
            :items="items"
            :loading="loading"
            :search="search"
            class="elevation-1"
          >
            <v-progress-linear slot="progress" color="blue" indeterminate></v-progress-linear>
            <template slot="items" slot-scope="props" class="text-xs-left">
              <td>{{ props.item.ID }}</td>
              <td>{{ props.item.name }}</td>
              <td>{{ props.item.alias }}</td>
              <td>{{ props.item.desc }}</td>
              <td>
                <v-chip label color="blue" text-color="white" @click.stop="show(props.item)">
                  查看详细
                </v-chip>
              </td>
            </template>
            <template slot="pageText" slot-scope="props">
              Lignes {{ props.pageStart }} - {{ props.pageStop }} de {{ props.itemsLength }}
            </template>
          </v-data-table>
        </v-card>
      </v-flex>
      <v-dialog v-model="dialog" max-width="500px">
        <v-form v-model="valid" ref="system_form" lazy-validation>
          <v-card>
            <v-card-title>
              添加系统
            </v-card-title>
            <v-card-text>
              <v-text-field
                label="Name"
                v-model="system_name"
                :rules="systemNameRules"
                required
              ></v-text-field>
              <v-text-field
                label="Alias"
                v-model="system_alias"
              ></v-text-field>
              <v-text-field
                label="Desc"
                v-model="system_desc"
              ></v-text-field>
            </v-card-text>
            <v-card-actions>
              <v-btn @click="submit" :disabled="!valid">添加</v-btn>
              <v-btn @click="clear">重置</v-btn>
              <v-btn color="blue" flat @click.stop="dialog = false">关闭</v-btn>
            </v-card-actions>
          </v-card>
        </v-form>
      </v-dialog>
      <v-dialog v-model="dialog_detail" max-width="700px">
        <v-form v-model="valid_detail" ref="system_user_form" lazy-validation>
          <v-card>
            <v-card-title>
              系统对应干系人
            </v-card-title>
            <v-card-text>
              <v-layout row wrap>
                <v-flex xs12>
                  <v-select
                    :items="approvers"
                    v-model="approver"
                    label="审核"
                    prepend-icon="person"
                    autocomplete
                  ></v-select>
                </v-flex>
                <v-flex xs12>
                  <v-select
                    :items="qas"
                    v-model="qa"
                    label="测试"
                    prepend-icon="person"
                    multiple
                    autocomplete
                  ></v-select>
                </v-flex>
                <v-flex xs12>
                  <v-select
                    :items="opss"
                    v-model="ops"
                    label="运维"
                    prepend-icon="person"
                    multiple
                    autocomplete
                  ></v-select>
                </v-flex>
                <v-flex xs12>
                  <v-select
                    :items="devs"
                    v-model="dev"
                    label="开发"
                    prepend-icon="person"
                    multiple
                    autocomplete
                  ></v-select>
                </v-flex>
                <v-flex xs12>
                  <v-select
                    :items="dbas"
                    v-model="dba"
                    label="DBA"
                    prepend-icon="person"
                    multiple
                    autocomplete
                  ></v-select>
                </v-flex>
                <v-flex xs12>
                  <v-select
                    :items="pms"
                    v-model="pm"
                    label="产品经理"
                    prepend-icon="person"
                    multiple
                    autocomplete
                  ></v-select>
                </v-flex>
              </v-layout>
            </v-card-text>
            <v-card-actions>
              <v-btn @click="updateSystem">更新</v-btn>
              <v-btn @click="clearSystem">重置</v-btn>
              <v-btn color="blue" flat @click.stop="dialog_detail = false">关闭</v-btn>
            </v-card-actions>
          </v-card>
        </v-form>
      </v-dialog>
    </v-layout>
  </div>
</template>

<script>
  import Breadcrumbs from '@/components/Breadcrumbs';
  import {listUser, listSystem, addSystem, updateSystem} from '@/api';

  export default {
    name: 'System',
    components: {
      Breadcrumbs: Breadcrumbs
    },
    data: () => ({
      breadcrumbs_items: [
        {text: "系统管理"},
      ],
      valid: true,
      valid_detail: true,
      dialog: false,
      dialog_detail: false,
      headers: [
        {
          text: '编号',
          align: 'left',
          sortable: false,
          value: 'ID'
        },
        {text: '名称', value: 'name'},
        {text: '别名', value: 'alias'},
        {text: '描述', value: 'desc'},
        {text: '操作', value: 'operate'},
      ],
      items: [],
      system_id: '',
      system_name: '',
      system_alias: '',
      system_desc: '',
      system_users: {},
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
      systemNameRules: [
        v => !!v || '请选择上线系统'
      ],
      loading: true,
      search: '',
    }),
    methods: {
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
      async listSystem() {
        this.loading = true;
        const res = await listSystem({});
        const data = res.data.data;
        const systems = data.systems;
        const system_users = data.system_users;
        this.items = systems;
        this.system_users = system_users;
        this.loading = false;
      },
      async addSystem() {
        const res = await addSystem({
          system_name: this.system_name,
          system_alias: this.system_alias,
          system_desc: this.system_desc,
        });
        if (res.data.status === 0) {
          this.dialog = false;
          this.clear();
          this.listSystem();
          this.$store.dispatch('showSnackBar', {text: '添加成功', level: 'success'});
        }
      },
      async updateSystem() {
        const res = await updateSystem({
          system_id: this.system_id,
          dev: this.translateList(this.dev),
          qa: this.translateList(this.qa),
          ops: this.translateList(this.ops),
          dba: this.translateList(this.dba),
          pm: this.translateList(this.pm),
          approver: this.translateList([{'text': this.approver}]),
        });
        if (res.data.status === 0) {
          this.listSystem();
          this.$store.dispatch('showSnackBar', {text: '更新成功', level: 'success'});
        }
      },
      async clearSystem() {
        this.$refs.system_user_form.reset();
      },
      submit() {
        if (this.$refs.system_form.validate()) {
          this.addSystem();
        }
      },
      clear() {
        this.$refs.system_form.reset();
      },
      show(system) {
        this.dialog_detail = true;
        this.system_id = system.ID;
        this.dev = [];
        this.qa = [];
        this.ops = [];
        this.dba = [];
        this.pm = [];
        this.approver = {};
        let user_roles = this.system_users[system.name] !== undefined ? this.system_users[system.name] : [];
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
      },
    },
    async mounted() {
      this.listSystem();
      this.listUser();
    },
  }
</script>

<style scoped>
  .todo_search {
    width: 256px;
    float: left;
    margin-left: 10px;
    padding-bottom: 10px;
  }

  .todo_add_system {
    float: left;
    margin-left: 22px;
    margin-top: 15px;
  }
</style>

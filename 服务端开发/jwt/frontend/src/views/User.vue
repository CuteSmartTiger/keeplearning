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
              <td>{{ props.item.username }}</td>
              <td>{{ props.item.name }}</td>
              <td>{{ props.item.phone }}</td>
              <td>{{ props.item.email }}</td>
              <td>
                <template v-for="role in user_roles[props.item.username]">
                  <v-chip small label :color="colorDict[role]" text-color="white">{{ role }}</v-chip>
                </template>
              </td>
              <td>{{ props.item.date_joined | utc2local }}</td>
              <td>{{ props.item.last_login | utc2local }}</td>
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
      <v-dialog v-model="dialog" max-width="550px">
        <v-form v-model="valid" ref="user_form" lazy-validation>
          <v-card>
            <v-card-title style="margin-bottom: -20px">
              <v-subheader style="margin-left: -15px">用户详细信息</v-subheader>
            </v-card-title>
            <v-card-text>
              <v-text-field
                label="账号"
                v-model="username"
                readonly
              ></v-text-field>
              <v-text-field
                label="姓名"
                v-model="name"
              ></v-text-field>
              <v-text-field
                label="联系电话"
                v-model="phone"
              ></v-text-field>
              <v-text-field
                label="电子邮箱"
                v-model="email"
              ></v-text-field>
              <v-subheader style="margin-left: -15px">
                用户角色
                <v-btn small flat icon color="grey" @click.stop="showRoleSetting">
                  <v-icon>settings</v-icon>
                </v-btn>
              </v-subheader>
              <template v-for="role in role_list">
                <v-chip style="margin-left: 0; margin-right: 10px" small label :color="colorDict[role]"
                        text-color="white">{{ role }}
                </v-chip>
              </template>
            </v-card-text>
            <v-card-actions>
              <v-btn @click="submit" :disabled="!valid">更新</v-btn>
              <v-btn color="blue" flat @click.stop="dialog = false">关闭</v-btn>
            </v-card-actions>
          </v-card>
        </v-form>
      </v-dialog>
      <v-dialog v-model="dialog2" max-width="500px">
        <v-card>
          <v-card-title>
            修改用户角色
          </v-card-title>
          <v-card-text>
            <v-chip close small label :color="colorDict['ADMIN']" text-color="white" v-model="role_admin">ADMIN</v-chip>
            <v-chip close small label :color="colorDict['DEV']" text-color="white" v-model="role_dev">DEV</v-chip>
            <v-chip close small label :color="colorDict['OPS']" text-color="white" v-model="role_ops">OPS</v-chip>
            <v-chip close small label :color="colorDict['QA']" text-color="white" v-model="role_qa">QA</v-chip>
            <v-chip close small label :color="colorDict['DBA']" text-color="white" v-model="role_dba">DBA</v-chip>
            <v-chip close small label :color="colorDict['PM']" text-color="white" v-model="role_pm">PM</v-chip>
            <v-chip close small label :color="colorDict['APPROVER']" text-color="white" v-model="role_approver">APPROVER
            </v-chip>
          </v-card-text>
          <v-card-actions>
            <v-btn @click="submitRoleSetting">更新</v-btn>
            <v-btn color="blue" flat @click.stop="dialog2 = false">关闭</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-layout>
  </div>
</template>

<script>
  import Breadcrumbs from '@/components/Breadcrumbs';
  import {listUser, updateUser} from '@/api';

  export default {
    name: 'User',
    components: {
      Breadcrumbs: Breadcrumbs
    },
    data: () => ({
      breadcrumbs_items: [
        {text: "用户管理"},
      ],
      valid: true,
      dialog: false,
      dialog2: false,
      headers: [
        {
          text: '编号',
          align: 'left',
          sortable: false,
          value: 'ID'
        },
        {text: '账号', value: 'username'},
        {text: '姓名', value: 'name'},
        {text: '联系电话', value: 'phone'},
        {text: '电子邮箱', value: 'email'},
        {text: '角色', value: 'roles'},
        {text: '加入时间', value: 'date_joined'},
        {text: '上次登陆时间', value: 'last_login'},
        {text: '操作', value: 'operate'},
      ],
      items: [],
      user_roles: {},
      username: '',
      name: '',
      phone: '',
      email: '',
      role_list: [],
      role_dev: true,
      role_ops: true,
      role_qa: true,
      role_approver: true,
      role_admin: true,
      role_dba: true,
      role_pm: true,
      colorDict: {
        DEV: 'green',
        OPS: 'light-green',
        QA: 'lime',
        APPROVER: 'orange lighten-1',
        ADMIN: 'red',
        DBA: 'teal lighten-3',
        PM: 'amber',
      },
      loading: true,
      search: '',
    }),
    methods: {
      async listUser() {
        this.loading = true;
        const res = await listUser({});
        const data = res.data.data;
        const users = data.users;
        const user_roles = data.user_roles;
        this.items = users;
        this.user_roles = user_roles;
        this.loading = false;
      },
      async updateUser() {
        const res = await updateUser({
          username: this.username,
          name: this.name,
          phone: this.phone,
          email: this.email,
          role_list: this.role_list,
        });
        if (res.data.status === 0) {
          this.listUser();
          this.$store.dispatch('showSnackBar', {text: '更新成功', level: 'success'});
        }
      },
      show(user) {
        this.username = user.username;
        this.name = user.name;
        this.phone = user.phone;
        this.email = user.email;
        this.role_list = this.user_roles[user.username];
        this.dialog = true;
      },
      submit() {
        if (this.$refs.user_form.validate()) {
          this.updateUser();
        }
      },
      showRoleSetting() {
        this.dialog2 = true;
        this.role_dev = true;
        this.role_ops = true;
        this.role_qa = true;
        this.role_approver = true;
        this.role_admin = true;
        this.role_dba = true;
        this.role_pm = true;
      },
      submitRoleSetting() {
        this.role_list = [];
        if (this.role_dev) {
          this.role_list.push('DEV');
        }
        if (this.role_ops) {
          this.role_list.push('OPS');
        }
        if (this.role_qa) {
          this.role_list.push('QA');
        }
        if (this.role_approver) {
          this.role_list.push('APPROVER');
        }
        if (this.role_admin) {
          this.role_list.push('ADMIN');
        }
        if (this.role_dba) {
          this.role_list.push('DBA');
        }
        if (this.role_pm) {
          this.role_list.push('PM');
        }
        this.dialog2 = false;
      },
    },
    async mounted() {
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
</style>

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
        <v-checkbox label="只看等待我操作的请求" v-model="relation" class="todo_checkbox"></v-checkbox>
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
              <td>
                <WorkflowType :workflow_type="props.item.workflow_type"></WorkflowType>
              </td>
              <td>{{ props.item.creator }}</td>
              <td>{{ props.item.create_time | utc2local }}</td>
              <td>{{ props.item.plan_time | utc2local }}</td>
              <td>{{ props.item.system }}</td>
              <td>{{ props.item.update_time | utc2local }}</td>
              <td>
                <Status :status="props.item.status"></Status>
              </td>
              <td>
                <v-btn small color="blue" dark @click="detail(props.item.ID, props.item.workflow_type)">查看详细</v-btn>
              </td>
            </template>
            <template slot="pageText" slot-scope="props">
              Lignes {{ props.pageStart }} - {{ props.pageStop }} de {{ props.itemsLength }}
            </template>
          </v-data-table>
        </v-card>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
  import Breadcrumbs from '@/components/Breadcrumbs';
  import Status from '@/components/Status';
  import WorkflowType from '@/components/WorkflowType';
  import {listDeploy, deployTodos, listChange, changeTodos} from '@/api';


  export default {
    name: 'Dashboard',
    components: {
      Breadcrumbs: Breadcrumbs,
      WorkflowType: WorkflowType,
      Status: Status,
    },
    data: () => ({
      breadcrumbs_items: [
        {text: "总览"},
      ],
      headers: [
        {
          text: '编号',
          align: 'left',
          sortable: false,
          value: 'ID'
        },
        {text: '流程类型', value: 'workflow_type'},
        {text: '申请人', value: 'creator'},
        {text: '申请日期', value: 'create_time'},
        {text: '预计时间', value: 'plan_time'},
        {text: '系统', value: 'system'},
        {text: '更新时间', value: 'update_time'},
        {text: '状态', value: 'status'},
        {text: '操作', value: 'action'},
      ],
      items: [],
      todo_number: 0,
      relation: false,
      loading: true,
      search: '',
    }),
    watch: {
      relation: function (val) {
        if (val) {
          this.todos();
        } else {
          this.list();
        }
      },
    },
    mounted: function () {
      this.list();
      this.get_todos();
      this.$root.eventHub.$on('get_todos', this.get_todos);
    },
    methods: {
      async get_todos() {
        this.todo_number = 0;
        const change_res = await changeTodos({});
        const change_data = change_res.data.data;
        const changes = change_data.changes;
        this.todo_number += changes.length;
        const deploy_res = await deployTodos({});
        const deploy_data = deploy_res.data.data;
        const deploys = deploy_data.deploys;
        this.todo_number += deploys.length;
        this.$root.eventHub.$emit('set_todos', this.todo_number);
      },
      async todos() {
        this.loading = true;
        this.items = [];
        await this.changeTodos();
        await this.deployTodos();
        this.loading = false;
      },
      async list() {
        this.loading = true;
        this.items = [];
        await this.listChange();
        await this.listDeploy();
        this.loading = false;
      },
      async listDeploy() {
        const res = await listDeploy({
          params: {
            close: 0,
          }
        });
        const data = res.data.data;
        const deploys = data.deploys;
        deploys.forEach(value => {
          value.workflow_type = "上线流程";
          this.items.push(value);
        });
      },
      async deployTodos() {
        const res = await deployTodos({});
        const data = res.data.data;
        const deploys = data.deploys;
        deploys.forEach(value => {
          value.workflow_type = "上线流程";
          this.items.push(value);
          this.todo_number += 1;
        });
      },
      async listChange() {
        const res = await listChange({
          params: {
            close: 0,
          }
        });
        const data = res.data.data;
        const changes = data.changes;
        changes.forEach(value => {
          value.workflow_type = "变更流程";
          this.items.push(value);
        });
      },
      async changeTodos() {
        const res = await changeTodos({});
        const data = res.data.data;
        const changes = data.changes;
        changes.forEach(value => {
          value.workflow_type = "变更流程";
          this.items.push(value);
          this.todo_number += 1;
        });
      },
      detail(ID, workflow_type) {
        switch (workflow_type) {
          case "上线流程":
            this.$router.push(`/deploy/detail/${ID}`);
            break;
          case "变更流程":
            this.$router.push(`/change/detail/${ID}`);
            break;
        }
      },
    }
  }
</script>

<style scoped>
  .todo_checkbox {
    width: 214px;
    margin-left: calc(100vw - 214px - 214px - 20px - 288px);
    float: left;
    height: 32px;
    padding-top: 18px;
    padding-bottom: 8px;
  }

  .todo_search {
    width: 256px;
    float: left;
    margin-left: 10px;
    padding-bottom: 10px;
  }
</style>

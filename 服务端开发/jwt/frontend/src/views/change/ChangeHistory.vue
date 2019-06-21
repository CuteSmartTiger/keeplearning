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
              <td>{{ props.item.creator }}</td>
              <td>{{ props.item.create_time | utc2local }}</td>
              <td>{{ props.item.plan_time | utc2local }}</td>
              <td>{{ props.item.system }}</td>
              <td>{{ props.item.update_time | utc2local }}</td>
              <td>
                <ChangeStatus :status="props.item.status"></ChangeStatus>
              </td>
              <td>
                <v-btn small color="blue" dark @click="detail(props.item.ID)">查看详细</v-btn>
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
  import ChangeStatus from '@/components/ChangeStatus';
  import {listChange} from '@/api';

  export default {
    name: 'ChangeHistory',
    components: {
      Breadcrumbs: Breadcrumbs,
      ChangeStatus: ChangeStatus,
    },
    data: () => ({
      breadcrumbs_items: [
        {text: "变更流程"},
        {text: "历史流程"},
      ],
      headers: [
        {
          text: '编号',
          align: 'left',
          sortable: false,
          value: 'ID'
        },
        {text: '申请人', value: 'creator'},
        {text: '申请日期', value: 'create_time'},
        {text: '预计变更时间', value: 'plan_time'},
        {text: '系统', value: 'system'},
        {text: '更新时间', value: 'update_time'},
        {text: '状态', value: 'status'},
        {text: '操作', value: 'action'},
      ],
      items: [],
      loading: true,
      search: '',
    }),
    mounted: function () {
      this.listChange();
    },
    methods: {
      async listChange() {
        this.loading = true;
        const res = await listChange({
          params: {
            close: 1,
          }
        });
        const data = res.data.data;
        const changes = data.changes;
        this.items = changes;
        this.loading = false;
      },
      detail(ID) {
        this.$router.push(`/change/detail/${ID}`);
      }
    }
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

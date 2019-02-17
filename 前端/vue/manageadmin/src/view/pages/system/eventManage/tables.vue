<template>
  <div>
    <Card>
      <tables ref="selection" :highlight-row="true"  editable searchable :searchs="searchs" v-model="tableData" :value="tableData"
              :columns="columns"
              @on-search="onSearch"
      />
      <Page show-sizer :page-size-opts="[5,10,15,20]" @on-page-size-change = "setPageSize" show-total :total="count"  :page-size="page.pagesize" :current="page.pagenumber" style="margin: 10px auto;" @on-change="handleList"/>
    </Card>

  </div>
</template>

<script>
  import Tables from '_c/tables'
  import {getRules} from '@/libs/ruleValidate'
  import {getEventData} from '@/api/event'
  import {getType} from '@/api/common'
  export default {
    name: 'event_manage_page',
    components: {
      Tables
    },
    data() {
      return {
        columns: [
          {title: '类型', key: 'type',width:100},
          {title: '操作', key: 'action',width:100},
          {title: '目标', key: 'target',width:400},
          {title: '执行者', key: 'executor'},
          {title: '创建日期', key: 'created_time'}
        ],
        count: 0,
        searchs: [
          {title: '执行者', key: 'executor'},
          {title: '类型', key: 'type',type: 'select',selects:[]}

        ],
        page: {
          pagesize: 5,
          pagenumber: 1
        },
        tableData: []
      }
    },
    methods: {
      /*修改分页条数*/setPageSize(value){
        this.page.pagesize = value;
        this.handleList()
      },
      /*table分页查询*/handleList(value) {
        if(value != undefined){
          this.page.pagenumber = value;
        }
        getEventData(this.page).then(res => {
          this.tableData = res.data;
          this.count = res.count
        })
      },
      handleType(type) {
        getType(type).then(res => {
          this.searchs[1].selects = res;
        })
      },
      /*修改搜索条件*/onSearch(params) {
        this.page = {pagesize: this.page.pagesize, pagenumber: 1};
        for (let key in params) {
          if (typeof params[key] == "string") {
            this.page[key] = params[key].trim();
          }else {
            this.page[key] = params[key]
          }
          if(this.page[key] + '' == ''){
            delete this.page[key]
          }
        }
        this.handleList()
      }
    },
    mounted() {
      this.handleList()
      this.handleType('EventType')
    }

  }
</script>
<style lang="less">
  .ivu-form-item {
    margin-bottom: 20px;
  }
</style>

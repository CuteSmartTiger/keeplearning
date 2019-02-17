<template>
  <div>
    <Card>
      <tables ref="selection" :highlight-row="true"  searchable :searchs="searchs" v-model="tableData" :value="tableData"
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
  import {getLdapObjData} from '@/api/ldapobjects'
  import {getldapserversData} from '@/api/LDAP'
  import {getType} from '@/api/common'
  export default {
    name: 'ldap_page',
    components: {
      Tables
    },
    data() {
      return {
        columns: [
          {title: '名称', key: 'name'},
          {title: '可区分名称', key: 'distinguished_name'},
          {title: 'GUID', key: 'GUID'},
          {title: '类型', key: 'type'},
          {title: 'LDAP服务器', key: 'ldap_server'}
        ],
        count: 0,
        searchs: [
          {title: '名称', key: 'name'},
          {title: '可区分名称', key: 'distinguished_name'},
          {title: 'GUID', key: 'GUID'},
          {title: '类型', key: 'type', type: 'select' ,selects:[]},
          {title: 'LDAP服务器', key: 'ldap_server' , type: 'select' ,selects:[]}
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
        getLdapObjData(this.page).then(res => {
          this.tableData = res.data;
          this.count = res.count
        })
      },
      handleTypes(type){
        getType(type).then(res => {
          this.searchs[3].selects = res;
        })
      },
      handleServers(){
        getldapserversData().then(res => {
          this.searchs[4].selects = res.data;
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
      this.handleTypes('LdapObjectType')
      this.handleServers()
    }

  }
</script>
<style lang="less">
  .ivu-form-item {
    margin-bottom: 20px;
  }
</style>

<template>
  <div>
    <Card>
      <tables ref="selection" :highlight-row="true"  editable searchable :searchs="searchs" v-model="tableData" :value="tableData"
              :columns="columns"
              @on-delete="handleDelete"
              @on-edit="openEdit"
              @on-search="onSearch"
              @on-selection-change="onSelect"
              @on-row-click="openEdit"
              @on-sort-change='changeSort'
      />
      <Page show-sizer :page-size-opts="[10,20,50,100]" @on-page-size-change = "setPageSize" show-total :total="count"  :page-size="page.pagesize" :current="page.pagenumber" style="margin: 10px auto;" @on-change="handleList"/>
        <Form ref="editForm" :model="editForm" inline>
          <FormItem>
            <Input v-model="editForm.name"  readonly = "readonly" placeholder="单击选中模板" />
          </FormItem>
          <FormItem >
            <Input v-model="editForm.vm_name"  placeholder="虚拟机名前缀" />
          </FormItem>
          <FormItem >
            <FormItem >
              <InputNumber :max="9" :min="1" v-model="editForm.vm_number"></InputNumber>
            </FormItem>
          </FormItem>
          <FormItem >
            启动时重置系统盘
            <i-switch v-model="editForm.revert_on_boot" size="large" :true-value="1" :false-value="0">
              <span slot="open">是</span>
              <span slot="close">否</span>
            </i-switch>
          </FormItem>
          <FormItem >
            <Button type="primary" @click="onEdit('editForm')" icon="ios-add-circle" :disabled="!edit">从模板添加</Button>
          </FormItem>
          <FormItem> <Poptip
            confirm
            title="确定要将选定记录批量删除吗?"
            placement="top"
            @on-ok="handleDeleteAll"
            @on-cancel="cancel">
            <Button  icon="ios-trash" :disabled="selects.length==0">批量删除</Button>
          </Poptip></FormItem>
        </Form>
    </Card>
  </div>
</template>

<script>
  import  Tables from '_c/tables'
  import {getTemplatesData, detailTemplatesData,editTemplatesData,deleteTemplatesData} from '@/api/templates'
  import {getVirtualData} from '@/api/virtual'
  import {getDeviceData} from '@/api/devices'
  export default {
    name: 'terminals_manage_page',
    components: {
      Tables
    },
    data() {
      return {
        edit:false,
        columns: [
          {
            type: 'selection',
            width: 60,
            align: 'center'
          },
          {title: '名称', key: 'name',sortable: true},
          {title: 'UUID', key: 'uuid'},
          {title: '激活状态', key: 'activity'},
          {title: '虚拟化服务器', key: 'host_server',sortable: true},
          {
            title: '操作',
            align: 'center',
            width: 240,
            key: 'handle',
            options: ['delete']
          }
        ],
        devices:[],
        count: 0,
        searchs: [
          {title: '名称', key: 'name'},
          {title: 'UUID', key: 'uuid'},
          {title: '虚拟化服务器', key: 'host_server_id',type: 'select',selects:[]},
        ],
        page: {
          pagesize: 10,
          pagenumber: 1
        },
        editForm: {},
        selects:[],
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
        getTemplatesData(this.page).then(res => {
          this.tableData = res.data;
          this.count = res.count
        })
      },
      handleSelects(){
        getVirtualData().then(res => {
          this.searchs[2].selects = res.data;
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
      },
      /*删除*/handleDelete(params) {
        let id = this.tableData[params.index].id;
        this.onDelete([id])
      },
      handleDeleteAll(){
        const ids = [];
        this.selects.forEach((item)=>{
          ids.push(item.id)
        })
        this.onDelete(ids);
      },
      handleDefault() {
        return {
          id: null,
          vm_number : 1,
          revert_on_boot: 0
        }
      },
      changeSort(params){
        if(params.order === 'asc')
          this.sort = '+';
        else
          this.sort = '-';
        this.page["order"]= this.sort;
        this.page["key"] = params.key;
        getTemplatesData(this.page).then(res => {
          this.tableData = res.data;
          this.count = res.count;
        });
      },
      onSelect(params){
        this.selects = params;
      },
      onDelete(ids){
        const params = {ids:ids}
        deleteTemplatesData(params).then(res => {
          this.$Message.info('删除成功');
          this.page.pagenumber = 1;
          this.editForm = this.handleDefault();
          this.edit = false;
          this.handleList()
        })
      },
      openEdit(params) {
        this.editForm = this.handleDefault()
        this.editForm['id'] = params.id;
        this.editForm['name'] = params.name;
        this.edit = true;
      },
      onEdit() {
        editTemplatesData(this.editForm).then(res => {
          this.$Message.success('添加成功');
          this.editForm = this.handleDefault();
          this.edit = false;
          this.handleList()
        },err =>{
        })

      },
      cancel() {
        this.$Message.info('取消');
      }
    },
    mounted() {
      this.handleList();
      this.handleSelects()

    }

  }
</script>
<style lang="less">
  .ivu-form-item {
    margin-bottom: 20px;
  }
</style>

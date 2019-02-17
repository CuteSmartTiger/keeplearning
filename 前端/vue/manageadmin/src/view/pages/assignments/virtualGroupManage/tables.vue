<template>
  <div>
    <Card>
      <tables ref="selection" :highlight-row="true"  editable searchable :searchs="searchs" v-model="tableData" :value="tableData"
              :columns="columns"
              @on-delete="handleDelete"
              @on-search="onSearch"
              @on-selection-change="onSelect"
              @on-row-click="onSelectOne"
      />
      <Page show-sizer :page-size-opts="[10,20,50,100]" @on-page-size-change = "setPageSize" show-total :total="count"  :page-size="page.pagesize" :current="page.pagenumber" style="margin: 10px auto;" @on-change="handleList"/>
      <Form ref="editForm" :model="editForm"  :rules="ruleValidate" inline>
        <FormItem prop="name">
          <Input v-model="editForm.name" placeholder="虚拟机组" />
          <Icon type="ios-person-outline" slot="prepend"></Icon>
        </FormItem>
        <FormItem>
          <Button type="success" @click="onEdit('add')">添加</Button>
          <Button type="info" @click="onEdit('edit')"  :disabled="editForm.id ==  undefined">修改</Button>
          <Poptip
            confirm
            title="确定要将选定记录批量删除吗?"
            placement="top"
            @on-ok="handleDeleteAll"
            @on-cancel="cancel">
            <Button  icon="ios-trash" :disabled="selects.length==0">批量删除</Button>
          </Poptip>
        </FormItem>
      </Form>
    </Card>

  </div>
</template>

<script>
  import Tables from '_c/tables'
  import {getRules} from '@/libs/ruleValidate'
  import {getvmGroupsData,editvmGroupsData,deletevmGroupsData} from '@/api/vmGroups'
  export default {
    name: 'virtual_group_page',
    components: {
      Tables
    },
    data() {
      return {
        columns: [
          {
            type: 'selection',
            width: 60,
            align: 'center'
          },
          {title: '虚拟机组名称', key: 'name', sortable: true},
          {title: '所有者', key: 'useradmin-*+++++++++++++++++++++++++////////////////////', sortable: true},
          {
            title: '操作',
            align: 'center',
            width: 240,
            key: 'handle',
            options: ['delete']
          }
        ],
        count: 0,
        searchs: [
          {title: '虚拟机组', key: 'name'}
        ],
        page: {
          pagesize: 10,
          pagenumber: 1
        },
        editForm: {},
        ruleValidate: getRules(['name']),
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
        this.editForm = {}
        this.$refs['editForm'].resetFields();
        if(value != undefined){
          this.page.pagenumber = value;
        }
        getvmGroupsData(this.page).then(res => {
          res.data.forEach((item,index)=>{
            item['_disabled'] = !item.selectable;
          })
          this.tableData = res.data;
          this.count = res.count
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
      onSelect(params){
        this.selects = params;
      },
      onSelectOne(p){
        this.editForm = p;
      },
      onDelete(ids){
        const params = {ids:ids}
        deletevmGroupsData(params).then(res => {
          this.$Message.info('删除成功');
          this.page.pagenumber = 1;
          this.$refs['editForm'].resetFields();
          this.handleList()
        })
      },
      cancel() {
        this.$refs['editForm'].resetFields();
        this.$Message.info('取消');
      },
      onEdit(type) {
        if(type == 'add'){
          delete this.editForm['id'];
        }
        this.$refs['editForm'].validate((valid) => {
          if (valid) {
            const data = {id:this.editForm['id'],name:this.editForm.name}
            editvmGroupsData(data).then(res => {
              if(this.editForm.id != undefined){
                this.$Message.success('修改成功');
              }else{
                this.$Message.success('新增成功');
              }
              this.handleList()
            })
          }
        })

      }
    },
    mounted() {
      this.handleList()
    }

  }
</script>
<style lang="less">
  .ivu-form-item {
    margin-bottom: 20px;
  }
</style>

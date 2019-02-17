<template>
  <div>
    <Card>
      <tables ref="selection" :highlight-row="true"  editable searchable :searchs="searchs" v-model="tableData" :value="tableData"
              :columns="columns"
              @on-delete="handleDelete"
              @on-edit="openEdit"
              @on-search="onSearch"
              @on-selection-change="onSelect"
      />
      <Page show-sizer :page-size-opts="[5,10,15,20]" @on-page-size-change = "setPageSize" show-total :total="count"  :page-size="page.pagesize" :current="page.pagenumber" style="margin: 10px auto;" @on-change="handleList"/>
      <Button type="primary" @click="openAdd" icon="ios-add-circle">添加</Button>
      <Poptip
        confirm
        title="确定要将选定记录批量删除吗?"
        placement="top"
        @on-ok="handleDeleteAll"
        @on-cancel="cancel">
        <Button  icon="ios-trash" :disabled="selects.length==0">批量删除</Button>
      </Poptip>
      <Modal
        v-model="model.edit.open"
        :title="model.edit.title"
        :width="300"
        :mask-closable="false"
        :loading="model.edit.loading"
        :ok-text="editForm.id!= undefined?'修改':'添加'"
        @on-ok="onEdit('editForm')"
        @on-cancel="cancel">
        <Form ref="editForm" :model="editForm" :label-width="80" :rules="ruleValidate">
          <FormItem label="名称" prop="name">
            <Input v-model="editForm.name" placeholder="名称4-20个字符"/>
          </FormItem>
          <FormItem label="类型">
            <Select v-model="editForm.type" placeholder="请选择">
              <Option v-for="item in types" :value="item.id" :key="item.id">{{item.name}}</Option>
            </Select>
          </FormItem>
          <FormItem label="主机名称" prop="hostname">
            <Input v-model="editForm.hostname" placeholder="请输入" />
          </FormItem>
          <FormItem label="用户名称" prop="username">
            <Input v-model="editForm.username" placeholder="请输入"/>
          </FormItem>
          <FormItem label="密码" prop="password">
           <Input v-model="editForm.password" placeholder="密码6-16个字符" type="password" />
          </FormItem>
          <FormItem >
            <Button  type="primary"  @click="onTest('editForm')"  :loading = 'test.status ==1'>测试连接</Button>

            <Icon v-show="test.status == 2"
                  :type="test.result == 1 ? 'ios-checkmark-circle':'ios-close-circle'"
                  :color="test.result == 1 ? '#19be6b':'#ed4014'" :size="20" />
            <span v-show="test.status !=0">{{test.btnText}}</span>
          </FormItem>
        </Form>
      </Modal>
    </Card>

  </div>
</template>

<script>
  import Tables from '_c/tables'
  import {getRules} from '@/libs/ruleValidate'
  import {getDeviceData, detailDeviceData,editDeviceData,testDeviceData,deleteDeviceData} from '@/api/devices'
  import {getType} from '@/api/common'
  export default {
    name: 'device_manage_page',
    components: {
      Tables
    },
    data() {
      return {
        edit: false,
        model: {
          edit: {
            loading: true,
            open: false,
            title: ""
          }
        },
        columns: [
          {
            type: 'selection',
            width: 60,
            align: 'center'
          },
          {title: '名称', key: 'name'},
          {title: '类型', key: 'type'},
          {title: '主机名称', key: 'hostname'},
          {
            title: '操作',
            align: 'center',
            width: 240,
            key: 'handle',
            options: ['delete', 'edit']
          }
        ],
        types: [],
        test:{'btnText':'测试连接',loading:false,status:0,result:0},
        count: 0,
        searchs: [
          {title: '名称', key: 'name'}
        ],
        page: {
          pagesize: 5,
          pagenumber: 1
        },
        addDefault: {
          type: 0
        },
        editForm: {},
        ruleValidate: getRules(['name','password','username','hostname']),
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
        getDeviceData(this.page).then(res => {
          this.tableData = res.data;
          this.count = res.count
        })
      },
      handleType(type) {
        getType(type).then(res => {
          this.types = res;
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
      onDelete(ids){
        const params = {ids:ids}
        deleteDeviceData(params).then(res => {
          this.$Message.info('删除成功');
          this.page.pagenumber = 1;
          this.handleList()
        })
      },
      openAdd() {
        this.model.edit.open = true;
        this.model.edit.title = '新增'
        this.$refs['editForm'].resetFields();
        this.editForm = this.addDefault;
      },
      openEdit(params) {
        let id = this.tableData[params.index].id;
        detailDeviceData(id).then(res => {
          this.editForm = res;
          this.model.edit.open = true;
          this.model.edit.title = '编辑';
        })

      },
      onEdit(type) {
        this.test.status = 0;
        this.$refs[type].validate((valid) => {
          if (valid) {
            editDeviceData(this.editForm).then(res => {
              if(this.editForm.id != undefined){
                this.$Message.success('修改成功');
              }else{
                this.$Message.success('新增成功');
              }
              this.$refs['editForm'].resetFields();
              this.editForm = this.addDefault;
              this.model.edit.open = false;
              this.model.edit.loading  = true;
              this.handleList()
            },err =>{
              this.model.edit.loading = false;
              this.$nextTick(() => {
                this.model.edit.loading  = true;
              });
            })
          }else{
            this.model.edit.loading = false;
            this.$nextTick(() => {
              this.model.edit.loading  = true;
            });
          }
        })

      },
      onTest(type) {
        this.test.status = 0;
        this.$refs[type].validate((valid) => {
          if (valid) {
            this.test.status = 1;
            this.test.btnText = '测试中...';
            testDeviceData(this.editForm).then(res => {
              this.test.btnText = '测试通过';
              this.test.result = 1;
              this.test.status = 2;
            },error => {
              this.test.status = 2;
              this.test.btnText = '测试失败';
              this.test.result = 0;
            })
          }

        })

      },
      cancel() {
        this.$refs['editForm'].resetFields();
        this.model.edit.loading = false;
        this.$nextTick(() => {
          this.model.edit.loading  = true;
        });

      }
    },
    mounted() {
      this.handleList()
      this.handleType('DeviceManagerType')
      this.editForm = this.addDefault;
    }

  }
</script>
<style lang="less">
  .ivu-form-item {
    margin-bottom: 20px;
  }
</style>

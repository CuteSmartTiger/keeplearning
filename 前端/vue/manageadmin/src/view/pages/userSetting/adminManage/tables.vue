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
      <Form ref="addForm" :model="editForm"  :rules="ruleValidate" v-show="model.edit.open == false"  inline>
        <FormItem prop="name">
          <Input v-model="editForm.name" placeholder="用户名4-16个字符" autocomplete="off" style="width:0;height:0;float:left;visibility:hidden"/>
          <Input v-model="editForm.name" placeholder="用户名4-16个字符" autocomplete="off"/>
          </Input>
        </FormItem>
        <FormItem prop="password">
          <Input v-model="editForm.password" placeholder="密码6-16个字符" autocomplete="off"  type="password" style="width:0;height:0;float:left;visibility:hidden"/>
          <Input v-model="editForm.password" placeholder="密码6-16个字符" autocomplete="off"  type="password"/>
          </Input>
        </FormItem>
        <FormItem>
          <Button type="success" @click="onEdit('addForm')" icon="ios-person-add">添加用户</Button>
          <!--<Button type="primary" @click="openAdd" icon="ios-person-add">添加用户</Button>-->
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
      <Modal
        v-model="model.edit.open"
        :title="model.edit.title"
        :width="300"
        :mask-closable="false"
        :loading="model.edit.loading"
        :ok-text="editForm.id!= undefined?'保存':'添加'"
        @on-ok="onEditPassword('editForm')"
        @on-cancel="cancel">
        <Form ref="editForm" :model="editForm" :label-width="80" :rules="ruleValidate">
          <FormItem label="用户名称" prop="name">
            <Input v-model="editForm.name" placeholder="用户名称" :disabled="editForm.id != undefined" autocomplete="off"/>
          </FormItem>
          <FormItem label="密码" prop="password" >
            <Input v-model="editForm.password" placeholder="密码6-16个字符" type="password" autocomplete="off" />
          </FormItem>
          <!--<FormItem label="策略">-->
            <!--<Select v-model="editForm.policy_id" placeholder="请选择">-->
              <!--<Option v-for="item in policies" :value="item.id" :key="item.id">{{item.name}}</Option>-->
            <!--</Select>-->
          <!--</FormItem>-->
          <!--<FormItem label="用户组">-->
            <!--<Select v-model="editForm.group_id" placeholder="请选择">-->
              <!--<Option v-for="item in groups" :value="item.id" :key="item.id">{{item.name}}</Option>-->
            <!--</Select>-->
          <!--</FormItem>-->
        </Form>
      </Modal>
    </Card>

  </div>
</template>

<script>
  import Tables from '_c/tables'
  import {getRules} from '@/libs/ruleValidate'
  import {getUserData, getUserInfo,editUserData,editPasswordData,deleteUserData} from '@/api/admins'
  import {getGroupsData} from '@/api/userGroups'
  import {getPoliciesData} from '@/api/policies'
  export default {
    name: 'admin_manage_page',
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
          {title: '管理员名称', key: 'name', sortable: true},
          {
            title: '操作',
            align: 'center',
            width: 240,
            key: 'handle',
            options: ['delete', 'edit']
          }
        ],
        groups: [],
        policies: [],
        count: 0,
        searchs: [
          {title: '用户名称', key: 'name', sortable: true}
        ],
        page: {
          pagesize: 5,
          pagenumber: 1
        },
        editForm: {},
        ruleValidate: getRules(['name','password']),
        selects:[],
        tableData: []
      }
    },
    methods: {
      /*修改分页条数*/setPageSize(value){
        this.page.pagesize = value;
        this.handleList()
      },
      handleDefault() {
        return {
          name: "",
          password: ""
        }
      },
      /*table分页查询*/handleList(value) {
        this.$refs['editForm'].resetFields();this.$refs['addForm'].resetFields();
        this.editForm = this.handleDefault();
        if(value != undefined){
          this.page.pagenumber = value;
        }
        getUserData(this.page).then(res => {
          res.data.forEach((item,index)=>{
            item['_disabled'] = !item.deletable;
          })
          this.tableData = res.data;
          this.count = res.count
        })
      },
      handleGroups(){
        getGroupsData().then(res => {
          this.groups = res.data;
        })
      },
      handlePolicies(){
        getPoliciesData().then(res => {
          this.policies = res.data;
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
        deleteUserData(params).then(res => {
          this.$Message.info('删除成功');
          this.page.pagenumber = 1;
          this.handleList()
        })
      },
      openAdd() {
        this.$refs['editForm'].resetFields();this.$refs['addForm'].resetFields();
        this.editForm = this.handleDefault();
        this.model.edit.open = true;
        this.model.edit.title = '新增管理员';
      },
      openEdit(params) {
        this.$refs['editForm'].resetFields();this.$refs['addForm'].resetFields();
        let id = this.tableData[params.index].id;
        getUserInfo(id).then(res => {
          this.editForm = res;
          this.model.edit.open = true;
          this.model.edit.title = '编辑管理员';
        })

      },
      onEdit(type) {
        if(this.editForm.id == undefined){
          this.$refs[type].validate((valid) => {
            if (valid) {
              this.postEdit()
            }else{
              this.model.edit.loading = false;
              this.$nextTick(() => {
                this.model.edit.loading  = true;
              });
            }
          })
        }else{
          this.postEdit()
        }


      },
      postEdit(){
        editUserData(this.editForm).then(res => {
          if(this.editForm.id != undefined){
            this.$Message.success('修改成功');
          }else{
            this.$Message.success('新增成功');
          }
          this.$refs['editForm'].resetFields();this.$refs['addForm'].resetFields();
          this.editForm = this.handleDefault();
          this.model.edit.open = false;
          this.model.edit.loading  = true;
          this.handleList()
        },err =>{
          this.model.edit.loading = false;
          this.$nextTick(() => {
            this.model.edit.loading  = true;
          });
        })
      },
      onEditPassword(type) {
        this.$refs[type].validate((valid) => {
          if (valid) {
            let data = {
              id: this.editForm.id,
              password: this.editForm.password
            }
            editPasswordData(data).then(res => {
              this.model.edit.open = false;
              this.model.edit.loading  = true;
              this.editForm = this.handleDefault();
              this.$Message.success('修改密码成功');
            },err =>{
              this.model.edit.loading = false;
              this.$nextTick(() => {
                this.model.edit.loading  = true;
              });
            })
          }
        })
      },
      cancel() {
        this.$refs['editForm'].resetFields();this.$refs['addForm'].resetFields();
        this.editForm = this.handleDefault();
        this.$Message.info('取消');
      }
    },
    mounted() {
      this.handleList()
      this.handleGroups()
      this.handlePolicies()
      this.editForm = this.handleDefault();
    }

  }
</script>
<style lang="less">
  .ivu-form-item {
    margin-bottom: 20px;
  }
</style>

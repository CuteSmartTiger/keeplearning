<template>
  <div>
    <Card>
      <tables ref="selection"
              :highlight-row="true"
              editable searchable
              :searchs="searchs" v-model="tableData" :value="tableData"
              :columns="columns"
              @on-delete="handleDelete"
              @on-edit="openEdit"
              :ok-text="editForm.id!= undefined?'修改':'添加'"
              @on-search="onSearch"
              @on-selection-change="onSelect"
      />
      <Page show-sizer :page-size-opts="[5,10,15,20]" @on-page-size-change = "setPageSize" show-total :total="count"  :page-size="page.pagesize" :current="page.pagenumber" style="margin: 10px auto;" @on-change="handleList"/>
      <Form ref="addForm" :model="editForm"  :rules="ruleValidate" v-show="model.edit.open == false" inline >
        <!--<FormItem prop="name">-->
          <!--<Input v-model="editForm.name" placeholder="用户名4-16个字符" />-->
          <!--<Icon type="ios-person-outline" slot="prepend"></Icon>-->
          <!--</Input>-->
        <!--</FormItem>-->
        <!--<FormItem prop="password">-->
          <!--<Input v-model="editForm.password" placeholder="密码6-16个字符" type="password" />-->
          <!--<Icon type="ios-locked-outline" slot="prepend"></Icon>-->
          <!--</Input>-->
        <!--</FormItem>-->
        <FormItem prop="count">
          <!--<InputNumber :max="99" :min="1" v-model="editForm.count"></InputNumber>-->
        </FormItem>
        <FormItem>
          <!--<Button type="success" @click="onEdit('addForm')" icon="ios-person-add">快速添加用户</Button>-->
          <Button type="primary" @click="openAdd" icon="ios-person-add">添加用户</Button>
          <Poptip
            confirm
            title="确定要将选定记录批量删除吗?"
            placement="top"
            @on-ok="handleDeleteAll"
            @on-cancel="cancel">
            <Button  icon="ios-trash" :disabled="selects.length==0">批量删除</Button>
          </Poptip>
        </FormItem>
        <FormItem >
          <Upload
            :on-success="uploadSuccess"
            :on-error="uploadError"
            :data="uploadForm"
            :format="['xls','xlsx']"
            :on-format-error="handleFormatError"
            :name="Excel"
            :show-upload-list="false"
            action="/v2/users/add_users_from_excel">
            <Button type="primary" icon="ios-cloud-upload-outline" >选择Excel表</Button>
          </Upload>

        </FormItem>
      </Form>
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
          <FormItem label="用户名称" prop="name">
            <Input v-model="editForm.name" placeholder="名称4-20个字符" type="s" />
          </FormItem>
          <FormItem label="密码" prop="password" v-if="editForm.id == undefined">
            <Input v-model="editForm.password" placeholder="密码6-16个字符" type="password" />
          </FormItem>
          <FormItem label="密码" prop="password2" v-if="editForm.id != undefined">
            <Row>
              <Col :span="12"><Input v-model="editForm.password" placeholder="密码6-16个字符" type="password" /></Col>
              <Col :span="12" style="text-align: right"><Button @click="onEditPassword('editForm')" type="success">修改密码</Button></Col>
            </Row>

          </FormItem>
          <FormItem label="策略">
            <Select v-model="editForm.policy_id" placeholder="请选择" v-if="policies.length > 0">
              <Option v-for="item in policies" :value="item.id" :key="item.id">{{item.name}}</Option>
            </Select>
            <router-link to="/policies/policies_manage_page"><Button v-if = "policies.length == 0" icon="ios-link">去添加策略</Button></router-link>
          </FormItem>
          <FormItem label="用户组">
            <Select v-model="editForm.group_id" placeholder="请选择" v-if = "groups.length > 0">
              <Option v-for="item in groups" :value="item.id" :key="item.id">{{item.name}}</Option>
            </Select>
            <router-link to="user_group_page"><Button v-if = "groups.length == 0" icon="ios-link">去添加用户组</Button></router-link>
          </FormItem>
          <FormItem label="数量" prop="count" v-if="editForm.id == undefined" >
            <InputNumber :max="99" :min="1" v-model="editForm.count"  ></InputNumber>
          </FormItem>
        </Form>
      </Modal>
    </Card>

  </div>
</template>

<script>
  import Tables from '_c/tables'
  import {getRules} from '@/libs/ruleValidate'
  import {getUserData, getUserInfo,editUserData,deleteUserData,editPasswordData,addexcel} from '@/api/users'
  import {getGroupsData} from '@/api/userGroups'
  import {getPoliciesData} from '@/api/policies'
  export default {
    name: 'user_manage_page',
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
          {title: '用户名称', key: 'name'},
          {title: '用户组', key: 'group', sortable: true},
          {title: '策略名称', key: 'policy', sortable: true},
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
          {title: '用户名称', key: 'name', sortable: true},
          {title: '用户组', key: 'group_id',type:'select',selects:[]},
          {title: '策略名称', key: 'policy_id',type:'select',selects:[]},

        ],
        page: {
          pagesize: 5,
          pagenumber: 1
        },
        editForm: {},
        ruleValidate: getRules(['name','password','count','password2']),
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
        this.$refs['editForm'].resetFields();this.$refs['addForm'].resetFields();
        this.editForm = this.handleDefault();
        if(value != undefined){
          this.page.pagenumber = value;
        }
        getUserData(this.page).then(res => {
          this.tableData = res.data;
          this.count = res.count
        })
      },
      handleGroups(){
        getGroupsData().then(res => {
          this.searchs[1].selects = this.groups = res.data;

        })
      },
      handlePolicies(){
        getPoliciesData().then(res => {
          this.searchs[2].selects = this.policies = res.data;
        })
      },
      handleDefault() {
        return {
          policy_id: 1,
          group_id: 1,
          count:1
        }
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
        this.model.edit.open = true;
        this.$refs['editForm'].resetFields();this.$refs['addForm'].resetFields();
        this.editForm = this.handleDefault();
        this.model.edit.title = '新增用户';
      },
      openEdit(params) {
        this.$refs['editForm'].resetFields();this.$refs['addForm'].resetFields();
        let id = this.tableData[params.index].id;
        getUserInfo(id).then(res => {
          this.editForm = res;
          this.model.edit.open = true;
          this.model.edit.title = '编辑用户';
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
              this.$Message.success('修改密码成功');
            },err =>{

            })
          }
        })
      },
      onEdit(type) {
        this.$refs[type].validate((valid) => {
          if (this.editForm.id != undefined || valid) {
            editUserData(this.editForm).then(res => {
              if(this.editForm.id != undefined){
                this.$Message.success('修改成功');
              }else{
                this.$Message.success('新增成功');
              }
              this.model.edit.open = false;
              this.model.edit.loading  = true;
              this.editForm = this.handleDefault();
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
      cancel() {
        this.$refs['addForm'].resetFields();
        this.$refs['editForm'].resetFields();
        this.editForm = this.handleDefault()
        this.$Message.info('取消');
      },

      handleFormatError (file) {
        this.$Message.warning('文件 ' + file.name + ' 格式不正确，请上传 Excel文件。');
      },
      uploadSuccess (res) {
        this.$Message.success(res.data)
      },
      uploadError (res) {
        console.log(res.data)
        addexcel(this.editForm).then(res => {
            this.$Message.error(res.data);
        },err =>{
          this.$nextTick(() => {
            this.model.edit.loading  = true;
          });
        })
      },
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

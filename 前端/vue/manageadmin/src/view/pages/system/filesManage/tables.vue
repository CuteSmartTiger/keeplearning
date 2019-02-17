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
      />
      <Page show-sizer :page-size-opts="[5,10,15,20]" @on-page-size-change = "setPageSize" show-total :total="count"  :page-size="page.pagesize" :current="page.pagenumber" style="margin: 10px auto;" @on-change="handleList"/>
      <Form ref="editForm" :model="editForm"  inline >
        <FormItem v-show="isShow">
          <Input v-model="editForm.name"  readonly = "readonly" />
        </FormItem>
        <FormItem v-show="isShow">
          是否最新
          <i-switch v-model="editForm.mark_latest" size="large" :true-value="1" :false-value="0">
            <span slot="open">是</span>
            <span slot="close">否</span>
          </i-switch>
        </FormItem>
        <FormItem v-show="isShow">
          <Button type="primary" @click="onEdit('editForm')">修改包状态</Button>
        </FormItem>
        <FormItem>
          <Button type="primary" @click="openAdd" icon="ios-add-circle">添加</Button>
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
        @on-ok="cancel"
        @on-cancel="cancel">
        <Form ref="addForm" :model="addForm" :label-width="80" :rules="ruleValidate">
          <FormItem label="文件名称" prop="name">
            <Input v-model="addForm.name" placeholder="请输入" :disabled="addForm.id != undefined"
                   @on-change="setName"/>
          </FormItem>

          <FormItem label="类型">
            <Select v-model="addForm.type" placeholder="请选择">
              <Option v-for="item in types" :value="item.id" :key="item.id">{{item.name}}</Option>
            </Select>
          </FormItem>
          <FormItem label="是否最新" v-if ="addForm.type == 1">
            <i-switch v-model="addForm.mark_latest" size="large" :true-value="1*1" :false-value="0*0">
              <span slot="open">是</span>
              <span slot="close">否</span>
            </i-switch>
          </FormItem>
          <FormItem  v-if ="addForm.type == 0" label="温馨提示">
            <Alert type="warning" show-icon>Agent只支持zip包并小于200M</Alert>
          </FormItem>
          <FormItem  v-if ="addForm.type == 2" label="温馨提示">
            <Alert type="warning" show-icon >文件小于200M</Alert>
          </FormItem>
        </Form>
        <div  slot="footer">
          <Upload
            :before-upload="handleUpload"
            :data="addForm"
            :on-success="uploadSuccess"
            :on-error="uploadError"
            name="file"
            action="/v2/packages/">
            <Button icon="ios-cloud-upload-outline" :disabled = "edit">选择上传文件</Button>
          </Upload>
        </div>
      </Modal>
    </Card>
  </div>
</template>

<script>
  import Tables from '_c/tables'
  import {getRules} from '@/libs/ruleValidate'
  import {getFilesData, detailFilesData,editFilesData,testFilesData,deleteFilesData} from '@/api/files'
  import {getType} from '@/api/common'
  import expandRow from '_c/tables/table-expand.vue';
  import baseURL from '_conf/url';
  export default {
    name: 'files_manage_page',
    components: {
      Tables,expandRow
    },
    data() {
      return {
        edit: true,
        isShow: false,
        model: {
          edit: {
            loading: true,
            open: false,
            title: ""
          }
        },
        columns: [
          {
            type: 'expand',
            width: 50,
            render: (h, params) => {
              return h(expandRow, {
                props: {
                  row: params.row,
                  columns: [
                    {title: '包版本', key: 'package_version'},
                    {title: 'uuid', key: 'uuid'}
                  ]
                }
              })
            }
          },
          {
            type: 'selection',
            width: 60,
            align: 'center'
          },
          {title: '软件包名称', key: 'name'},
          {title: '文件名称', key: 'filename',
          render (h, column, index) {
                  return h('a', {
                    attrs: {
                      target: "_blank",
                      href: column.row.download_package_path
                    }
                  }, column.row.filename);
          }},
          {title: '类型', key: 'type'},
          {title: '创建日期', key: 'created_time'},
          {title: '是否最新', key: 'mark_latest'},
          {
            title: '操作',
            align: 'center',
            width: 120,
            key: 'handle',
            options: ['delete']
          }
        ],
        types: [{id:0,name:'Agent软件包'},{id:1,name:'终端软件包'},{id:2,name:'用户文件'}],
        mark_latests: [{id:0,name:'非最新'},{id:1,name:'最新'}],
        uploadUrl:baseURL+"/v2/packages/",
        count: 0,
        searchs: [
          {title: '软件包名称', key: 'name'},
          {title: '类型', key: 'type',type: 'select',selects:[]},
        ],
        page: {
          pagesize: 5,
          pagenumber: 1
        },
        addDefault: {
          type: 0,
          mark_latest: 1,
          file: null
        },
        addForm: {},
        editForm: { mark_latest: 1},
        ruleValidate: getRules(['name']),
        selects:[],
        tableData: []
      }
    },
    methods: {
      handleUpload (file) {
        if(this.addForm.type != 1){
          this.addForm.mark_latest = 4
        }
        return true;
      },
      setName(){
        if(this.addForm.name && this.addForm.name != ''){
          this.edit = false ;
        }else{
          this.edit = true;
        }
      },
      uploadSuccess () {
        this.$Message.success('上传成功')
        this.addForm.file = null;
        this.edit = true;
        this.cancel();
      },
      uploadError (error, file, fileList) {
        this.$Message.error('上传失败')
        this.addForm.file = null;
      },
      /*修改分页条数*/setPageSize(value){
        this.page.pagesize = value;
        this.handleList()
      },
      /*table分页查询*/handleList(value) {
        if(value != undefined){
          this.page.pagenumber = value;
        }
        getFilesData(this.page).then(res => {
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
        deleteFilesData(params).then(res => {
          this.$Message.info('删除成功');
          this.page.pagenumber = 1;
          this.handleList()
        })
      },
      openAdd() {
        this.model.edit.open = true;
        this.model.edit.title = '新增';
      },
      openEdit(params) {
        if(params.type_value && params.type_value == 1){
          this.editForm = {};
          this.editForm['id'] = params.id;
          this.editForm['name'] = params.name;
          this.editForm['mark_latest'] = params.mark_latest_value;
          this.isShow = true;
        }else{
          this.isShow = false;
        }

      },
      onEdit(type) {
        editFilesData(this.editForm).then(res => {
          this.$Message.success('修改成功');
          this.$refs[type].resetFields();
          this.editForm = { mark_latest: 1};
          this.isShow = false;
          this.handleList()
        },err =>{})

      },
      cancel() {
        this.$refs['addForm'].resetFields();
        this.addForm = this.addDefault;
        this.handleList();

      }
    },
    mounted() {
      this.handleList()
      this.addForm = this.addDefault;
      this.searchs[1].selects = this.types
    }

  }
</script>
<style lang="less">
  .ivu-form-item {
    margin-bottom: 20px;
  }
</style>

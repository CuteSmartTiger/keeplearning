<template>
  <div>
    <Card>
      <tables ref="selection" :highlight-row="true"  editable searchable :searchs="searchs" v-model="tableData" :value="tableData"
              :columns="columns"
              :rowClassName="rowClassName"
              @on-delete="handleDelete"
              @on-search="onSearch"
              @on-selection-change="onSelect"
              @on-row-click="openEdit"
              @on-sort-change='changeSort'
      />
      <Page show-sizer :page-size-opts="[10,20,50,100]" @on-page-size-change = "setPageSize" show-total :total="count"  :page-size="page.pagesize" :current="page.pagenumber" style="margin: 10px auto;" @on-change="handleList"/>
      <Form ref="editForm" :model="editForm"  :rules="ruleValidate" inline>
        <FormItem  v-show="edit">
          <Input v-model="editForm.name"  :disabled="true" />
        </FormItem>
        <FormItem prop="alias"  v-show="edit">
          <Input v-model="editForm.alias" placeholder="别名"/>
        </FormItem>
        <FormItem>
          <Button type="primary" @click="onEdit('editForm')" v-show="edit" icon="md-create">修改别名</Button>
          <Button  type="primary" icon="ios-archive" :disabled="selects.length==0" @click="model.package.open = true" v-if="files.length>0" >推送终端软件包</Button>
          <Button type="success" @click="onDownloadDate()" :disabled="selects.length==0" icon="ios-download">获取终端日志</Button>
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
        v-model="model.package.open"
        :title="model.package.title"
        :width="300"
        :mask-closable="false"
        :loading="model.package.loading"
        ok-text="推送"
        @on-ok="onPackage('packageForm')"
        @on-cancel="cancel">
        <Form ref="packageForm" :model="packageForm" :label-width="80" >
          <FormItem  label="终端软件包">
            <Select v-model="packageForm.package_id" placeholder="请选择">
              <Option v-for="item in files" :value="item.id" :key="item.id">{{item.name}}</Option>
            </Select>
          </FormItem>
        </Form>
      </Modal>
    </Card>

  </div>
</template>

<script>
  import Tables from '_c/tables'
  import {getRules} from '@/libs/ruleValidate'
  import {getTerminalsData, detailTerminalsData,editTerminalsData,pushPackage,deleteTerminalsData,getLog} from '@/api/terminals'
  import {getDeviceData} from '@/api/devices'
  import {getFilesData} from '@/api/files'
  import {getType} from '@/api/common'
  import expandRow from '_c/tables/table-expand.vue';
  export default {
    name: 'terminals_manage_page',
    components: {
      Tables,
      expandRow
    },
    data() {
      return {
        edit: false,
        model: {
          package: {
            loading: true,
            open: false,
            title: "推送到虚拟机"
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
                    {title: '名称', key: 'name'},
                    {title: '别名', key: 'alias'},
                    {title: '连接', key: 'connectivity'},
                    {title: '状态', key: 'status'},
                    {title: 'IP地址', key: 'ipv4'},
                    {title: '版本', key: 'vdi_version'},
                    {title: '设备管理', key: 'device_manager'},
                    {title: '登录用户', key: 'terminaluser'},
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
          {title: '名称', key: 'name',width: 200,},
          {title: '登录用户', key: 'terminaluser'},
          {title: '别名', key: 'alias',sortable: true},
          {title: '状态', key: 'status', className: 'status',sortable: true},
          {title: 'IP地址', key: 'ipv4',sortable: true},
          {title: '版本', key: 'vdi_version',sortable: true},
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
          {title: 'IP', key: 'ipv4'},
          {title: '版本', key: 'vdi_version'},
          {title: '别名', key: 'alias'},
          {title: '状态', key: 'status',type:'select',selects:[]},
          {title: '登录用户', key: 'user'},
        ],
        files:[],
        page: {
          pagesize: 10,
          pagenumber: 1
        },
        editForm: {},
        packageForm: {package_id:0,ids:[]},
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
        this.$refs['editForm'].resetFields();
        this.editForm = {};
        this.edit = false;
        if(value != undefined){
          this.page.pagenumber = value;
        }
        getTerminalsData(this.page).then(res => {
          this.tableData = res.data;
          this.count = res.count
        })
      },
      changeSort(params){
        if(params.order === 'asc')
          this.sort = '+';
        else
          this.sort = '-';
        this.page["order"]= this.sort;
        this.page["key"] = params.key;
        getTerminalsData(this.page).then(res => {
          this.tableData = res.data;
          this.count = res.count;
        });
      },
      handleDevice(){
        getDeviceData().then(res => {
          this.devices = res.data;
          this.devices.unshift({id:-1,name:'<空>'})
        })
        getFilesData().then(res => {
          res.data.forEach((item,index)=>{
            switch (item.type_value){
              case 1:
                this.files.push(item)
                break;
              default:
                break;
            }
          })
          if(this.files.length>0){
            this.packageForm = {package_id:this.files[0].id};
          }
        })
      },
      handleSelects() {
        getType('TerminalStatus').then(res => {
          this.searchs[4].selects = res;
        })
      },
      /*修改搜索条件*/onSearch(params){
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
        deleteTerminalsData(params).then(res => {
          this.$Message.info('删除成功');
          this.page.pagenumber = 1;
          this.handleList()
        })
      },
      onPackage(type) {
        const ids = [];
        this.selects.forEach((item)=>{
          ids.push(item.id)
        })
        this.packageForm['ids'] = ids;
        pushPackage(this.packageForm).then(res => {
          this.$Message.success('推送成功');
          this.model.package.open = false;
          this.$refs[type].resetFields();
          if(this.files0.length>0){
            this.packageForm = {package_id:this.files0[0].id};
          }

          this.model.package.open = false;
          this.model.package.loading  = true;
        },err=> {
          this.model.package.loading = false;
          this.$nextTick(() => {
            this.model.package.loading = true;
          })
        })
      },
      onDownloadDate() {
        const ids = [];
        this.selects.forEach((item)=>{
          ids.push(item.id)
        })
        const params = {ids:ids}
        getLog(params).then(res => {
          if (res != null && res.url != undefined && res.url != '') {
            window.location.href = res.url;
          } else {
            this.$Message.error('下载地址获取失败');
          }
        })

      },
      openEdit(params) {
        this.editForm['id'] = params.id;
        this.editForm['name'] = params.name;
        this.editForm['alias'] = params.alias;
        this.edit = true;
      },
      onEdit(type) {
        this.$refs[type].validate((valid) => {
          if (valid) {
            editTerminalsData(this.editForm).then(res => {
              if(this.editForm.id != undefined){
                this.$Message.success('修改成功');
              }else{
                this.$Message.success('新增成功');
              }
              this.$refs['editForm'].resetFields();
              this.editForm = {};
              this.edit = false;
              this.handleList()
            })
          }else{

          }
        })

      },
      cancel() {
        this.$refs['editForm'].resetFields();
        this.editForm = {};
        this.$Message.info('取消');
      },
      rowClassName(row,index) {
        if(row.status == '在线'){
          return 'status-success'
        }else if(row.status == '离线'){
          return 'status-error'
        }else{
          return 'status-warning'
        }
      }
    },
    mounted() {
      this.handleList()
      this.handleDevice()
      this.handleSelects()
    }

  }
</script>
<style lang="less">
  .ivu-form-item {
    margin-bottom: 20px;
  }
  .status-success{
    .status{
      color:#19be6b;
    }
  }
  .status-warning{
  .status{
    color:#ff9900;
  }
  }
  .status-error{
  .status{
    color:#ed4014;
  }
  }
</style>

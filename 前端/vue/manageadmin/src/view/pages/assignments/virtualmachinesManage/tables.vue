<template>
  <div>
    <Card>

      <tables ref="selection" :highlight-row="true"  editable searchable :searchs="searchs" v-model="tableData" :value="tableData"
              :columns="columns"
              :rowClassName="rowClassName"
              @on-edit="openEdit"
              @on-search="onSearch"
              @on-selection-change="onSelect"
              @on-sort-change='changeSort'

      />
      <Page show-sizer :page-size-opts="[10,20,50,100]" @on-page-size-change = "setPageSize" show-total :total="count"  :page-size="page.pagesize" :current="page.pagenumber" style="margin: 10px auto;" @on-change="handleList"/>
      <Modal
        v-model="model.edit.open"
        :title="model.edit.title"
        :width="300"
        :mask-closable="false"
        :loading="model.edit.loading"
        ok-text="修改"
        @on-ok="onEdit('editForm')"
        @on-cancel="cancel">
        <Form ref="editForm" :model="editForm" :label-width="80" >
          <FormItem label="名称">
            <Input v-model="editForm.name"  :disabled="true" />
          </FormItem>
          <FormItem  label="模板">
            <Select v-model="editForm.template_id" placeholder="请选择">
              <Option v-for="item in templates" :value="item.id" :key="item.id">{{item.name}}</Option>
            </Select>
          </FormItem>
          <FormItem  label="虚拟机组">
            <Select v-model="editForm.vmgroup_id" placeholder="请选择">
              <Option v-for="item in vmGroups" :value="item.id" :key="item.id">{{item.name}}</Option>
            </Select>
          </FormItem>
        </Form>
      </Modal>
      <Modal
        v-model="model.modify.open"
        :title="model.modify.title"
        :width="380"
        :mask-closable="false"
        :loading="model.modify.loading"
        ok-text="修改"
        @on-ok="onModify('modifyVMForm')"
        @on-cancel="cancel">
        <Form ref="modifyVMForm" :model="modifyVMForm" :label-width="80" :rules="ruleValidate">
          <FormItem label="计算机名" placeholder="修改计算机名">
            <Input v-model="modifyVMForm.computername"  />
          </FormItem>

          <FormItem label="模板" placeholder="修改模板">
            <Select v-model="modifyVMForm.template_id" placeholder="请选择">
              <Option v-for="item in templates" :value="item.id" :key="item.id">{{item.name}}</Option>
            </Select>
          </FormItem>
          <FormItem  label="虚拟机组">
            <Select v-model="modifyVMForm.vmgroup_id" placeholder="请选择">
              <Option v-for="item in vmGroups" :value="item.id" :key="item.id">{{item.name}}</Option>
            </Select>
          </FormItem>
          <FormItem label="是否修改IP">
            <i-switch v-model="modifyVMForm.switch" size="large">
              <span slot="open">是</span>
              <span slot="close">否</span>
            </i-switch>
          </FormItem>
          <FormItem label="IP类型" v-show="modifyVMForm.switch">
            <input type="radio" name="type" value="static" v-model="modifyVMForm.iptype"/>
            <label for="one">静态</label>
            <input type="radio" name="type" value="dhcp" v-model="modifyVMForm.iptype"/>
            <label for="two">动态</label>
          </FormItem>
          <FormItem label="起始IP"  prop="ip1" ref="modifyVMForm" v-show="modifyVMForm.switch && modifyVMForm.iptype == 'static'">
            <!--<Input v-model="modifyVMForm.ip"/>-->
            <InputNumber :max="255" :min="0" maxlength="3"  v-model="modifyVMForm.ip1" style="width: 50px;text-align: center;" ></InputNumber>.
            <InputNumber :max="255" :min="0" maxlength="3"  number  v-model="modifyVMForm.ip2" style="width: 50px;text-align: center;"></InputNumber>.
            <InputNumber :max="255" :min="0" maxlength="3"  number  v-model="modifyVMForm.ip3" style="width: 50px;text-align: center;"></InputNumber>.
            <InputNumber :max="255" :min="0" maxlength="3"  number v-model="modifyVMForm.ip4" style="width: 50px;text-align: center;"></InputNumber>
          </FormItem>
          <FormItem label="子网掩码" prop="netmask1" v-show="modifyVMForm.switch && modifyVMForm.iptype == 'static'">
            <!--<Input v-model="modifyVMForm.netmask"/>-->
            <InputNumber :max="255" :min="0" maxlength="3"  v-model="modifyVMForm.netmask1" style="width: 50px;text-align: center;"/>.
            <InputNumber :max="255" :min="0" maxlength="3"  v-model="modifyVMForm.netmask2" style="width: 50px;text-align: center;"/>.
            <InputNumber :max="255" :min="0" maxlength="3"  v-model="modifyVMForm.netmask3" style="width: 50px;text-align: center;"/>.
            <InputNumber :max="255" :min="0" maxlength="3"  v-model="modifyVMForm.netmask4" style="width: 50px;text-align: center;"/>
          </FormItem>
          <FormItem label="网关地址" prop="gateway1" v-show="modifyVMForm.switch && modifyVMForm.iptype == 'static'">
            <!--<Input v-model="modifyVMForm.gateway"/>-->
            <InputNumber :max="255" :min="0" maxlength="3"  v-model="modifyVMForm.gateway1"  style="width: 50px;text-align: center;"/>.
            <InputNumber :max="255" :min="0" maxlength="3"  v-model="modifyVMForm.gateway2"  style="width: 50px;text-align: center;"/>.
            <InputNumber :max="255" :min="0" maxlength="3"  v-model="modifyVMForm.gateway3"  style="width: 50px;text-align: center;"/>.
            <InputNumber :max="255" :min="0" maxlength="3"  v-model="modifyVMForm.gateway4"  style="width: 50px;text-align: center;"/>
          </FormItem>
          <FormItem label="DNS地址" v-show="modifyVMForm.switch &&  modifyVMForm.iptype">
            <!--<Input v-model="modifyVMForm.dns"/>-->
            <InputNumber :max="255" :min="0" maxlength="3"  v-model="modifyVMForm.dns1" style="width: 50px;text-align: center;"></InputNumber>.
            <InputNumber :max="255" :min="0" maxlength="3"  v-model="modifyVMForm.dns2" style="width: 50px;text-align: center;"></InputNumber>.
            <InputNumber :max="255" :min="0" maxlength="3"  v-model="modifyVMForm.dns3" style="width: 50px;text-align: center;"></InputNumber>.
            <InputNumber :max="255" :min="0" maxlength="3"  v-model="modifyVMForm.dns4" style="width: 50px;text-align: center;"></InputNumber>
          </FormItem>

        </Form>

      </Modal>
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
          <FormItem  label="Agent软件包">
            <Select v-model="packageForm.package_id" placeholder="请选择">
              <Option v-for="item in files0" :value="item.id" :key="item.id">{{item.name}}</Option>
            </Select>
          </FormItem>
        </Form>
      </Modal>
      <Modal
        v-model="model.files.open"
        :title="model.files.title"
        :width="300"
        :mask-closable="false"
        :loading="model.files.loading"
        ok-text="分发"
        @on-ok="onFiles('filesForm')"
        @on-cancel="cancel">
        <Form ref="filesForm" :model="filesForm" :label-width="120" :rules="ruleValidate" >
          <FormItem label="文件存储位置" prop="file_location">
            <Input v-model="filesForm.file_location"  />
          </FormItem>
          <FormItem  label="文件名称">
            <Select v-model="filesForm.package_id" placeholder="请选择">
              <Option v-for="item in files1" :value="item.id" :key="item.id">{{item.name}}</Option>
            </Select>
          </FormItem>
        </Form>
      </Modal>
      <Button  type="primary" :disabled="selects.length==0" @click="model.package.open = true" v-if="files0.length>0">推送Agent软件包</Button>
      <Button  type="primary" :disabled="selects.length==0" @click="model.files.open = true"  v-if="files1.length > 0">分发用户文件</Button>
      <Button type="success" @click="onDownloadDate()" :disabled="selects.length==0" icon="ios-download">获取虚拟机日志</Button>
      <Button type="success" @click="openModifyVM" :disabled="selects.length==0" icon="ios-download">批量修改虚拟机参数信息</Button>
    </Card>

  </div>
</template>

<script>
  import Tables from '_c/tables'
  import {getRules} from '@/libs/ruleValidate'
  import {getVirtualmachinesData,getLog, detailVirtualmachinesData,editVirtualmachinesData,deleteVirtualmachinesData,pushPackage,pushUserfile,modifyVirtualmachines} from '@/api/virtualmachines'
  import {getVirtualData} from '@/api/virtual'
  import {getvmGroupsData} from '@/api/vmGroups'
  import {getTemplatesData} from '@/api/templates'
  import {getFilesData} from '@/api/files'
  import expandRow from '_c/tables/table-expand.vue';
  import {getType} from '@/api/common'
  export default {
    name: 'terminals_manage_page',
    components: {
      Tables,
      expandRow
    },
    data() {
      return {
        model: {
          edit: {
            loading: true,
            open: false,
            title: ""
          },
          modify: {
            loading: true,
            open: false,
            title: "修改虚拟机参数"
          },
          package: {
            loading: true,
            open: false,
            title: "推送到虚拟机"
          },
          files: {
            loading: true,
            open: false,
            title: "分发到虚拟机"
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
                    {title: 'UUID', key: 'uuid'},
                    {title: '激活状态', key: 'activity'},
                    {title: '设备管理', key: 'device_manager'},
                  ]
                }
              })
            }
          },
          {
            type: 'selection',
            width: 60,
            align: 'center',
          },
          {title: '名称', key: 'name',width: 200,sortable: true},
          {title: '模板', key: 'template',sortable: true},
          {title: '虚拟化服务器', key: 'host_server',sortable: true},
          {title: '电源状态', key: 'power_state', className: 'status',sortable: true},
          {title: 'Agent状态', key: 'agent_status'},
          {title: 'IP地址', key: 'ipv4',sortable: true},
          {title: '虚拟机组', key: 'vmgroup'},
          {title: '版本', key: 'vdi_version'},
          {
            title: '操作',
            align: 'center',
            width: 240,
            key: 'handle',
            options: ['edit']
          }
        ],
        devices:[],
        templates:[],
        vmGroups: [],
        files0:[],
        files1:[],
        searchs: [
          {title: '名称', key: 'name'},
          {title: 'UUID', key: 'uuid'},
          {title: '虚拟化服务器', key: 'host_server_id',type: 'select',selects:[]},
          {title: '电源状态', key: 'power_state',type: 'select',selects:[]},
          {title: '虚拟机组', key: 'vmgroup_id',type: 'select',selects:[]},
          // {title: 'Agent状态', key: 'agent_status',type: 'select',selects:[]},

        ],
        count: 0,
        page: {
          pagesize: 10,
          pagenumber: 1
        },
        editForm: {},
        packageForm: {package_id:0,vms:[]},
        filesForm: {package_id:0,vms:[]},
        modifyVMForm: {ids:[],ip1:null,ip2:null,ip3:null,ip4:null,netmask1:null,netmask2:null,netmask3:null,netmask4:null,
                        gateway1:null,gateway2:null,gateway3:null,gateway4:null,
                          dns1:null,dns2:null,dns3:null,dns4:null},
        ruleValidate: getRules(['file_location','ip1','netmask1','gateway1']),
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
        getVirtualmachinesData(this.page).then(res => {
          this.tableData = res.data;
          this.count = res.count

        })
      },

      handleDefault() {
        return {
          ids:[],switch:false,iptype:null,ip1:null,ip2:null,ip3:null,ip4:null,netmask1:null,netmask2:null,netmask3:null,netmask4:null,
          gateway1:null,gateway2:null,gateway3:null,gateway4:null,
          dns1:null,dns2:null,dns3:null,dns4:null
        }
      },
      handlevalidate(){
        if(this.modifyVMForm.ip2 && this.modifyVMForm.ip3 && this.modifyVMForm.ip4 && this.modifyVMForm.gateway2
          && this.modifyVMForm.gateway3 && this.modifyVMForm.gateway4 && this.modifyVMForm.netmask2 && this.modifyVMForm.netmask3
          && this.modifyVMForm.gateway4){
          return true
        }else {
          return false
        }
      },
      handleSelects(){
        getvmGroupsData().then(res => {
          this.vmGroups = res.data;
          this.searchs[4].selects = res.data;
        });
        getTemplatesData().then(res => {
          this.templates = res.data;
        });
        // getType('AgentStatus').then(res => {
        //   this.searchs[4].selects = res;
        // });
        getType('VirtualMachinePowerState').then(res => {
          this.searchs[3].selects = res;
        });
        getVirtualData().then(res => {
          this.searchs[2].selects = res.data;
        });


        getFilesData().then(res => {
          res.data.forEach((item,index)=>{
              switch (item.type_value){
                case 0:
                  this.files0.push(item)
                   break;
                case 2:
                  this.files1.push(item)
                  break;
                default:
                  break;
              }
          })
          if(this.files0.length>0){
            this.packageForm = {package_id:this.files0[0].id};
          }
          if(this.files1.length>0){
            this.filesForm = {package_id:this.files1[0].id};
          }
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
      // /*删除*/handleDelete(params) {
      //   let id = this.tableData[params.index].id;
      //   this.onDelete([id])
      // },
      // handleDeleteAll(){
      //   const ids = [];
      //   this.selects.forEach((item)=>{
      //     ids.push(item.id)
      //   })
      //   this.onDelete(ids);
      // },
      onSelect(params){
        this.selects = params;
      },
      // onDelete(ids){
      //   const params = {ids:ids}
      //   deleteVirtualmachinesData(params).then(res => {
      //     this.$Message.info('删除成功');
      //     this.page.pagenumber = 1;
      //     this.handleList()
      //   })
      // },
      changeSort(params){
        if(params.order === 'asc')
          this.sort = '+';
        else
          this.sort = '-';
        this.page["order"]= this.sort;
        this.page["key"] = params.key;
        getVirtualmachinesData(this.page).then(res => {
          this.tableData = res.data;
          this.count = res.count;
        });
      },
      openEdit(params) {
        let id = this.tableData[params.index].id;
        detailVirtualmachinesData(id).then(res => {
          this.editForm = res;
          this.model.edit.open = true;
          this.model.edit.title = '编辑';
        })
      },
      openModifyVM(params){
        const ids = [];
        this.selects.forEach((item)=>{
          ids.push(item.id)
        })
        this.model.modify.open = true;
        this.model.modify.title = '修改';
        this.modifyVMForm['ids'] = ids

      },
      onPackage(type) {
        const vms = [];
        this.selects.forEach((item)=>{
          vms.push(item.id)
        })
        this.packageForm['vms'] = vms;
        pushPackage(this.packageForm).then(res => {
          this.$Message.success('推送成功');
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
      onFiles(type) {
        this.$refs[type].validate((valid) => {
          if (valid) {
            const vms = [];
            this.selects.forEach((item)=>{
              vms.push(item.id)
            })
            this.filesForm['vms'] = vms;
            pushUserfile(this.filesForm).then(res => {
              this.$Message.success('分发成功');
              this.$refs[type].resetFields();
              if(this.files1.length>0){
                this.filesForm = {package_id:this.files1[0].id};
              }
              this.model.files.open = false;
              this.model.files.loading  = true;
            },err=> {
              this.model.files.loading= false;
              this.$nextTick(() => {
                this.model.files.loading  = true;
              })
            })
          }else{
            this.model.files.loading= false;
            this.$nextTick(() => {
              this.model.files.loading  = true;
            })
          }
        })

      },
      onEdit(type) {
        editVirtualmachinesData(this.editForm).then(res => {
            if(this.editForm.id != undefined){
              this.$Message.success('修改成功');
            }else{
              this.$Message.success('新增成功');
            }
            this.model.edit.open = false;
            this.model.edit.loading  = true;
            this.handleList()
          },err=> {
          this.model.edit.loading = false;
          this.$nextTick(() => {
            this.model.edit.loading = true;
          })
        })
      },
      onModify(type) {
        if(this.modifyVMForm.switch && this.modifyVMForm.iptype=='static'){
          this.$refs[type].validate((valid) => {
            if(valid && this.handlevalidate()){
              modifyVirtualmachines(this.modifyVMForm).then(res => {
                this.$Message.success('修改成功');
                this.model.modify.open = false;
                this.$refs['modifyVMForm'].resetFields();
                this.modifyVMForm = this.handleDefault();
                this.model.modify.loading = true;
              }, err => {
                this.model.modify.loading = false;
                this.$nextTick(() => {
                  this.model.modify.loading = true;
                })
              })
            }else {
              this.model.modify.loading= false;
              this.$nextTick(() => {
                this.model.modify.loading  = true;
              })
            }
          })
        }else {
          modifyVirtualmachines(this.modifyVMForm).then(res => {
            this.$Message.success('修改成功');
            this.model.modify.open = false;
            this.$refs['modifyVMForm'].resetFields();
            this.model.modify.loading = true;
          }, err => {
            this.model.modify.loading = false;
            this.$nextTick(() => {
              this.model.modify.loading = true;
            })
          })
          }
      },
      cancel(){
        this.$refs['editForm','packageForm','filesForm','modifyVMForm'].resetFields();
        this.editForm = {};
        this.filesForm = {};
        this.packageForm = {};
        this.modifyVMForm = this.handleDefault();
        if(this.files0.length>0){
          this.packageForm = {package_id:this.files0[0].id};
        }
        if(this.files1.length>0){
          this.filesForm = {package_id:this.files1[0].id};
        }
        this.$Message.info('取消');
      },
      rowClassName(row,index) {
        if(row.power_state == '运行中'){
          return 'status-success'
        }else if(row.power_state == '关机'){
          return 'status-error'
        }else{
          return 'status-warning'
        }
      }
    },
    mounted() {
      this.handleList()
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


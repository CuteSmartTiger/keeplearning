<template>
  <div>
    <Card>
      <tables ref="selection" :highlight-row="true"  editable searchable :searchs="searchs" v-model="tableData" :value="tableData"
              :columns="columns"
              :rowClassName="rowClassName"
              @on-delete="handleDelete"
              @on-undo="handleUndo"
              @on-edit="openEdit"
              @on-search="onSearch"
              @on-selection-change="onSelect"
              @on-sort-change='changeSort'
      />
      <Page show-sizer :page-size-opts="[10,20,50,100]" @on-page-size-change = "setPageSize" show-total :total="count"  :page-size="page.pagesize" :current="page.pagenumber" style="margin: 10px auto;" @on-change="handleList"/>
      <Button type="primary" @click="openAdd" icon="ios-add-circle">添加</Button>
      <Poptip
        confirm
        title="确定要将选定记录批量删除吗?"
        placement="top"
        ok-text="永久删除"
        cancel-text="临时删除"
        @on-ok="handleDeleteAll(false)"
        @on-cancel="handleDeleteAll(true)">
        <Button  icon="ios-trash" :disabled="selects.length==0">批量删除</Button>
      </Poptip>
      <Poptip
        confirm
        title="确定要将选定记录批量撤销删除吗?"
        placement="top"
        ok-text="确定"
        cancel-text="取消"
        @on-ok="handleUndoAll()"
        @on-cancel="cancel">
        <Button  icon="ios-undo" :disabled="selects.length==0">批量撤销</Button>
      </Poptip>
      <Modal
        v-model="model.edit.open"
        :title="model.edit.title"
        :width="700"
        :mask-closable="false"
        :loading="model.edit.loading"
        :ok-text="editForm.id!= undefined?'修改':'添加'"
        @on-ok="onEdit('editForm')"
        @on-cancel="cancel">

        <Form ref="editForm" :model="editForm" :label-width="80" :rules="ruleValidate">
          <FormItem label="自动修改虚拟机名字">
            <i-switch v-model="editForm.switch" size="large">
              <span slot="open">是</span>
              <span slot="close">否</span>
            </i-switch>
          </FormItem>
          <Row>
            <Col :span="12" class="trees" >
              <Input search  enter-button v-show="editForm.id ==undefined" @on-search="() => this.searchuser(editForm.searchContent)" type="text" placeholder="输入关键字搜索" v-model="editForm.searchContent" style="width: 200px" />
            <p>LDAP用户</p>
              <Tree :data="ldap_objs"  show-checkbox  :getSelectedNodes="editForm.ldap_objects" ref="ldap_objs"></Tree>
            <p>用户组</p>
              <Tree :data="ows" show-checkbox filterable :getSelectedNodes="editForm.users" ref="ows" ></Tree>
            </Col>
            <Col :span="12" class="trees">
              <Input search  enter-button  @on-search="() => this.searchvm(editForm.searchVM)" type="text" placeholder="输入关键字搜索" v-model="editForm.searchVM" style="width: 200px" />
              <p>虚拟机组</p>
              <Tree :data="mcs" show-checkbox  :getSelectedNodes="editForm.vms" ref="mcs"></Tree>
            </Col>
          </Row>
        </Form>
      </Modal>
    </Card>
  </div>
</template>

<script>
  /**
   * 资源分配
   * */
  import Tables from '_c/tables'
  import {getRules} from '@/libs/ruleValidate'
  import {getAssignmentsData, detailAssignmentsData,editAssignmentsData,deleteAssignmentsData,undoAssignmentsData,TreeOwner,TreeMachines,TreeLDAPOwner} from '@/api/assignments'
  import {getType} from '@/api/common'
  // import Search from "iview/src/components/transfer/search";
  export default {
    name: 'assignments_manage_page',
    components: {
      // Search,
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
        },//弹窗
        columns: [
          {
            type: 'selection',
            width: 60,
            align: 'center'
          },
          {title: '所有者', key: 'users',sortable: true},
          {title: '资源', key: 'vms',sortable: true},
          {
            title: '操作',
            align: 'center',
            width: 240,
            key: 'handle',
            options: ['delete2', 'edit']
          }
        ],//表字段
        count: 0,//分页总条数
        searchs: [//筛选条件
          {title: '所有者', key: 'name'},
          // {title: '资源', key: 'virtual_machines'},
        ],
        page: {//分页
          pagesize: 10,
          pagenumber: 1
        },
        addDefault: {//表单默认值
          ldap_objects: [],
          users: [],
            vms: [],
          searchContent:'',
          searchVM:''
        },
        editForm: {searchContent:'',searchVM:''},//表单
        searchForm:{},
        ruleValidate: getRules(['name','password','username','hostname']),//表单验证
        selects:[],//table多选
        tableData: [],//table数据
        ldap_objs: [],//LDAP用户组
        ows: [],//用户组
        mcs: []//终端组
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
        getAssignmentsData(this.page).then(res => {
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
      /*搜索树*/
      searchuser(value){
        TreeOwner(value).then(res => {
          this.getOwner(res)
          this.ows = res;
        })
      },
      searchvm(value){
        TreeMachines(value).then(res => {
          this.getMcs(res);
          this.mcs = res;
        })
      },
      /*删除*/handleDelete(params) {
        let id = this.tableData[params.index].id;
        let isDelete = params.isDelete;
        this.onDelete([id],isDelete)
      },
      handleUndo(params) {
        let id = this.tableData[params.index].id;
        this.onUndo([id])
      },
      handleUndoAll() {
        const ids = [];
        this.selects.forEach((item)=>{
          ids.push(item.id)
        })
        this.onUndo(ids);
      },
      onUndo(ids){
        const params = {ids:ids}
        undoAssignmentsData(params).then(res => {
          this.$Message.info('撤销删除成功');
          this.page.pagenumber = 1;
          this.handleList()
        })
      },
      changeSort(params){
        if(params.order === 'asc')
          this.sort = '+';
        else
          this.sort = '-';
        this.page["order"]= this.sort;
        this.page["key"] = params.key;
        getAssignmentsData(this.page).then(res => {
          this.tableData = res.data;
          this.count = res.count;
        });
      },
      handleDeleteAll(isDelete){
        const ids = [];
        this.selects.forEach((item)=>{
          ids.push(item.id)
        })
        this.onDelete(ids,isDelete);
      },
      handleTreeOwner() {
        TreeOwner(this.searchForm).then(res => {
          this.getOwner(res)
          this.ows = res;
        })
      },
      getOwner(list) {
        let owsStr = this.editForm.users.join(",")+"," || '';
        list.forEach((item)=>{
           if(item.parent_group == "owner"){
             item['title'] =  item.group_name+'组';
             item['expand'] = true;
             item['render'] =  (h, { root, node, data }) => {
               return h('span', {
                 style: {
                   display: 'inline-block',
                   width: '100%'
                 }
               }, [
                 h('span', [
                   h('Icon', {
                     props: {
                       type: 'ios-people'
                     },
                     style: {
                       marginRight: '8px',
                       fontSize:'18px',
                       color: '#ff9900'
                     }
                   }),
                   h('span', data.title)
                 ])
               ])
             }
           }else{
             item['title'] = item.username;
             item['render'] =  (h, { root, node, data }) => {
               return h('span', {
                 style: {
                   display: 'inline-block',
                   width: '100%'
                 }
               }, [
                 h('span', [
                   h('Icon', {
                     props: {
                       type: 'md-person'
                     },
                     style: {
                       marginRight: '8px',
                       color: '#2db7f5'
                     }
                   }),
                   h('span', data.title)
                 ])
               ])
             }
             let str = item.user_id+",";
             if(owsStr.includes(str)){
               item.checked =  true
             }
          }
           if(item.children && item.children.length>0){
             this.getOwner(item.children);
           }


        })

      },

      // LDAPobjects

      handleTreeLdapobjects() {
        TreeLDAPOwner(this.searchForm).then(res => {
          this.getLdap(res)
          this.ldap_objs = res;
        })
      },
      getLdap(list) {
        let ldap_objsStr = this.editForm.ldap_objects.join(",")+"," || '';
        list.forEach((item)=>{
          if(item.parent_group == "LDAP"){
            item['title'] =  item.group_name+'组';
            item['expand'] = true;
            item['render'] =  (h, { root, node, data }) => {
              return h('span', {
                style: {
                  display: 'inline-block',
                  width: '100%'
                }
              }, [
                h('span', [
                  h('Icon', {
                    props: {
                      type: 'ios-people'
                    },
                    style: {
                      marginRight: '8px',
                      fontSize:'18px',
                      color: '#ff9900'
                    }
                  }),
                  h('span', data.title)
                ])
              ])
            }
          }else{
            item['title'] = item.ldap_object_name;
            item['render'] =  (h, { root, node, data }) => {
              return h('span', {
                style: {
                  display: 'inline-block',
                  width: '100%'
                }
              }, [
                h('span', [
                  h('Icon', {
                    props: {
                      type: 'md-person'
                    },
                    style: {
                      marginRight: '8px',
                      color: '#2db7f5'
                    }
                  }),
                  h('span', data.title)
                ])
              ])
            }
            let str = item.ldap_object_id+",";
            if(ldap_objsStr.includes(str)){
              item.checked =  true
            }
          }
          if(item.children && item.children.length>0){
            this.getLdap(item.children);
          }


        })

      },


      handleTreeMachines() {
        TreeMachines(this.searchForm).then(res => {
          this.getMcs(res);
          this.mcs = res;

        })
      },
      getMcs(list) {
        let mcsStr = this.editForm.vms.join(",")+"," || '';
        list.forEach((item)=>{

          if(item.parent_group == "resource"){
            item['title'] = '服务器-'+item.host_server_name;
            item['expand'] = true;
            item['render'] =  (h, { root, node, data }) => {
              return h('span', {
                style: {
                  display: 'inline-block',
                  width: '100%'
                }
              }, [
                h('span', [
                  h('Icon', {
                    props: {
                      type: 'ios-desktop'
                    },
                    style: {
                      marginRight: '8px',
                      fontSize:'18px',
                      color: '#2d8cf0'
                    }
                  }),
                  h('span', data.title)
                ])
              ])
            }
          }else{

            item['title'] = item.virtual_machine_name;
            item['render'] =  (h, { root, node, data }) => {
              return h('span', {
                style: {
                  display: 'inline-block',
                  width: '100%'
                }
              }, [
                h('span', [
                  h('Icon', {
                    props: {
                      type: 'md-desktop'
                    },
                    style: {
                      marginRight: '8px',
                      color: '#5cadff'
                    }
                  }),
                  h('span', data.title)
                ])
              ])
            }
            let str = item.virtual_machine_id+",";
            if(mcsStr.includes(str)){
              item['checked'] =  true
            }
          }
          if(item.children && item.children.length>0){
            this.getMcs(item.children);
          }
        });

      },
      onSelect(params){
        this.selects = params;
      },
      onDelete(ids,isDelete){
        const params = {ids:ids,isDelete:isDelete}
        deleteAssignmentsData(params).then(res => {
          this.$Message.info('删除成功');
          // this.page.pagenumber = 1;
          this.handleList()
        })
      },
      openAdd() {
        this.model.edit.open = true;
        this.model.edit.title = '新增';
        this.searchForm = {};
        this.editForm = this.addDefault;
        this.editForm.switch=true;
        this.editForm.users=[];
        this.editForm.searchContent='';
        this.editForm.searchVM='';
        this.handleTreeMachines();
        this.handleTreeOwner();
        this.handleTreeLdapobjects();
      },
      openEdit(params) {
        let id = this.tableData[params.index].id;

        detailAssignmentsData(id).then(res => {
          this.editForm = res;
          this.model.edit.open = true;
          this.model.edit.title = '编辑';
          this.editForm.switch=true;
          this.searchForm = {id:res.id};
          this.handleTreeMachines();
          this.handleTreeOwner();
        })

      },
      onEdit() {
        const oChecked = this.$refs['ows'].getCheckedNodes();
        const lChecked = this.$refs['ldap_objs'].getCheckedNodes();
        const mChecked = this.$refs['mcs'].getCheckedNodes();
        this.editForm.users = [];
        this.editForm.ldap_objects = [];
        this.editForm.vms = [];
        // this.editForm.editForm = [];
        if(oChecked.length >0){
          oChecked.forEach((item)=>{
            if((item.childen == undefined || item.childen.length == 0) && item.group_id == undefined){
              this.editForm.users.push(item.user_id);
            }
          })
        } else if (lChecked.length>0){
          lChecked.forEach((item)=>{
            if((item.children == undefined || item.children.length == 0) && item.group_id == undefined){
              this.editForm.ldap_objects.push(item.ldap_object_id);
            }
          })
        } else{
          this.$Message.error('请勾选用户');
          this.model.edit.loading = false;
          this.$nextTick(() => {
            this.model.edit.loading  = true;
          });
          return false;
        }
        if(mChecked.length>0){
          mChecked.forEach((item)=>{
            if((item.childen == undefined || item.childen.length == 0) && item.host_server_id == undefined){
              this.editForm.vms.push(item.virtual_machine_id);
            }

          })
        }else{
          this.$Message.error('请勾选虚拟机');

          this.model.edit.loading = false;
          this.$nextTick(() => {
            this.model.edit.loading  = true;
          });
          return false;
        }
        if(this.editForm.vms.length == 0){
          this.$Message.error('请勾选虚拟机');
          this.model.edit.loading = false;
          this.$nextTick(() => {
            this.model.edit.loading  = true;
          });
          return false;
        }
        if(this.editForm.users.length == 0 && this.editForm.ldap_objects.length == 0){
          this.$Message.error('请勾选用户');
          this.model.edit.loading = false;
          this.$nextTick(() => {
            this.model.edit.loading  = true;
          });
          return false;
        }
        editAssignmentsData(this.editForm).then(res => {
          if(this.editForm.id != undefined){
            this.$Message.success('修改成功');
          }else{
            this.$Message.success('新增成功');
          }
          this.$refs['editForm'].resetFields();
          this.editForm = this.addDefault;
          this.editForm.vms = [];
          this.model.edit.open = false;
          this.model.edit.loading = true;
          this.handleList()
        },err =>{
          this.model.edit.loading = false;
          this.$nextTick(() => {
            this.model.edit.loading  = true;
          });
        })

      },
      cancel() {
        this.$refs['editForm'].resetFields();
        this.editForm = this.addDefault;
        this.model.edit.loading = false;
        this.$nextTick(() => {
          this.model.edit.loading  = true;
        });

      },
      rowClassName(row,index) {
      if(row.isDelete){
          return 'undo'
        }
      }
    },
    mounted() {
      this.handleList()
      this.editForm = this.addDefault;
    }

  }
</script>
<style lang="less">
  .ivu-form-item {
    margin-bottom: 20px;
  }
  .trees{
    height: 400px;
    overflow-y: auto;
    overflow-x: hidden;
  }
  .undo{
    text-decoration:line-through;
  }
</style>

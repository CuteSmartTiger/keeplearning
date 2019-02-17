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
      <Page
            show-sizer :page-size-opts="[10,20,50,100]" @on-page-size-change = "setPageSize" show-total :total="count"  :page-size="page.pagesize"
            :current="page.pagenumber" style="margin: 10px auto;"
            @on-change="handleList"/>
      <Button type="primary" @click="openAdd" icon="ios-add-circle">新增</Button>
      <Poptip
        confirm
        title="确定要将选定记录批量删除吗?"
        placement="top"
        @on-ok="handleDeleteAll"
        @on-cancel="cancel">
        <Button  :disabled="selects.length==0" icon="ios-trash">批量删除</Button>
      </Poptip>
      <Modal
        v-model="model.edit.open"
        :title="model.edit.title"
        :mask-closable="false"
        :loading="model.edit.loading"
        :ok-text="editForm.id!= undefined?'修改':'添加'"
        @on-ok="onEdit"
        @on-cancel="cancel">
        <Form ref="editForm" :model="editForm" :label-width="130" :rules="ruleValidate">
          <FormItem label="策略名称" prop="name">
            <Input v-model="editForm.name" placeholder="请输入" />
          </FormItem>
          <FormItem label="USB 重定向">
            <i-switch v-model="editForm.usb_redirection" size="large">
              <span slot="open">是</span>
              <span slot="close">否</span>
            </i-switch>

          </FormItem>
          <FormItem label="USB 存储重定向" v-show="editForm.usb_redirection">
            <Row >
              <Col span="6">
                <Select v-model="editForm.mass_storage_redirection" placeholder="请选择">
                  <Option v-for="item in mass_storage_redirections" :value="item.key" :key="item.key">{{item.value}}</Option>
                </Select>
              </Col>
              <Col span="10"  offset="2">
                <Label>打印机重定向</Label>
                <i-switch v-model="editForm.printer_redirection" size="large">
                  <span slot="open">是</span>
                  <span slot="close">否</span>
                </i-switch>
              </Col>
            </Row>
          </FormItem>
          <FormItem label="自动登录进虚拟机">
            <Row >
              <Col span="4">
                <i-switch v-model="editForm.auto_login" size="large">
                  <span slot="open">是</span>
                  <span slot="close">否</span>
                </i-switch>
              </Col>
              <Col span="9" offset="1">
                <Label>独占桌面</Label>
                <i-switch v-model="editForm.dedicated_desktop" size="large">
                  <span slot="open">是</span>
                  <span slot="close">否</span>
                </i-switch>
              </Col>

            </Row>

          </FormItem>
          <FormItem :style="{textAlign:'right'}"><Button @click="expert = !expert" >高级<Icon type="ios-arrow-down" v-show="expert"></Icon><Icon type="ios-arrow-up"  v-show="!expert"></Icon></Button></FormItem>
          <div v-show="expert">
          <FormItem label="断开连接后锁屏">
            <i-switch v-model="editForm.lock_screen" size="large">
              <span slot="open">是</span>
              <span slot="close">否</span>
            </i-switch>
          </FormItem>
            <FormItem label="IDV模式">
              <i-switch v-model="editForm.idv_mode" size="large">
              <span slot="open">是</span>
              <span slot="close">否</span>
            </i-switch>
            </FormItem>
          <FormItem label="MAC地址过滤">
            <Row>
              <Col span="6">
                <i-switch v-model="editForm.mac_addr_filter" size="large">
                  <span slot="open">是</span>
                  <span slot="close">否</span>
                </i-switch>
              </Col>
              <Col span="18">
                <Input v-model="editForm.mac_addr_string" placeholder="允许连接的MAC地址" :disabled="editForm.mac_addr_filter == false"/>
              </Col>
            </Row>
          </FormItem>
          <FormItem label="协议类型">
            <Row>
              <Col span="6">
              <i-switch v-model="editForm.auto_protocol" size="large">
                <span slot="open">自动</span>
                <span slot="close">手动</span>
              </i-switch>
              </Col>
              <Col span="18">
              <Select v-model="editForm.protocol_type" placeholder="请选择" :disabled="editForm.auto_protocol == true">
                <Option v-for="item in protocol_types" :value="item.key" :key="item.key">{{item.value}}</Option>
              </Select>
              </Col>
            </Row>
          </FormItem>
          <FormItem label="FPS">
            <Row>
              <Col span="6">
              <i-switch v-model="editForm.auto_fps" size="large">
                <span slot="open">自动</span>
                <span slot="close">手动</span>
              </i-switch>
              </Col>
              <Col span="18">
              <Input v-model="editForm.fps" placeholder="请输入" :disabled="editForm.auto_fps == true"/>
              </Col>
            </Row>
          </FormItem>
          <FormItem label="比特率(Mbit/s)">
            <Input v-model="editForm.bit_rate" placeholder="请输入"/>
          </FormItem>
          <FormItem label="质量(%)">
            <Slider v-model="editForm.quality" show-input></Slider>
          </FormItem>
          <FormItem label="允许从网关连接">
            <Row >
              <Col span="4">
              <i-switch v-model="editForm.gateway" size="large">
                <span slot="open">是</span>
                <span slot="close">否</span>
              </i-switch>

              </Col>
              <Col span="9" offset="1">
              <Label>&nbsp;&nbsp;3D支持</Label>
              <i-switch v-model="editForm.d3d" size="large">
                <span slot="open">是</span>
                <span slot="close">否</span>
              </i-switch>
              </Col>
              <Col span="9" offset="1">
              <Label>&nbsp;联动关机</Label>
              <i-switch v-model="editForm.linkage_shutdown" size="large">
                <span slot="open">是</span>
                <span slot="close">否</span>
              </i-switch>
              </Col>
            </Row>
          </FormItem>

          </div>

        </Form>

      </Modal>
    </Card>

  </div>
</template>

<script>
  import Tables from '_c/tables'
  import {getRules} from '@/libs/ruleValidate'
  import {getPoliciesData, getPoliciesInfo,editPolicies,deletePolicies} from '@/api/policies'

  export default {
    name: 'policies_manage_page',
    components: {
      Tables
    },
    data() {
      return {
        expert: false,
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
          {title: '策略名称', key: 'name', sortable: true},
          {
            title: '操作',
            align: 'center',
            width: 240,
            key: 'handle',
            options: ['delete', 'edit']
          }
        ],
        searchs: [
          {title: '策略名称', key: 'name'}
        ],
        count: 0,
        page: {
          pagesize: 10,
          pagenumber: 1
        },
        protocol_types: [{key: 0,value: '局域网'},{key: 1,value: '城域网'},{key: 2,value: '广域网'},{key: 3,value: '无损'},{key: 4,value: 'RDP桥接'}],
        mass_storage_redirections: [{key: 0,value: '读写'},{key: 1,value: '只读'},{key: 2,value: '禁用'}],
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

        if(value != undefined){
          this.page.pagenumber = value;
        }
        getPoliciesData(this.page).then(res => {
         res.data.forEach((item,index)=>{
           item['_disabled'] = !item.selectable;
         })
          this.tableData = res.data;
          this.count = res.count
        })
      },
      addDefault () {
        return  {
          usb_redirection: true,
          mass_storage_redirection: 0,
          printer_redirection: true,
          lock_screen: true,
          auto_protocol: true,
          protocol_type: 0,
          auto_fps: true,
          fps: 20,
          bit_rate: 8,
          quality: 95,
          auto_login: true,
          dedicated_desktop: true,
          mac_addr_filter: false,
          d3d: false,
          gateway: false,
          idv_mode: false,
          mac_addr_string : '',
          linkage_shutdown:false,
          name : ''
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
        deletePolicies(params).then(res => {
          this.$Message.info('删除成功');
          this.page.pagenumber = 1;
          this.handleList()
        })
      },
      exportExcel() {
        this.$refs.tables.exportCsv({
          filename: `table-${(new Date()).valueOf()}.csv`
        })
      },
      openAdd() {
        this.editForm = this.addDefault();
        this.model.edit.open = true;
        this.expert = false;
        this.model.edit.title = '新增策略';
      },
      openEdit(params) {
        let id = this.tableData[params.index].id;
        getPoliciesInfo(id).then(res => {
          this.editForm = res;
          this.expert = false;
          this.model.edit.open = true;
          this.model.edit.title = '编辑策略';
        })

      },
      onEdit() {
        this.$refs['editForm'].validate((valid) => {
          if (valid) {
             const res = this.editForm;
              editPolicies(res).then(res => {
                if(this.editForm.id != undefined){
                  this.$Message.success('修改成功');
                }else{
                  this.$Message.success('新增成功');
                }
                this.$refs['editForm'].resetFields();
                this.editForm = this.addDefault();
                this.model.edit.open = false;
                this.model.edit.loading  = true;
                this.handleList()
              },err=>{
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
        this.$refs['editForm'].resetFields();
        this.$Message.info('取消');
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

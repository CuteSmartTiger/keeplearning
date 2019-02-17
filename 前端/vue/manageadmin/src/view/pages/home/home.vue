<template>
  <div>
    <Row :gutter="20">
      <i-col  span="8">
      <Row :gutter="20" align="top" >
        <i-col :key="`infor-0`" style="height: 120px;margin-bottom: 20px;">
          <infor-card shadow :color="inforCardData[0].color" :icon="inforCardData[0].icon" :icon-size="36">
            <count-to :end="inforCardData[0].count" count-class="count-style"/>
            <p>{{ inforCardData[0].title }}</p>
          </infor-card>
        </i-col>
        <i-col  :key="`infor-1`" style="height: 120px;margin-bottom: 20px;">
          <infor-card shadow :color="inforCardData[1].color" :icon="inforCardData[1].icon" :icon-size="36">
            <router-link to="server-setting/virtual_manage_page"><count-to :end="inforCardData[1].count" count-class="count-style"/></router-link>
            <p>{{ inforCardData[1].title }}</p>
          </infor-card>
        </i-col>
      </Row>
      </i-col>
      <i-col span="8" ><Card shadow style="height: 260px;">
        <chart-pie style="height: 200px;" :value="userData" text="用户数" v-if="chartShow"></chart-pie>
        <p style="text-align: center">
          <span :style="{color:'#3399ff',margin:'0 10px'}">在线：{{userData[0].value}}</span>
          <span :style="{color:'#FFB400',margin:'0 10px'}">离线：{{userData[1].value}}</span>
        </p>
      </Card></i-col>
      <i-col span="8">
        <Card shadow style="height: 260px;">
          <chart-pie style="height: 200px;" :value="vmData" text="虚拟机数" v-if="chartShow"></chart-pie>
        <p style="text-align: center">
          <span :style="{color:'#3399ff',margin:'0 10px'}">开机：{{vmData[0].value}}</span>
          <span :style="{color:'#FFB400',margin:'0 10px'}">关机：{{vmData[1].value}}</span>
        </p>
        </Card>
      </i-col>
    </Row>
    <Row style="margin-top: 20px;">
      <Echart1 />
    </Row>
  </div>
</template>

<script>
import InforCard from '_c/info-card'
import CountTo from '_c/count-to'
import { ChartPie, ChartBar } from '_c/charts'
import Example from './example.vue'
import Echart1 from './echart1.vue'
import {getIndexparams } from '@/api/home'
export default {
  name: 'home',
  components: {
    InforCard,
    CountTo,
    ChartPie,
    ChartBar,
    Example,
    Echart1
  },
  data () {
    return {
      chartShow:false,
      inforCardData: [
        { title: '池个数', icon: 'ios-cube', count: 0, color: '#5cadff' },
        { title: '服务器个数', icon: 'ios-desktop', count: 0, color: '#2b85e4' }
      ],
      userData: [
        {value: 0, name: '在线'},
        {value: 0, name: '离线'},
      ],
      vmData: [
        {value: 0, name: '开机'},
        {value: 0, name: '关机'},
      ],
      barData: {
        Mon: 13253,
        Tue: 34235,
        Wed: 26321,
        Thu: 12340,
        Fri: 24643,
        Sat: 1322,
        Sun: 1324
      }
    }
  },
  methods: {
    handleGetDatas() {
      getIndexparams().then(res => {
          this.inforCardData[0].count = res.pool || 0;
          this.inforCardData[1].count = res.hostserver || 0;
          this.userData[0].value = res.useronline  || 0;
          this.userData[1].value = res.useroffline  || 0;
          this.vmData[0].value = res.vmrun  || 0;
          this.vmData[1].value = res.vmoff  || 0;
          this.chartShow = true;
      })
    }
  },
  mounted () {
    this.handleGetDatas()
  }
}
</script>

<style lang="less">
.count-style{
  font-size: 50px;
}
</style>

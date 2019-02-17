<template>
<div style="background: none">
    <Form ref="formInline" :model="formSearch" inline>
      <FormItem >
        <Select v-model.sync="formSearch.type"  @on-change = "setSearchType" :style="{width: '200px'}">
          <Option v-for="item in types"  :value="item.id" :key="`${item.name+item.id}`">{{ item.name }}</Option>
        </Select>
      </FormItem>
      <FormItem>
        <Select v-model.sync="formSearch.id" :style="{width: '200px'}" >
          <Option v-for="(item ,index) in ids"  :value="item.id" :key="`${item.name+item.id}`" >{{ item.name }}</Option>
        </Select>
      </FormItem>
      <FormItem>
        <Button type="primary" @click="handleGetDatas('formInline')">查询</Button>
      </FormItem>
    </Form>
    <Card  style="margin-top: 20px;" >  <div ref="cpu"  style="height: 310px;"></div></Card>
    <Card  style="margin-top: 20px;" >  <div ref="memory"  style="height: 310px;"></div></Card>
    <Card  style="margin-top: 20px;" >  <div ref="vif"  style="height: 310px;"></div></Card>
</div>
</template>

<script>
import echarts from 'echarts'
import { on, off } from '@/libs/tools'
import {getDatas } from '@/api/home'
import {getXenServerHostData} from '@/api/home'
import {getVirtualmachinesData} from '@/api/virtualmachines'
export default {
  name: 'echart2',
  data () {
    return {
      formSearch: {
        type: '',
        id: '',
        start: 604800,
        interval: 3600
      },
      types:[],
      ids: [],
      vms: [],
      hps: [],
      date: [],
      cpu:{chart:null,isShow:true},
      memory:{chart:null,isShow:true},
      vif:{chart:null,isShow:true},
    }
  },
  methods: {
    option1 (datas) {
      const series = [];
      const legends = [];
      datas.forEach((v,index)=>{
        const item = {
          name: v.name,
          type: 'line',
          showSymbol: false,
          hoverAnimation: false,
          itemStyle: {
            normal: {
              lineStyle: {
                width:0.8// 0.1的线条是非常细的了
              }
            }
          },
          data: v.data
        };
        series.push(item);
        legends.push(v.name);
      })
      const  option = {
        title: {
          text: 'CPU利用率(Max=100%)'
        },
        tooltip: {
          trigger: 'axis',
          confine: true,
          formatter: function (datas) {
              var res = datas[0].name + '<br/>', val;
              for(var i = 0, length = datas.length; i < length; i++) {
                val = (datas[i].value*100).toFixed(2) + '%';
                res += datas[i].seriesName + '：' + val + '<br/>';
              }
              return res;

          },
          axisPointer: {
            animation: false
          }
        },
        legend: {
          type: 'scroll',
          orient: 'vertical',
          right: 10,
          top: 50,
          bottom: 20,
          data:legends
        },
        grid: {
          left: '3%',
          right: '10%',
          bottom: '3%',
          containLabel: true
        },
        toolbox: {
          feature: {
              mark : {
                show :  false,
                  title : {
                  mark : '辅助线开关',
                    markUndo : '删除辅助线',
                    markClear : '清空辅助线'
                },
                lineStyle : {
                  width : 2,
                    color : '#1e90ff',
                    type : 'dashed'
                }
              },
              dataZoom : {
                show : false,
                  title : {
                  dataZoom : '区域缩放',
                    dataZoomReset : '区域缩放后退'
                }
              },
              dataView : {
                show :  true,
                  title : '数据视图',
                  readOnly: false,
                  lang: ['数据视图', '关闭', '刷新']
              },
              magicType: {
                show : true,
                  title : {
                  line : '折线图切换',
                    bar : '柱形图切换',
                    stack : '堆积',
                    tiled : '平铺',
                    force: '力导向布局图切换',
                    chord: '和弦图切换',
                    pie: '饼图切换',
                    funnel: '漏斗图切换'
                },
                option: {
                   line: {},
                   bar: {},
                   stack: {},
                   tiled: {},
                   force: {},
                   chord: {},
                   pie: {},
                   funnel: {}
                },
                type : ['line', 'bar']
              },
              restore : {
                show : true,
                  title : '还原'
              },
              saveAsImage : {
                show : true,
                  title : '保存为图片',
                  type : 'png',
                  lang : ['点击保存']
              }


    }
        },
        calculable: true,
        xAxis: {
          type: 'category',
          boundaryGap: false,
          width: '4',
          data: this.date
        },
        yAxis: {
          type: 'value',
          max: 1,
          //y轴刻度
          axisLabel: {
            //设置y轴数值为%
            formatter: function (datas) {

              return datas*100 + '%'
            },
            textStyle: {

            }
          },
          axisLine: {
            lineStyle: {
              type: 'solid',
            }
          }
        },
        series: series
      };
      this.cpu.chart.setOption(option,true)
      on(window, 'resize', this.cpu.chart.resize())

    },
    option2 (datas) {
      const series = [];
      const legends = [];
      let max = null;
      datas.forEach((v,index)=>{
        const item = {
          name: v.name,
          type: 'line',
          showSymbol: false,
          hoverAnimation: false,
          itemStyle: {
            normal: {
              lineStyle: {
                width:0.8// 0.1的线条是非常细的了
              },
              areaStyle: {type: 'default'}
            }
          },
          data: v.data
        };
        if(v.max != undefined){
          max = v.max;
        }
        series.push(item);
        legends.push(v.name);
      })
      const  option = {
        title: {
          text: '内存占用(GB)'
        },
        tooltip: {
          trigger: 'axis',
          confine: true,
          axisPointer: {
            animation: false
          }
        },
        legend: {
          type: 'scroll',
          orient: 'vertical',
          right: 10,
          top: 50,
          bottom: 20,
          data:legends
        },
        grid: {
          left: '3%',
          right: '10%',
          bottom: '3%',
          containLabel: true
        },
        toolbox: {
          feature: {
            mark : {
              show :  false,
              title : {
                mark : '辅助线开关',
                markUndo : '删除辅助线',
                markClear : '清空辅助线'
              },
              lineStyle : {
                width : 2,
                color : '#1e90ff',
                type : 'dashed'
              }
            },
            dataZoom : {
              show : false,
              title : {
                dataZoom : '区域缩放',
                dataZoomReset : '区域缩放后退'
              }
            },
            dataView : {
              show :  true,
              title : '数据视图',
              readOnly: false,
              lang: ['数据视图', '关闭', '刷新']
            },
            magicType: {
              show : true,
              title : {
                line : '折线图切换',
                bar : '柱形图切换',
                stack : '堆积',
                tiled : '平铺',
                force: '力导向布局图切换',
                chord: '和弦图切换',
                pie: '饼图切换',
                funnel: '漏斗图切换'
              },
              option: {
                line: {},
                bar: {},
                stack: {},
                tiled: {},
                force: {},
                chord: {},
                pie: {},
                funnel: {}
              },
              type : ['line', 'bar']
            },
            restore : {
              show : true,
              title : '还原'
            },
            saveAsImage : {
              show : true,
              title : '保存为图片',
              type : 'png',
              lang : ['点击保存']
            }


          }
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: this.date
        },
        yAxis: {
          type: 'value',
          max: max,
        },
        series: series
      };
      this.memory.chart.setOption(option,true)
      on(window, 'resize', this.memory.chart.resize())

    },
    option3 (datas) {
      const series = [];
      const legends = [];
      datas.forEach((v,index)=>{
        const item = {
          name: v.name,
          type: 'line',
          showSymbol: false,
          hoverAnimation: false,
          itemStyle: {
            normal: {
              lineStyle: {
                width:0.8// 0.1的线条是非常细的了
              },
              areaStyle: {type: 'default'}
            }
          },
          data: v.data
        };
        series.push(item);
        legends.push(v.name);
      })
      const  option = {
        title: {
          text:'网络(MBps)'
        },
        tooltip: {
          trigger: 'axis',
          confine: true,
          axisPointer: {
            animation: false
          }
        },
        legend: {
          type: 'scroll',
          orient: 'vertical',
          right: 10,
          top: 50,
          bottom: 20,
          data:legends
        },
        grid: {
          left: '3%',
          right: '10%',
          bottom: '3%',
          containLabel: true
        },
        toolbox: {
          feature: {
            mark : {
              show :  false,
              title : {
                mark : '辅助线开关',
                markUndo : '删除辅助线',
                markClear : '清空辅助线'
              },
              lineStyle : {
                width : 2,
                color : '#1e90ff',
                type : 'dashed'
              }
            },
            dataZoom : {
              show : false,
              title : {
                dataZoom : '区域缩放',
                dataZoomReset : '区域缩放后退'
              }
            },
            dataView : {
              show :  true,
              title : '数据视图',
              readOnly: false,
              lang: ['数据视图', '关闭', '刷新']
            },
            magicType: {
              show : true,
              title : {
                line : '折线图切换',
                bar : '柱形图切换',
                stack : '堆积',
                tiled : '平铺',
                force: '力导向布局图切换',
                chord: '和弦图切换',
                pie: '饼图切换',
                funnel: '漏斗图切换'
              },
              option: {
                line: {},
                bar: {},
                stack: {},
                tiled: {},
                force: {},
                chord: {},
                pie: {},
                funnel: {}
              },
              type : ['line', 'bar']
            },
            restore : {
              show : true,
              title : '还原'
            },
            saveAsImage : {
              show : true,
              title : '保存为图片',
              type : 'png',
              lang : ['点击保存']
            }


          }
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: this.date
        },
        yAxis: {
          type: 'value'
        },
        series: series
      };
      this.vif.chart.setOption(option,true)
      on(window, 'resize', this.vif.chart.resize())


    },
    setSearchType (params) {
        switch (params) {
          case 0:
            this.ids = this.hps;

            break;
          case 1:
            this.ids = this.vms;

            break;
          default:
            break;
        }
      this.formSearch.id = "";
    },
    handleGetDatas() {
      if(this.formSearch.id == "" ||this.formSearch.id == undefined){
        this.$Message.error("请选择查询对象")
        return false;
      }
      getDatas(this.formSearch).then(res => {
        this.date=res.date;
        off(window, 'resize', this.cpu.chart.resize())
        this.option1(res.cpu)
        off(window, 'resize', this.memory.chart.resize())
        this.option2(res.memory);
        off(window, 'resize', this.vif.chart.resize())
        this.option3(res.if);

      },err=>{
        this.memory.isShow = false;
        this.vif.isShow = false;
        this.cpu.isShow = false;

      })
    },
    handleSelects () {
      this.types=[];
      getXenServerHostData().then(res => {
        this.hps = res.data;
        if(this.hps.length>0){
          this.types.push({id:0,name:'虚拟化服务器'});
          if(this.formSearch.id == ''){
            this.ids = this.hps;
            this.formSearch.id = this.hps[0].id;
            this.formSearch.type = 0;
            this.handleGetDatas();
          }
        }
      })
      getVirtualmachinesData({power_state:1}).then(res => {
        this.vms = res.data;
        if(this.vms.length>0){
          this.types.push({id:1,name:'虚拟机'})
          if(this.formSearch.id == ''){
            this.ids = this.vms;
            this.formSearch.id = this.vms[0].id;
            this.formSearch.type = 1;
            this.handleGetDatas();
          }
        }
      })
    }
  },
  mounted () {
    this.memory.chart = echarts.init(this.$refs.memory)
    this.cpu.chart = echarts.init(this.$refs.cpu)
    this.vif.chart = echarts.init(this.$refs.vif)
    this.handleSelects()
  },
  beforeDestroy () {

  }
}
</script>

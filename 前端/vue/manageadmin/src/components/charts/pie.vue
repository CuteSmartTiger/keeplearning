<template>
  <div ref="dom" class="charts chart-pie" ></div>
</template>

<script>
import echarts from 'echarts'
import tdTheme from './theme.json'
import { on, off } from '@/libs/tools'
echarts.registerTheme('tdTheme', tdTheme)
export default {
  name: 'ChartPie',
  props: {
    value: Array,
    text: String,
    subtext: String
  },
  methods: {

  },
  mounted () {

    this.$nextTick(() => {
      let legend = this.value.map(_ => _.name)
      let option = {
        title: {
          text: this.text,
          subtext: this.subtext,
          x: 'left'
        },
        tooltip: {
          trigger: 'item',
          formatter: '{b} : {c} ({d}%)'
        },
        legend: {
          orient: 'vertical',
          left: 'right',
          data: legend
        },
        color:[ '#3399ff','#FFB400'],
        series: [
          {
            type: 'pie',
            radius: ['60%', '90%'],
            avoidLabelOverlap: false,
            //center: ['50%', '60%'],
            data: this.value,
            label: {
              normal: {
                show: false,

                position: 'center'
              },
              emphasis: {
                show: true,
                formatter: '{b}: {c}',
                textStyle: {
                  fontSize: '20',
                  fontWeight: 'bold'
                }
              }
            },
            labelLine: {
              normal: {
                show: false
              }
            },

          }
        ]
      }
      let dom = echarts.init(this.$refs.dom, 'tdTheme')
      dom.setOption(option)
      on(window, 'resize', dom.resize())
    })
  }
}
</script>

<style lang="less">
.charts{
  //
}
</style>

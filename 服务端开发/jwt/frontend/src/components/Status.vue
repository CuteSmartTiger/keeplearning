<template>
  <v-chip small label :color="colorDict[status]" text-color="white">{{ changeDict[status] }}</v-chip>
</template>

<script>
  export default {
    name: 'Status',
    props: ["status"],
    data: () => ({
      changeDict: {
        1: '待测试',
        2: '待审批',
        3: '待执行',
        4: '待验收',
        5: '已完成',
        6: '已取消',
        7: '已拒绝',
      },
      colorDict: {
        1: 'amber',
        2: 'orange',
        3: 'lime',
        4: 'light-green',
        5: 'green',
        6: 'grey',
        7: 'red',
      },
    }),
    mounted: () => ({}),
    methods: {}
  }
</script>

<style scoped>
</style>

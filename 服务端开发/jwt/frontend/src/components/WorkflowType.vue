<template>
  <v-chip small :color="colorDict[workflow_type]" text-color="white">{{ workflow_type }}</v-chip>
</template>

<script>
  export default {
    name: 'WorkflowType',
    props: ["workflow_type"],
    data: () => ({
      colorDict: {
        "上线流程": 'green lighten-1',
        "变更流程": 'orange lighten-2',
        "通用流程": 'blue lighten-1',
      },
    }),
    mounted: () => ({}),
    methods: {}
  }
</script>

<style scoped>
</style>

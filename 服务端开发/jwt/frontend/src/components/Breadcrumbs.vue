<template>
  <v-layout row wrap>
    <v-flex mb-3 xs12>
      <v-breadcrumbs>
        <v-breadcrumbs-item v-for="item in breadcrumbs_items" :key="item.text"
                            :disabled="item.disabled">
          {{ item.text }}
        </v-breadcrumbs-item>
      </v-breadcrumbs>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    name: 'Breadcrumbs',
    props: ["breadcrumbs_items"],
    data: () => ({}),
    mounted: () => ({}),
    methods: {}
  }
</script>

<style scoped>
  .breadcrumbs {
    justify-content: flex-start;
  }
</style>

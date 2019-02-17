<template>
  <div>
    <Row :gutter="16" class="expand-row" >
      <Col span="8" v-for="item in columns">
        <p class="item"><span class="expand-key">{{item.title}}: </span>
          <span class="expand-value">{{ row[item.key]?row[item.key]:'无' }}</span>
        </p>

      </Col>
    </Row>
    <!--<Row class="expand-row">-->
      <!--<Col span="8" v-for="item in columns">-->
      <!--<span class="expand-key">{{item.title}}: </span>-->
      <!--<span class="expand-value">{{ row[item.key] }}</span>-->
      <!--</Col>-->
    <!--</Row>-->
  </div>
</template>
<script>
  export default {
    props: {
      row: Object,
      columns: {
        type: Array,
        default () {
          return []
        }
      }
    }
  };
</script>
<style lang="less">
  .expand-row {
    border:1px solid #d3d3d3;
    padding: 10px;
    .item{
      margin-bottom: 5px;
    }

  }
</style>

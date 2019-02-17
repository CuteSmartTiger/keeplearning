import Vue from 'vue';
import App from './App.vue';

//引入公共的scss   注意：创建项目的时候必须用scss
import './assets/css/basic.scss';   


//请求数据

import VueResource from 'vue-resource';

Vue.use(VueResource);


//配置路由
import router from './router/router.js';

//4、挂载路由

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})



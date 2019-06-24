// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import Vuetify from 'vuetify';
import App from './App';
import router from './router';
import store from './store';
import {utc2local} from './filter';


Vue.use(Vuetify);

// filter utc datetime format
Vue.filter('utc2local', utc2local);

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  data: {
    eventHub: new Vue()
  },
  store,
  template: '<App/>',
  components: {App}
});


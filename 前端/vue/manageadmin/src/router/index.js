import Vue from 'vue'
import Router from 'vue-router'
import routes from './routers'
import CONFIG from '_conf/config'
Vue.use(Router)
const router = new Router({
  routes,
  base: CONFIG.BASE,
  mode: 'history'
})
export default router

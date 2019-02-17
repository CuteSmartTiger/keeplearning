import Vue from 'vue';
import App from './App.vue';


//引入公共的scss   注意：创建项目的时候必须用scss

import './assets/css/basic.scss';   


/*路由的嵌套

  1.配置路由
   {

      path: '/user',

      component: User,
      children:[
        { path: 'useradd', component: UserAdd },

        { path: 'userlist', component: Userlist }

      ]

    }

  2.父路由里面配置子路由显示的地方   <router-view></router-view>
*/



//请求数据


import VueResource from 'vue-resource';
Vue.use(VueResource);




import VueRouter from 'vue-router';

Vue.use(VueRouter);

//1.创建组件


import Home from './components/Home.vue';

import News from './components/News.vue';

import Content from './components/Content.vue';


import User from './components/User.vue';

  import UserAdd from './components/User/UserAdd.vue';
  import Userlist from './components/User/Userlist.vue';



//2.配置路由   注意：名字

const routes = [
  { path: '/home', component: Home },
  { path: '/news', component: News,name:'news' },

  {   
    
    path: '/user',
    
    component: User,
    children:[
      { path: 'useradd', component: UserAdd },

      { path: 'userlist', component: Userlist }

    ]

  },


  { path: '/content/:aid', component: Content },   /*动态路由*/

  { path: '*', redirect: '/home' }   /*默认跳转路由*/
]


//3.实例化VueRouter  注意：名字

const router = new VueRouter({
  mode: 'history',   /*hash模式改为history*/
  routes // （缩写）相当于 routes: routes
})




//4、挂载路由

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})


//5 <router-view></router-view> 放在 App.vue

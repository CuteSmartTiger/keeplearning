import Vue from 'vue';
import Router from 'vue-router';
import views from '@/views';
import store from '@/store';
import axios from 'axios';

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '*',
      redirect: '/'
    },
    {
      path: '/login',
      component: views.Login,
    },
    {
      path: '/',
      component: views.Home,
      children: [
        {
          path: '',
          component: views.Dashboard,
          meta: {requiresAuth: true},
        },
        {
          path: 'deploy',
          component: views.Deploy,
          meta: {requiresAuth: true},
          children: [
            {
              path: 'todo',
              component: views.DeployTodo,
              meta: {requiresAuth: true},
            },
            {
              path: 'create',
              component: views.DeployCreate,
              meta: {requiresAuth: true},
            },
            {
              path: 'history',
              component: views.DeployHistory,
              meta: {requiresAuth: true},
            },
            {
              path: 'detail/:ID',
              component: views.DeployDetail,
              meta: {requiresAuth: true},
            },
          ]
        },
        {
          path: 'change',
          component: views.Change,
          meta: {requiresAuth: true},
          children: [
            {
              path: 'todo',
              component: views.ChangeTodo,
              meta: {requiresAuth: true},
            },
            {
              path: 'create',
              component: views.ChangeCreate,
              meta: {requiresAuth: true},
            },
            {
              path: 'history',
              component: views.ChangeHistory,
              meta: {requiresAuth: true},
            },
            {
              path: 'detail/:ID',
              component: views.ChangeDetail,
              meta: {requiresAuth: true},
            },
          ]
        },
        {
          path: 'user',
          component: views.User,
          meta: {requiresAuth: true},
        },
        {
          path: 'system',
          component: views.System,
          meta: {requiresAuth: true},
        },
      ]
    },
  ]
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    if (store.getters.isLoggedIn) {
      // add global header
      axios.defaults.headers.common.Authorization = `JWT ${localStorage.getItem('token')}`;
      next();
    } else {
      console.log(to.fullPath);
      next({
        path: '/login',
        query: {redirect: to.fullPath},
      });
    }
  } else {
    next(); // make sure to always call next()!
  }
});

export default router;

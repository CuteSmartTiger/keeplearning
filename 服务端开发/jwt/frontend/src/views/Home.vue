<template>
  <v-app id="inspire">
    <v-navigation-drawer
      width="214"
      fixed
      :clipped="$vuetify.breakpoint.lgAndUp"
      app
      v-model="drawer"
    >
      <v-list dense>
        <template v-for="item in navigation_items">
          <v-layout
            row
            v-if="item.heading"
            align-center
            :key="item.heading"
          >
            <v-flex xs6>
              <v-subheader v-if="item.heading">
                {{ item.heading }}
              </v-subheader>
            </v-flex>
            <v-flex xs6 class="text-xs-center">
              <a href="#!" class="body-2 black--text">EDIT</a>
            </v-flex>
          </v-layout>
          <v-list-group
            v-else-if="item.children"
            v-model="item.model"
            :key="item.text"
            :prepend-icon="item.model ? item.icon : item['icon-alt']"
            append-icon=""
          >
            <v-list-tile slot="activator">
              <v-list-tile-content>
                <v-list-tile-title>
                  {{ item.text }}
                </v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <router-link tag="v-list-tile" :to="{ path: child.link }"
                         v-for="(child, i) in item.children"
                         :key="i"
            >
              <v-list-tile-action>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>
                  {{ child.text }}
                </v-list-tile-title>
              </v-list-tile-content>
            </router-link>
          </v-list-group>
          <router-link tag="v-list-tile" :to="{ path: item.link }" v-else @click="" :key="item.text">
            <v-list-tile-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>
                {{ item.text }}
              </v-list-tile-title>
            </v-list-tile-content>
          </router-link>
        </template>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar color="blue" clipped-left fixed app dark>
      <v-toolbar-title class="ml-0 pl-3">
        <v-toolbar-side-icon @click.native.stop="drawer = !drawer"></v-toolbar-side-icon>
        <span class="hidden-xs-only">{{ toolbar.title }}</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu class="mr-5" offset-y left>
        <v-btn icon slot="activator" dark>
          {{ tenant }}
        </v-btn>
      </v-menu>
      <v-spacer></v-spacer>
      <v-menu class="mr-5" offset-y left>
        <v-btn icon slot="activator" dark>
          <v-badge color="red" left style="padding-right: 10px" v-if="todos > 0">
            <span slot="badge">{{ todos }}</span>
          </v-badge>
          {{ username }}
          <v-icon>keyboard_arrow_down</v-icon>
        </v-btn>
        <v-list>
          <v-list-tile v-for="item in operate_items" :key="item.title" @click="toolbarOperate(item.link)">
            <v-list-tile-title class="body-2">{{ item.text }}</v-list-tile-title>
          </v-list-tile>
        </v-list>
      </v-menu>
    </v-toolbar>
    <main>
      <v-content id="main_content">
        <v-container fluid grid-list-md>
          <router-view></router-view>
        </v-container>
      </v-content>
    </main>
    <v-footer class="pa-3" app>
      <v-spacer></v-spacer>
      <div><span style="color: #9E9E9E;">&copy; {{ toolbar.subTitle }}</span></div>
    </v-footer>
    <v-snackbar :color="snackBar.level" :timeout="4000" top="top" right="right"
                :success="snackBar.level === 'success'"
                :info="snackBar.level === 'info'" :warning="snackBar.level === 'warning'"
                :error="snackBar.level === 'error'" @input="closeSnackBar" :value="snackBar.value">
      {{ snackBar.text}}
      <v-btn flat="flat" @click="closeSnackBar" color="white">x</v-btn>
    </v-snackbar>
  </v-app>
</template>

<script>
  import {mapState} from 'vuex';
  import {deployTodos} from '@/api';

  export default {
    name: 'Home',
    data: () => ({
      drawer: true,
      username: localStorage.getItem('username'),
      tenant: localStorage.getItem('tenant'),
      todos: 0,
      toolbar: {
        title: "Dalmore",
        subTitle: 'Project Management & Collaboration System',
      },
      operate_items: [
        {text: '提交Bug'},
        {text: '注销', link: '/logout'},
      ],
      navigation_items: [
        {
          text: '总览',
          icon: 'dashboard',
          link: '/dashboard'
        },
        {
          text: '上线流程',
          icon: 'keyboard_arrow_up',
          'icon-alt': 'keyboard_arrow_down',
          model: false,
          children: [
            {icon: 'list', text: '待办流程', link: '/deploy/todo',},
            {icon: 'add', text: '新建流程', link: '/deploy/create',},
            {icon: 'history', text: '历史流程', link: '/deploy/history',},
          ]
        },
        {
          text: '变更流程',
          icon: 'keyboard_arrow_up',
          'icon-alt': 'keyboard_arrow_down',
          model: false,
          children: [
            {icon: 'list', text: '待办流程', link: '/change/todo',},
            {icon: 'add', text: '新建流程', link: '/change/create',},
            {icon: 'history', text: '历史流程', link: '/change/history',},
          ]
        },
        {
          text: '系统管理',
          icon: 'view_list',
          link: '/system',
        },
        {
          text: '用户管理',
          icon: 'people',
          link: '/user',
        },
      ]
    }),
    computed: mapState([
      'snackBar',
    ]),
    mounted: function () {
      this.navigationInit();
      this.$root.eventHub.$on('set_todos', this.set_todos);
    },
    methods: {
      closeSnackBar() {
        this.$store.dispatch('dismissSnackBar');
      },
      navigationInit() {
        let path = this.$route.path;
        console.log(path);
        if (path !== null && path !== undefined) {
          if (path.indexOf('deploy') !== -1) {
            this.navigation_items[1].model = true;
          } else if (path.indexOf('change') !== -1) {
            this.navigation_items[2].model = true;
          } else {
          }
        }
      },
      toolbarOperate(link) {
        if (link && link == '/logout') {
          this.$store.dispatch('logout');
          this.$router.push('/login');
        }
      },
      set_todos(value) {
        this.todos = value;
      },
    }
  }
</script>

<style scoped>
  .router-link-active {
    background: lightgray;
  }
</style>

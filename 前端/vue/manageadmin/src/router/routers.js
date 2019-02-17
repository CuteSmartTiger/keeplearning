import Main from '@/view/main'
import parentView from '@/components/parent-view'

/**
 * iview-admin中meta除了原生参数外可配置的参数:
 * meta: {
 *  hideInMenu: (false) 设为true后在左侧菜单不会显示该页面选项
 *  notCache: (false) 设为true后页面不会缓存
 *  access: (null) 可访问该页面的权限数组，当前路由设置的权限会影响子路由
 *  icon: (-) 该页面在左侧菜单、面包屑和标签导航处显示的图标，如果是自定义图标，需要在图标名称前加下划线'_'
 * }
 */

export default [
  {
    path: '/login',
    name: 'login',
    meta: {
      notCache:  true,
      title: 'Login - 登录',
      hideInMenu: true
    },
    component: () => import('@/view/login/login.vue')
  },
  {
    path: '/',
    name: '_home',
    redirect: '/login',
    component: Main,
    meta: {

      hideInMenu: true,
      notCache: true
    },
    children: [
      {
        path: '/home',
        name: 'home',
        meta: {
          hideInMenu: true,
          title: '首页',
          notCache: true
        },
        component: () => import('@/view/pages/home')
      }
    ]
  },
  {
    path: '/policies',
    name: 'policies',
    meta: {
      icon: 'logo-buffer',
      title: '策略设置'
    },
    component: Main,
    children: [
      {
        path: 'policies_manage_page',
        name: 'policies_manage_page',
        meta: {
          icon: 'md-trending-up',
          notCache: true,
          title: '策略管理'
        },
        component: () => import('@/view/pages/policies/manage/tables.vue')
      }
    ]
  },
  {
    path: '/user-setting',
    name: 'user-setting',
    meta: {
      icon: 'md-person',
      notCache: true,
      title: '用户设置'
    },
    component: Main,
    children: [
      {
        path: 'user_manage_page',
        name: 'user_manage_page',
        meta: {
          icon: 'md-person',
          notCache: true,
          title: '用户管理'
        },
        component: () => import('@/view/pages/userSetting/userManage/tables.vue')
      },
      {
        path: 'user_group_page',
        name: 'user_group_page',
        meta: {
          icon: 'ios-people',
          notCache: true,
          title: '用户组管理'
        },
        component: () => import('@/view/pages/userSetting/userGroupManage/tables.vue')
      },
      {
        path: 'admin_manage_page',
        name: 'admin_manage_page',
        meta: {
          icon: 'md-settings',
          notCache: true,
          title: '管理员管理'
        },
        component: () => import('@/view/pages/userSetting/adminManage/tables.vue')
      },
      {
        path: 'LDAPobj_page',
        name: 'LDAPobj_page',
        meta: {
          icon: 'md-outlet',
          notCache: true,
          title: 'LDAP对象管理'
        },
        component: () => import('@/view/pages/userSetting/LDAPobjManage/tables.vue')
      }
    ]
  },
  {
    path: '/server-setting',
    name: 'server-setting',
    meta: {
      icon: 'md-briefcase',
      title: '服务器设置'
    },
    component: Main,
    children: [
      {
        path: 'virtual_manage_page',
        name: 'virtual_manage_page',
        meta: {
          icon: 'md-folder',
          title: '虚拟化服务器管理'
        },
        component: () => import('@/view/pages/serverSetting/virtualManage/tables.vue')
      },
      {
        path: 'device_manage_page',
        name: 'device_manage_page',
        meta: {
          icon: 'md-folder',
          title: '设备管理器管理'
        },
        component: () => import('@/view/pages/serverSetting/deviceManage/tables.vue')
      },
      {
        path: 'LDAP_manage_page',
        name: 'LDAP_manage_page',
        meta: {
          icon: 'md-folder',
          title: 'LDAP服务器管理'
        },
        component: () => import('@/view/pages/serverSetting/LDAPServerManage/tables.vue')
      },
      // {
      //   path: 'vessel_manage_page',
      //   name: 'vessel_manage_page',
      //   meta: {
      //     icon: 'soup-can',
      //     title: '容器管理器管理'
      //   },
      //   component: () => import('@/view/pages/serverSetting/vesselManage/tables.vue')
      // }
    ]
  },
  {
    path: '/assignments',
    name: 'assignments',
    meta: {
      icon: 'md-filing',
      title: '资源管理'
    },
    component: Main,
    children: [
      {
        path: 'assignments_manage_page',
        name: 'assignments_manage_page',
        meta: {
          icon: 'md-folder',
          title: '资源分配'
        },
        component: () => import('@/view/pages/assignments/assignmentsManage/tables.vue')
      },
      {
        path: 'terminals_manage_page',
          name: 'terminals_manage_page',
        meta: {
        icon: 'md-folder',
          title: '终端管理'
      },
        component: () => import('@/view/pages/assignments/terminalsManage/tables.vue')
      },
      {
        path: 'virtualmachines_manage_page',
        name: 'virtualmachines_manage_page',
        meta: {
          icon: 'md-folder',
          title: '虚拟机管理'
        },
        component: () => import('@/view/pages/assignments/virtualmachinesManage/tables.vue')
      },
      {
        path: 'virtual_group_page',
        name: 'virtual_group_page',
        meta: {
          icon: 'md-folder',
          title: '虚拟机组管理'
        },
        component: () => import('@/view/pages/assignments/virtualGroupManage/tables.vue')
      },
      {
        path: 'templates_manage_page',
        name: 'templates_manage_page',
        meta: {
          icon: 'md-folder',
          title: '模板管理'
        },
        component: () => import('@/view/pages/assignments/templatesManage/tables.vue')
      }
    ]
  },
  {
    path: '/system',
    name: 'system',
    meta: {
      icon: 'md-settings',
      title: '系统管理'
    },
    component: Main,
    children: [
      {
        path: 'files_manage_page',
        name: 'files_manage_page',
        meta: {
          icon: 'md-folder',
          title: '文件管理'
        },
        component: () => import('@/view/pages/system/filesManage/tables.vue')
      },
      {
        path: 'event_manage_page',
        name: 'event_manage_page',
        meta: {
          icon: 'md-folder',
          title: '事件管理'
        },
        component: () => import('@/view/pages/system/eventManage/tables.vue')
      },
      {
        path: 'license_manage_page',
        name: 'license_manage_page',
        meta: {
          icon: 'md-folder',
          title: '许可证管理'
        },
        component: () => import('@/view/pages/system/licenseManage/tables.vue')
      },
      {
        path: 'system_set_page',
        name: 'system_set_page',
        meta: {
        icon: 'md-folder',
          title: '个性化设置'
        },
        component: () => import('@/view/pages/system/systemSet/tables.vue')
      }

    ]
  },
  {
    path: '/help',
    name: 'help',
    meta: {
      title: '帮助',
      icon: 'ios-book'
    },
    component: Main,
    children: [
      {
        path: 'about',
        name: 'about',
        meta: {
          icon: 'ios-book',
          title: '关于'
        },
        component: () => import('@/view/pages/help/tables.vue')
      }
    ]

  },
  // {
  //   path: '/join',
  //   name: 'join',
  //   component: Main,
  //   children: [
  //     {
  //       path: 'join_page',
  //       name: 'join_page',
  //       meta: {
  //         icon: '_qq',
  //         title: 'QQ群'
  //       },
  //       component: () => import('@/view/join-page.vue')
  //     }
  //   ]
  // },
  // {
  //   path: '/components',
  //   name: 'components',
  //   meta: {
  //     icon: 'logo-buffer',
  //     title: '组件'
  //   },
  //   component: Main,
  //   children: [
  //     {
  //       path: 'count_to_page',
  //       name: 'count_to_page',
  //       meta: {
  //         icon: 'md-trending-up',
  //         title: '数字渐变'
  //       },
  //       component: () => import('@/view/components/count-to/count-to.vue')
  //     },
  //     {
  //       path: 'tables_page',
  //       name: 'tables_page',
  //       meta: {
  //         icon: 'md-grid',
  //         title: '多功能表格'
  //       },
  //       component: () => import('@/view/components/tables/tables.vue')
  //     },
  //     {
  //       path: 'split_pane_page',
  //       name: 'split_pane_page',
  //       meta: {
  //         icon: 'md-pause',
  //         title: '分割窗口'
  //       },
  //       component: () => import('@/view/components/split-pane/split-pane.vue')
  //     },
  //     {
  //       path: 'markdown_page',
  //       name: 'markdown_page',
  //       meta: {
  //         icon: 'logo-markdown',
  //         title: 'Markdown编辑器'
  //       },
  //       component: () => import('@/view/components/markdown/markdown.vue')
  //     },
  //     {
  //       path: 'editor_page',
  //       name: 'editor_page',
  //       meta: {
  //         icon: 'ios-create',
  //         title: '富文本编辑器'
  //       },
  //       component: () => import('@/view/components/editor/editor.vue')
  //     },
  //     {
  //       path: 'icons_page',
  //       name: 'icons_page',
  //       meta: {
  //         icon: '_bear',
  //         title: '自定义图标'
  //       },
  //       component: () => import('@/view/components/icons/icons.vue')
  //     }
  //   ]
  // },
  // {
  //   path: '/update',
  //   name: 'update',
  //   meta: {
  //     icon: 'md-cloud-upload',
  //     title: '数据上传'
  //   },
  //   component: Main,
  //   children: [
  //     {
  //       path: 'update_table_page',
  //       name: 'update_table_page',
  //       meta: {
  //         icon: 'ios-document',
  //         title: '上传Csv'
  //       },
  //       component: () => import('@/view/update/update-table.vue')
  //     },
  //     {
  //       path: 'update_paste_page',
  //       name: 'update_paste_page',
  //       meta: {
  //         icon: 'md-clipboard',
  //         title: '粘贴表格数据'
  //       },
  //       component: () => import('@/view/update/update-paste.vue')
  //     }
  //   ]
  // },
  // {
  //   path: '/excel',
  //   name: 'excel',
  //   meta: {
  //     icon: 'ios-stats',
  //     title: 'EXCEL导入导出'
  //   },
  //   component: Main,
  //   children: [
  //     {
  //       path: 'upload-excel',
  //       name: 'upload-excel',
  //       meta: {
  //         icon: 'md-add',
  //         title: '导入EXCEL'
  //       },
  //       component: () => import('@/view/excel/upload-excel.vue')
  //     },
  //     {
  //       path: 'export-excel',
  //       name: 'export-excel',
  //       meta: {
  //         icon: 'md-download',
  //         title: '导出EXCEL'
  //       },
  //       component: () => import('@/view/excel/export-excel.vue')
  //     }
  //   ]
  // },
  // {
  //   path: '/directive',
  //   name: 'directive',
  //   meta: {
  //     hide: true
  //   },
  //   component: Main,
  //   children: [
  //     {
  //       path: 'directive_page',
  //       name: 'directive_page',
  //       meta: {
  //         icon: 'ios-navigate',
  //         title: '指令'
  //       },
  //       component: () => import('@/view/directive/directive.vue')
  //     }
  //   ]
  // },
  // {
  //   path: '/multilevel',
  //   name: 'multilevel',
  //   meta: {
  //     icon: 'md-menu',
  //     title: '多级菜单'
  //   },
  //   component: Main,
  //   children: [
  //     {
  //       path: 'level_2_1',
  //       name: 'level_2_1',
  //       meta: {
  //         icon: 'md-funnel',
  //         title: '二级-1'
  //       },
  //       component: () => import('@/view/multilevel/level-2-1.vue')
  //     },
  //     {
  //       path: 'level_2_2',
  //       name: 'level_2_2',
  //       meta: {
  //         access: ['super_admin'],
  //         icon: 'md-funnel',
  //         showAlways: true,
  //         title: '二级-2'
  //       },
  //       component: parentView,
  //       children: [
  //         {
  //           path: 'level_2_2_1',
  //           name: 'level_2_2_1',
  //           meta: {
  //             icon: 'md-funnel',
  //             title: '三级'
  //           },
  //           component: () => import('@/view/multilevel/level-2-2/level-3-1.vue')
  //         }
  //       ]
  //     },
  //     {
  //       path: 'level_2_3',
  //       name: 'level_2_3',
  //       meta: {
  //         icon: 'md-funnel',
  //         title: '二级-3'
  //       },
  //       component: () => import('@/view/multilevel/level-2-3.vue')
  //     },
  //   ]
  // },
  {
    path: '/401',
    name: 'error_401',
    meta: {
      hideInMenu: true
    },
    component: () => import('@/view/error-page/401.vue')
  },
  {
    path: '/500',
    name: 'error_500',
    meta: {
      hideInMenu: true
    },
    component: () => import('@/view/error-page/500.vue')
  },
  {
    path: '*',
    name: 'error_404',
    meta: {
      hideInMenu: true
    },
    component: () => import('@/view/error-page/404.vue')
  }
]

export default [
  // *===============================================---*
  // *--------- USER ---- ---------------------------------------*
  // *===============================================---*
  {
    path: '/apps/users/list',
    name: 'apps-users-list',
    component: () => import('@/views/apps/user/users-list/UsersList.vue'),
  },
  // {
  //   path: '/apps/users/view/:id',
  //   name: 'apps-users-view',
  //   component: () => import('@/views/apps/user/users-view/UsersView.vue'),
  // },
  // {
  //   path: '/apps/users/edit/:id',
  //   name: 'apps-users-edit',
  //   component: () => import('@/views/apps/user/users-edit/UsersEdit.vue'),
  // },
  // *===============================================---*
  // *--------- Teams ---- ---------------------------------------*
  // *===============================================---*
  {
    path: '/apps/teams/list',
    name: 'apps-teams-list',
    component: () => import('@/views/apps/team/teams-list/TeamsList.vue'),
  },
  // {
  //   path: '/apps/users/view/:id',
  //   name: 'apps-users-view',
  //   component: () => import('@/views/apps/user/users-view/TeamsView.vue'),
  // },
  // {
  //   path: '/apps/users/edit/:id',
  //   name: 'apps-users-edit',
  //   component: () => import('@/views/apps/user/users-edit/TeamsEdit.vue'),
  // },
]

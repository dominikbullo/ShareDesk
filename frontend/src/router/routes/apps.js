export default [
  // *===============================================---*
  // *--------- USERS ----------------------------------*
  // *===============================================---*
  {
    path: '/apps/users/list',
    name: 'apps-users-list',
    component: () => import('@/views/apps/user/users-list/UsersList.vue'),
  },
  {
    path: '/apps/users/view/:id',
    name: 'apps-users-view',
    component: () => import('@/views/apps/user/users-view/UsersView.vue'),
  },
  // {
  //   path: '/apps/users/edit/:id',
  //   name: 'apps-users-edit',
  //   component: () => import('@/views/apps/user/users-edit/UsersEdit.vue'),
  // },
  // *===============================================---*
  // *--------- TEAMS ----------------------------------*
  // *===============================================---*
  {
    path: '/apps/teams/list',
    name: 'apps-teams-list',
    component: () => import('@/views/apps/team/teams-list/TeamsList.vue'),
  },
  {
    path: '/apps/teams/view/:id',
    name: 'apps-teams-view',
    component: () => import('@/views/apps/team/teams-view/TeamsView.vue'),
  },
  // {
  //   path: '/apps/users/edit/:id',
  //   name: 'apps-users-edit',
  //   component: () => import('@/views/apps/user/users-edit/TeamsEdit.vue'),
  // },
  // *===============================================---*
  // *--------- RESERVATIONS ---------------------------*
  // *===============================================---*
  {
    path: '/apps/reservations/booking',
    name: 'apps-reservations-booking',
    component: () => import('@/views/apps/reservation/reservation-booking/ReservationsBooking.vue'),
  },
  {
    path: '/apps/reservations/user',
    name: 'apps-reservations-user',
    component: () => import('@/views/apps/reservation/reservation-user/UserReservationsList.vue'),
  },
  {
    path: '/apps/reservations/manager',
    name: 'apps-reservations-manager',
    component: () => import('@/views/apps/reservation/reservation-manager/ReservationManager.vue'),
  },
  // *===============================================---*
  // *--------- WORKSPACES -----------------------------*
  // *===============================================---*
  {
    path: '/apps/workspaces/list',
    name: 'apps-workspaces-list',
    component: () => import('@/views/apps/workplace/spots-list/SpotsList.vue'),
  },
  {
    path: '/apps/workspaces/issues/list',
    name: 'apps-workspaces-issues-list',
    component: () => import('@/views/apps/workplace/issues-list/SpotIssuesList.vue'),
  },
  {
    path: '/apps/workspaces/layout/list',
    name: 'apps-workspaces-layout-list',
    component: () => import('@/views/apps/workplace/layout-list/RoomLayoutList.vue'),
  },
  {
    path: '/apps/workspaces/layout/edit/:id/',
    name: 'apps-workspaces-layout-edit',
    component: () => import('@/views/apps/workplace/layout-edit/RoomLayoutEdit.vue'),
  },
]

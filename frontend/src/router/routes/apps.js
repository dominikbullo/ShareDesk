export default [
  // *===============================================---*
  // *--------- USERS ----------------------------------*
  // *===============================================---*
  {
    path: '/apps/users/list',
    name: 'apps-users-list',
    component: () => import('@/views/apps/user/users-list/UsersList.vue'),
    meta: {
      pageTitle: 'Users List',
      breadcrumb: [
        {
          text: 'Users',
          to: { name: 'apps-users-list' },
        },
        {
          text: 'List',
          active: true,
        },
      ],
    },
  },
  {
    path: '/apps/users/view/:id',
    name: 'apps-users-view',
    component: () => import('@/views/apps/user/users-view/UsersView.vue'),
    meta: {
      pageTitle: 'User View',
      breadcrumb: [
        {
          text: 'Users',
          to: { name: 'apps-users-list' },
        },
        {
          text: 'View',
          active: true,
        },
      ],
    },
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
    meta: {
      pageTitle: 'Teams List',
      breadcrumb: [
        {
          text: 'Teams',
          to: { name: 'apps-teams-list' },
        },
        {
          text: 'List',
          active: true,
        },
      ],
    },
  },
  {
    path: '/apps/teams/view/:id',
    name: 'apps-teams-view',
    component: () => import('@/views/apps/team/teams-view/TeamsView.vue'),
    meta: {
      pageTitle: 'Team View',
      breadcrumb: [
        {
          text: 'Teams',
          to: { name: 'apps-teams-list' },
        },
        {
          text: 'View',
          active: true,
        },
      ],
    },
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
    meta: {
      pageTitle: 'Reservations',
      breadcrumb: [
        {
          text: 'Reservations',
          to: { name: 'apps-reservations-booking' },
        },
        {
          text: 'Bookings',
          active: true,
        },
      ],
    },
  },
  {
    path: '/apps/reservations/user',
    name: 'apps-reservations-user',
    component: () => import('@/views/apps/reservation/reservation-user/UserReservationsList.vue'),
    meta: {
      pageTitle: 'My reservations',
      breadcrumb: [
        {
          text: 'Reservations',
          to: { name: 'apps-reservations-booking' },
        },
        {
          text: 'My reservations',
        },
        {
          text: 'List',
          active: true,
        },
      ],
    },
  },
  {
    path: '/apps/reservations/manager',
    name: 'apps-reservations-manager',
    component: () => import('@/views/apps/reservation/reservation-manager/ReservationManager.vue'),
    meta: {
      pageTitle: 'Reservations Manager',
      breadcrumb: [
        {
          text: 'Reservations',
          to: { name: 'apps-reservations-booking' },
        },
        {
          text: 'Manager',
          active: true,
        },
      ],
    },
  },
  // *===============================================---*
  // *--------- WORKSPACES -----------------------------*
  // *===============================================---*
  {
    path: '/apps/workspaces/list',
    name: 'apps-workspaces-list',
    component: () => import('@/views/apps/workplace/spots-list/SpotsList.vue'),
    meta: {
      pageTitle: 'Spot List',
      breadcrumb: [
        {
          text: 'Workspaces',
          to: { name: 'apps-workspaces-list' },
        },
        {
          text: 'Spots',
          to: { name: 'apps-workspaces-list' },
        },
        {
          text: 'List',
          active: true,
        },
      ],
    },
  },
  {
    path: '/apps/workspaces/issues/list',
    name: 'apps-workspaces-issues-list',
    component: () => import('@/views/apps/workplace/issues-list/SpotIssuesList.vue'),
    meta: {
      pageTitle: 'Issue List',
      breadcrumb: [
        {
          text: 'Workspaces',
          to: { name: 'apps-workspaces-list' },
        },
        {
          text: 'Issues',
          to: { name: 'apps-issues-list' },
        },
        {
          text: 'List',
          active: true,
        },
      ],
    },
  },
  {
    path: '/apps/workspaces/layout/list',
    name: 'apps-workspaces-layout-list',
    component: () => import('@/views/apps/workplace/layout-list/RoomLayoutList.vue'),
    meta: {
      pageTitle: 'Room Layouts List',
      breadcrumb: [
        {
          text: 'Workspaces',
          to: { name: 'apps-workspaces-layout-list' },
        },
        {
          text: 'Layout',
        },
        {
          text: 'Room Layout',
        },
        {
          text: 'List',
          active: true,
        },
      ],
    },
  },
  {
    path: '/apps/workspaces/layout/edit/:id/',
    name: 'apps-workspaces-layout-edit',
    component: () => import('@/views/apps/workplace/layout-edit/RoomLayoutEdit.vue'),
    meta: {
      pageTitle: 'Room Layouts List',
      breadcrumb: [
        {
          text: 'Workspaces',
          to: { name: 'apps-workspaces-layout-list' },
        },
        {
          text: 'Layout',
        },
        {
          text: 'Room Layout',
        },
        {
          text: 'Edit',
          active: true,
        },
      ],
    },
  },
]

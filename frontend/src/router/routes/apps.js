import i18n from '@/libs/i18n'

export default [
  // *===============================================---*
  // *--------- USERS ----------------------------------*
  // *===============================================---*
  {
    path: '/apps/users/list',
    name: 'apps-users-list',
    component: () => import('@/views/apps/user/users-list/UsersList.vue'),
    meta: {
      pageTitle: i18n.t('Users List'),
      breadcrumb: [
        {
          text: i18n.t('Users'),
          to: { name: 'apps-users-list' },
        },
        {
          text: i18n.t('List'),
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
      pageTitle: i18n.t('User View'),
      breadcrumb: [
        {
          text: i18n.t('Users'),
          to: { name: 'apps-users-list' },
        },
        {
          text: i18n.t('View'),
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
      pageTitle: i18n.t('Teams List'),
      breadcrumb: [
        {
          text: i18n.t('Teams'),
          to: { name: 'apps-teams-list' },
        },
        {
          text: i18n.t('List'),
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
      pageTitle: i18n.t('Team View'),
      breadcrumb: [
        {
          text: i18n.t('Teams'),
          to: { name: 'apps-teams-list' },
        },
        {
          text: i18n.t('View'),
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
      pageTitle: i18n.t('Reservations'),
      breadcrumb: [
        {
          text: i18n.t('Reservations'),
          to: { name: 'apps-reservations-booking' },
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
      pageTitle: i18n.t('My reservations'),
      breadcrumb: [
        {
          text: i18n.t('Reservations'),
          to: { name: 'apps-reservations-booking' },
        },
        {
          text: i18n.t('My reservations'),
        },
        {
          text: i18n.t('List'),
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
      action: 'write',
      resource: 'Reservations',
      pageTitle: i18n.t('Reservations Manager'),
      breadcrumb: [
        {
          text: i18n.t('Reservations'),
          to: { name: 'apps-reservations-booking' },
        },
        {
          text: i18n.t('Manager'),
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
      pageTitle: i18n.t('Spot List'),
      breadcrumb: [
        {
          text: i18n.t('Workspaces'),
          to: { name: 'apps-workspaces-list' },
        },
        {
          text: i18n.t('Spots'),
          to: { name: 'apps-workspaces-list' },
        },
        {
          text: i18n.t('List'),
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
      pageTitle: i18n.t('Issue List'),
      breadcrumb: [
        {
          text: i18n.t('Workspaces'),
          to: { name: 'apps-workspaces-list' },
        },
        {
          text: i18n.t('Issues'),
          to: { name: 'apps-issues-list' },
        },
        {
          text: i18n.t('List'),
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
      pageTitle: i18n.t('Room Layouts List'),
      breadcrumb: [
        {
          text: i18n.t('Workspaces'),
          to: { name: 'apps-workspaces-layout-list' },
        },
        {
          text: i18n.t('Layout'),
        },
        {
          text: i18n.t('Room Layout'),
        },
        {
          text: i18n.t('List'),
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
          text: i18n.t('Workspaces'),
          to: { name: 'apps-workspaces-layout-list' },
        },
        {
          text: i18n.t('Layout'),
        },
        {
          text: i18n.t('Room Layout'),
        },
        {
          text: i18n.t('Edit'),
          active: true,
        },
      ],
    },
  },
]

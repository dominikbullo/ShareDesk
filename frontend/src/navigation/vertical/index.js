export default [
  {
    title: 'Home',
    route: 'home',
    icon: 'HomeIcon',
  },
  {
    title: 'Reservations',
    route: 'apps-reservations-list',
    icon: 'ListIcon',
  },
  // {
  //   title: 'My reservations',
  //   route: 'apps-reservations-list',
  //   icon: 'HomeIcon',
  // },
  {
    title: 'Users',
    icon: 'HomeIcon',
    children: [
      {
        title: 'Users list',
        route: 'apps-users-list',
        icon: 'UserIcon',
      },
      {
        title: 'Teams list',
        route: 'apps-teams-list',
        icon: 'UsersIcon',
      },
    ],
  },
  {
    title: 'Workspaces',
    icon: 'HomeIcon',
    children: [
      {
        title: 'Spot list',
        route: 'apps-workspaces-list',
        icon: 'ListIcon',
      },
      {
        title: 'Spot issues',
        route: 'apps-workspaces-issues-list',
        icon: 'AlertTriangleIcon',
      },
    ],
  },
]

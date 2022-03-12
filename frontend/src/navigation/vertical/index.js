export default [
  {
    title: 'Home',
    route: 'home',
    icon: 'HomeIcon',
  },
  {
    title: 'Reservations',
    route: 'apps-reservations-list',
    icon: 'HomeIcon',
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
    title: 'Spot issues',
    route: 'apps-reservations-issues-list',
    icon: 'AlertTriangleIcon',
  },

]

export default [
  {
    title: 'Home',
    route: 'home',
    icon: 'HomeIcon',
  },
  {
    title: 'Reservations',
    route: 'apps-reservations-booking',
    icon: 'ListIcon',
  },
  {
    title: 'My reservations (testing only)',
    route: 'apps-reservations-user',
    icon: 'HomeIcon',
  },
  {
    title: 'Reservation manager (testing only)',
    route: 'apps-reservations-manager',
    icon: 'HomeIcon',
  },
  {
    title: 'Layout list (testing only)',
    route: 'apps-workspaces-layout-list',
    icon: 'HomeIcon',
  },
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

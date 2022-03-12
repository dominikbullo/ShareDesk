export default [
  {
    title: 'Home',
    route: 'home',
    icon: 'HomeIcon',
  },
  {
    title: 'Reservations',
    route: '#',
    icon: 'HomeIcon',
  },
  {
    title: 'My reservations',
    route: '#',
    icon: 'HomeIcon',
  },
  {
    title: 'Teams',
    icon: 'HomeIcon',
    children: [
      {
        title: 'Users list',
        route: 'home',
        icon: 'UserIcon',
      },
      {
        title: 'Teams list',
        route: 'home',
        icon: 'UsersIcon',
      },
    ],
  },
  {
    title: 'Problems',
    route: '#',
    icon: 'AlertTriangleIcon',
  },

]

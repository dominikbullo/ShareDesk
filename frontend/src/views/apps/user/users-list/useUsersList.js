import { ref, watch, computed } from '@vue/composition-api'

// Notification
import { useToast } from 'vue-toastification/composition'
import ToastificationContent from '@core/components/toastification/ToastificationContent.vue'
import store from '@/store'
import { formatDate } from '@/utils/filter'

export default function useUsersList() {
  // Use toast
  const toast = useToast()

  const refUserListTable = ref(null)

  // Table Handlers
  const tableColumns = [
    { key: 'user', sortable: true },
    { key: 'role', sortable: true },
    { key: 'is_active', sortable: false },
    {
      key: 'registered_at',
      label: 'Register',
      sortable: true,
      formatter: value => formatDate(value, 'shortWithTime'),
    },
    {
      key: 'teams',
      label: 'Teams',
    },
    // { key: 'status', sortable: true },
    { key: 'actions' },
  ]
  const perPage = ref(10)
  const totalUsers = ref(0)
  const currentPage = ref(1)
  const perPageOptions = [5, 10, 25, 50, 100]
  const searchQuery = ref('')
  const sortBy = ref('id')
  const isSortDirDesc = ref(true)
  const roleFilter = ref(null)
  const planFilter = ref(null)
  const statusFilter = ref(true)
  const teamFilter = ref(null)

  const dataMeta = computed(() => {
    const localItemsCount = refUserListTable.value ? refUserListTable.value.localItems.length : 0
    return {
      from: perPage.value * (currentPage.value - 1) + (localItemsCount ? 1 : 0),
      to: perPage.value * (currentPage.value - 1) + localItemsCount,
      of: totalUsers.value,
    }
  })

  const refetchData = () => {
    refUserListTable.value.refresh()
  }

  watch([currentPage, perPage, searchQuery, roleFilter, planFilter, statusFilter], () => {
    refetchData()
  })

  const fetchUsers = (ctx, callback) => {
    store
      .dispatch('app-user/fetchUsers', {
        search: searchQuery.value,
        perPage: perPage.value,
        page: currentPage.value,
        ordering: isSortDirDesc.value ? sortBy.value : `-${sortBy.value}`,
        role: roleFilter.value,
        teams: teamFilter.value,
        // plan: planFilter.value,
        is_active: statusFilter.value,
      })
      .then(response => {
        const users = response.data.results

        callback(users)
        totalUsers.value = response.data.count
      })
      .catch(() => {
        toast({
          component: ToastificationContent,
          props: {
            title: 'Error fetching users list',
            icon: 'AlertTriangleIcon',
            variant: 'danger',
          },
        })
      })
  }

  // *===============================================---*
  // *--------- UI ---------------------------------------*
  // *===============================================---*

  const resolveUserRoleVariant = role => {
    if (role === 'admin') return 'danger'
    return 'primary'
  }

  const resolveUserRoleIcon = role => {
    if (role === 'admin') return 'ServerIcon'
    return 'UserIcon'
  }

  const resolveUserStatusVariant = status => {
    if (status === 'pending') return 'warning'
    if (status === 'active') return 'success'
    if (status === 'inactive') return 'secondary'
    return 'primary'
  }

  const resolveUserIsActiveVariant = status => {
    if (status) return 'success'
    return 'danger'
  }

  return {
    fetchUsers,
    tableColumns,
    perPage,
    currentPage,
    totalUsers,
    dataMeta,
    perPageOptions,
    searchQuery,
    sortBy,
    isSortDirDesc,
    refUserListTable,

    resolveUserRoleVariant,
    resolveUserRoleIcon,
    resolveUserStatusVariant,
    resolveUserIsActiveVariant,

    refetchData,

    // Extra Filters
    roleFilter,
    planFilter,
    statusFilter,
    teamFilter,
  }
}
